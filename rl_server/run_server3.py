import subprocess
import os
import numpy as np
import sys

PYTHON = "python"
PENSIEVE_PATH = "/home/william/android-measurement/pensieve/"

def main(args):
    alg = args[0]
    server_ip = args[1]
    trace_file = args[2]
    server_script = ""
    
    if alg == "RL":
        server_script = "rl_server_no_training.py"
    elif alg == "fastMPC":
        server_script = "mpc_server.py"
    elif alg == 'robustMPC':
        server_script = "robust_mpc_server.py"
    else:
        server_script = "simple_server.py"
    
    # Run http server
    cmd = [PYTHON, PENSIEVE_PATH + "http_server.py", server_ip]
    http_proc = subprocess.Popen(cmd)

    # Run video server
    print("Server script = " + server_script)
    cmd = [PYTHON, PENSIEVE_PATH + server_script, server_ip, trace_file]
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
    if (num_args < 3) :
        sys.stderr.write((u"Usage: %s" +
                          u" <alg> <bind-ip> <trace-file>\n") %
                         (prog))
        sys.exit(1)

    main(args)