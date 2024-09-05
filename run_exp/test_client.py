from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import requests
from time import sleep

import os
import sys


def main(args):
    alg = args[0]
    url = "http://100.64.0.2/myindex_"
    if alg == "BB":
        url = url + "BB.html"
    if alg == "RB":
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
    driver=webdriver.Chrome(options=options)

    try:
        driver.get(url)
        sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    prog = sys.argv[0]
    args = sys.argv[1:]
    num_args = len(args)
    if (num_args < 1) :
        sys.stderr.write((u"Usage: %s" +
                          u" <algorithm>\n") %
                         (prog))
        sys.exit(1)

    main(args)