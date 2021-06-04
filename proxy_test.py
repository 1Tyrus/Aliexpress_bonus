import os
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver import FirefoxProfile

import main as main

req_proxy = RequestProxy()  # you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list()  # this will create proxy list

profile = FirefoxProfile(r'C:\Programmi Portable\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
torexe = os.popen(r'C:\Programmi Portable\\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

PROXY = []
for proxy in proxies:
    if proxy.country == 'Italy' or proxy.country == 'France' or proxy.country == 'Germany' or proxy.country == 'Poland':
        PROXY.append(proxy)


def set_proxy(p):
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": p.get_address(),
        "ftpProxy": p.get_address(),
        "sslProxy": p.get_address(),
        "proxyType": "MANUAL",
    }


for proxy in PROXY:
    set_proxy(proxy)
    browser = webdriver.Firefox()
    try:
        main.getBonus(browser=browser)
    except WebDriverException:
        print("Proxy non funziona....cambio")
        browser.quit()
    time.sleep(2)