import os
import time

from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configuro per usare tor Firefox
'''torexe = os.popen(r'C:\Programmi Portable\\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
profile = FirefoxProfile(r'C:\Programmi Portable\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(options=firefox_options, firefox_profile=profile)'''


def getBonus(browser):
    # 1 Apri temp mail
    browser.get("http://www.temp-mail.org")

    # 2 aspetto che carica pagina per copiare email
    browser.find_element_by_css_selector(".btn-rds:nth-child(1)")
    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-rds:nth-child(1)"))
        )
    except:
        print("bottone non abilitato")
        browser.quit()

    # 3 Copio email
    email = browser.find_element_by_xpath("//*[@id='mail']").get_attribute("value")

    # 4 Apro nuovo tab con twitter
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://mobile.twitter.com")
    time.sleep(2)

    # 5 Clicco su registra
    browser.find_element_by_xpath("//a[@data-testid='signupButton']").click()
    time.sleep(1)

    # 6 Compilo form
    browser.find_element_by_name("name").send_keys("gastone")
    browser.find_element_by_css_selector(
        "div.css-18t94o4.css-901oao.r-k200y.r-1n1174f.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-19h5ruw.r-bcqeeo.r-qvutc0").click()
    browser.find_element_by_name("email").send_keys(email)
    month = Select(browser.find_element_by_xpath("//select[@aria-label='Mese']"))
    month.select_by_visible_text("Luglio")
    day = Select(browser.find_element_by_xpath("//select[@aria-label='Giorno']"))
    day.select_by_visible_text("23")
    year = Select(browser.find_element_by_xpath("//select[@aria-label='Anno']"))
    year.select_by_visible_text("1984")

    # 7 Clicco i vari modali
    time.sleep(1)
    browser.find_element_by_css_selector(
        "div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div/div/span/span[text()='Avanti']").click()
    time.sleep(1)
    browser.find_element_by_css_selector(".css-18t94o4:nth-child(6)>.css-901oao>.css-901oao>.css-901oao").click()
    time.sleep(1)

    # 8 Copio link dalla email
    browser.switch_to.window(browser.window_handles[0])
    browser.execute_script("window.scrollBy(0,550);")
    try:
        element = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.viewLink.title-subject"))
        )
    except:
        print("Codice non visualizzato")
        browser.refresh()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a"))
        )
    except:
        print("Codice non trovato")
        browser.refresh()

    codeLink = browser.find_element_by_xpath("//li[2]/div[2]/span/a").text
    code = codeLink[0:6]  # Prendo i primi 6 caratteri

    # 9 Inserisco codice
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_name("verfication_code").send_keys(code)
    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
    except:
        print("Campo password non trovato")
        browser.refresh()

    # 10 Inserisco password
    password = "edfghjksfuhdjw347"
    browser.find_element_by_name("password").send_keys(password)

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "html body div#react-root div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-13awgt0.r-12vffkv div#layers.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af div.css-1dbjc4n.r-aqfbo4.r-1d2f490.r-12vffkv.r-1xcajam.r-zchlnj div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-1p0dtai.r-1adg3ll.r-1d2f490.r-bnwqim.r-zchlnj.r-ipm5af div.r-1oszu61.r-1phboty.r-1yadl64.r-1p0dtai.r-deolkf.r-1adg3ll.r-eqz5dr.r-1d2f490.r-crgep1.r-ifefl9.r-bcqeeo.r-t60dpp.r-bnwqim.r-zchlnj.r-ipm5af.r-417010 div.css-1dbjc4n.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1ylenci.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x div.css-1dbjc4n.r-14lw9ot.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1h3ijdo.r-136ojw6 div.css-1dbjc4n div.css-1dbjc4n.r-14lw9ot.r-1h3ijdo.r-1j3t67a div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1h3ijdo.r-1777fci.r-1jgb5lz.r-sb58tz.r-13qz1uu div.css-1dbjc4n.r-obd0qt.r-1pz39u2.r-1t2qqvi.r-16y2uox.r-1wbh5a2.r-1777fci.r-1joea0r.r-1vsu8ta.r-18qmn74 div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr"))
        )
    except:
        print("Non riesco a inviare password....Refresh")
        browser.refresh()

    browser.find_element_by_css_selector(
        "html body div#react-root div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-13awgt0.r-12vffkv div#layers.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af div.css-1dbjc4n.r-aqfbo4.r-1d2f490.r-12vffkv.r-1xcajam.r-zchlnj div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-12vffkv div.css-1dbjc4n.r-1p0dtai.r-1adg3ll.r-1d2f490.r-bnwqim.r-zchlnj.r-ipm5af div.r-1oszu61.r-1phboty.r-1yadl64.r-1p0dtai.r-deolkf.r-1adg3ll.r-eqz5dr.r-1d2f490.r-crgep1.r-ifefl9.r-bcqeeo.r-t60dpp.r-bnwqim.r-zchlnj.r-ipm5af.r-417010 div.css-1dbjc4n.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1ylenci.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x div.css-1dbjc4n.r-14lw9ot.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-1h3ijdo.r-136ojw6 div.css-1dbjc4n div.css-1dbjc4n.r-14lw9ot.r-1h3ijdo.r-1j3t67a div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1h3ijdo.r-1777fci.r-1jgb5lz.r-sb58tz.r-13qz1uu div.css-1dbjc4n.r-obd0qt.r-1pz39u2.r-1t2qqvi.r-16y2uox.r-1wbh5a2.r-1777fci.r-1joea0r.r-1vsu8ta.r-18qmn74 div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr").click()

    # 11 Termino registrazione Twitter
    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div"))
        )
    except:
        print("Non riesco a saltare immagine profilo....Refresh")
        browser.refresh()

    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath(
        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]").click()
    cookies = browser.get_cookies()

    # 12 Apro link affiliato
    browser.quit()
    profile1 = FirefoxProfile(r'C:\Programmi Portable\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
    user_agent = "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36"
    profile1.set_preference("general.useragent.override", user_agent)
    browser = webdriver.Firefox(firefox_profile=profile1)

    browser.set_window_size(392, 630)
    browser.get("https://mobile.twitter.com")
    for cokki in cookies:
        browser.add_cookie(cokki)
    time.sleep(2)
    browser.get("https://a.aliexpress.com/_mKdYNwf")

    # 13 Clicco su apri e mi loggo come utente twitter
    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[6]"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[6]").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/a"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/a").click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section/div/div[3]/a"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath("/html/body/div/section/div/div[3]/a").click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "allow"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_id("allow").click()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(4)

    try:
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[6]"))
        )
    except:
        print("Non riesco ad andare avanti...Refresh")
        browser.refresh()

    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[6]").click()
