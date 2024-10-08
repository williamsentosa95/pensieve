from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import requests
from time import sleep

import os
import sys


def main(args):
    alg = args[0]
    duration = int(args[1])
    url = "http://100.64.0.1:8000/myindex_"
    if alg == "BB":
        url = url + "BB.html"
    elif alg == "RB":
        url = url + "RB.html"
    elif alg == "BOLA":
        url = url + "BOLA.html"
    elif alg == "fastMPC":
        url = url + "fastMPC.html"
    elif alg == "FESTIVE":
        url = url + "FESTIVE.html"
    elif alg == "FIXED":
        url = url + "FIXED.html"
    elif alg == "robustMPC":
        url = url + "robustMPC.html"
    elif alg == "RL":
        url = url + "RL.html"
    else:
        exit("ALG %s is not supported" % (alg))

    options=Options()
    chrome_driver = '../abr_browser_dir/chromedriver-128'
    options.add_argument('--user-data-dir=' + "/tmp/chrome_user_dir_real_exp_0")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--autoplay-policy=no-user-gesture-required")
    options.add_argument('--no-sandbox')
    options.add_argument("--incognito")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--headless")
    driver=webdriver.Chrome(options=options)

    try:
        sleep(5)
        driver.get(url)
        sleep(duration)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    prog = sys.argv[0]
    args = sys.argv[1:]
    num_args = len(args)
    if (num_args < 2) :
        sys.stderr.write((u"Usage: %s" +
                          u" <algorithm> <duration-second>\n") %
                         (prog))
        sys.exit(1)

    main(args)