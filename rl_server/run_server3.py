import subprocess
import os
import numpy as np
import sys
from datetime import datetime

PYTHON = "python"
PENSIEVE_PATH = "/home/william/android-measurement/pensieve/"
HOME_SERVER_PATH = "/home/william/"
ABR_LOG_PATH = HOME_SERVER_PATH + "abr-log/"

def create_log_dir(trace_folder, exp_condition, exp_name, exp_id):
    if (not os.path.exists(trace_folder)):
        os.mkdir(trace_folder)

    now = datetime.now()
    date_folder = trace_folder + "/" + now.strftime("%m-%d-%Y")
    if (not os.path.exists(date_folder)):
        os.mkdir(date_folder)

    if (exp_condition != ""):
        exp_folder = date_folder + "/" + exp_condition
    
    if (not os.path.exists(exp_folder)):
        os.mkdir(exp_folder)

    if (exp_id > 0):
        exp_folder = exp_folder + "/" + str(exp_id)
    else:
        exp_folder = date_folder + "/default"
    
    if (not os.path.exists(exp_folder)):
        os.mkdir(exp_folder)

    exp_trace_folder = exp_folder + "/" + exp_name
    if (not os.path.exists(exp_trace_folder)):
        os.mkdir(exp_trace_folder)
        
    log_file_name = exp_name + "_" + now.strftime("%H-%M-%S") + ".txt"
    return exp_trace_folder + "/" + log_file_name

def main(args):
    alg = args[0]
    server_ip = args[1]
    exp_condition = args[2]
    exp_id = int(args[3])
    exp_name = args[4]
    server_script = ""
    
    if alg == "RL":
        server_script = "rl_server_no_training.py"
    elif alg == "fastMPC":
        server_script = "mpc_server.py"
    elif alg == 'robustMPC':
        server_script = "robust_mpc_server.py"
    else:
        server_script = "simple_server.py"
    
    log_file = create_log_dir(ABR_LOG_PATH, exp_condition, exp_name, exp_id)

    # Run http server
    script_path = PENSIEVE_PATH + "/rl_server/" + "http_server.py"
    cmd = [PYTHON, script_path, server_ip]
    http_proc = subprocess.Popen(cmd)

    # Run video server
    print("Server script = " + server_script)
    script_path = PENSIEVE_PATH + "/rl_server/" + server_script
    cmd = [PYTHON, script_path, server_ip, log_file]
    video_proc = subprocess.Popen(cmd)

    try:
        http_proc.wait()
    except KeyboardInterrupt:
        http_proc.kill()
        video_proc.kill()
        print("Server termintated!")



if __name__ == '__main__':
    prog = sys.argv[0]
    args = sys.argv[1:]
    num_args = len(args)
    if (num_args < 5) :
        sys.stderr.write((u"Usage: %s" +
                          u" <alg> <bind-ip> <exp-cond> <exp-id> <exp-name>\n") %
                         (prog))
        sys.exit(1)

    main(args)