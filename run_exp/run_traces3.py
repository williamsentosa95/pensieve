import sys
import os
import subprocess
import numpy as np


RUN_SCRIPT = 'run_video3.py'
RANDOM_SEED = 42
RUN_TIME = 10  # sec
MM_DELAY = 40   # millisec


def main():
    print("RUN traces 3")
    trace_path = sys.argv[1]
    abr_algo = sys.argv[2]
    process_id = sys.argv[3]
    ip = sys.argv[4]
    # ip = "100.64.0.1"

    sleep_vec = list(range(1, 10))  # random sleep second

    files = os.listdir(trace_path)

    
    for f in files:
        print("python3 %s %s %s %d %s %s" % (RUN_SCRIPT, ip, abr_algo, RUN_TIME, process_id, f))
        while True:

            np.random.shuffle(sleep_vec)
            sleep_time = sleep_vec[int(process_id)]

            # print("python3 %s %s %s %d %s %s %d" % (RUN_SCRIPT, ip, abr_algo, RUN_TIME, process_id, f, sleep_time))
            # cmd = ["mm-delay", str(MM_DELAY), "mm-link", "12mbps", trace_path + f, "python3", RUN_SCRIPT, ip, abr_algo, str(RUN_TIME), process_id, f, str(sleep_time)]
            cmd = ["mm-delay", str(MM_DELAY), "python3", RUN_SCRIPT, ip, abr_algo, str(RUN_TIME), process_id, f, str(sleep_time)]
            # proc = subprocess.Popen('mm-delay ' + str(MM_DELAY) + 
            #           ' mm-link 12mbps ' + trace_path + f + ' ' +
            #           '/usr/bin/python3 ' + RUN_SCRIPT + ' ' + ip + ' ' +
            #           abr_algo + ' ' + str(RUN_TIME) + ' ' +
            #           process_id + ' ' + f + ' ' + str(sleep_time),
            #           stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            proc = subprocess.Popen(cmd)

            (out, err) = proc.communicate()

            if out == 'done\n':
                break
            else:
                with open('./chrome_retry_log', 'a') as log:
                    log.write(abr_algo + '_' + f + '\n')
                    #log.write(out + '\n')
                    log.write(out.decode("utf-8") + "\n")
                    log.flush()



if __name__ == '__main__':
    main()