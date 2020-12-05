import os
import psutil
import csv
import json
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *


# variables
serverProxy = "https://127.0.0.1:8888"
proxyInit = Proxy({
    'https': serverProxy
})
absPath = "C:\\Users\\Owner\\Desktop\\Webdriver\\"
topSites = "topSites.txt"

# read topSites
def openTopSites():
    file = open(topSites, 'r')
    lines = file.readlines()
    build = []
    for line in lines:
        if(line != lines[-1]):
            build.append(line[:-1])
        else:
            build.append(line)
    return build

# main driving function
def __main__(input):
    sites = openTopSites()
    if("c" in input):
        from selenium.webdriver.chrome.options import Options
        opts = Options()
        if(1 in input):
            opts.add_extension("Extensions\\Chrome\\adblock.crx")
        if(2 in input):
            opts.add_extension("Extensions\\Chrome\\adblockPlus.crx")
        if(3 in input):
            opts.add_extension("Extensions\\Chrome\\adGuard.crx")
        if(4 in input):
            opts.add_extension("disconnect.crx")
        if(5 in input):
            opts.add_extension("Extensions\\Chrome\\duckduckgoEss.crx")
        if(6 in input):
            opts.add_extension("Extensions\\Chrome\\ghostery.crx")
        if(7 in input):
            opts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            opts.add_extension("Extensions\\Chrome\\myTrackingChoices.crx")
        if(9 in input):
            opts.add_extension("Extensions\\Chrome\\noScript.crx")
        if(10 in input):
            opts.add_extension("Extensions\\Chrome\\privBadger.crx")
        if(11 in input):
            opts.add_extension("ublock.crx")  
        if(12 in input):
            opts.add_extension("Extensions\\Chrome\\uBlockOrigin.crx")   
        if(13 in input):
            opts.add_extension("blur.crx") 
        driver = webdriver.Chrome(options=opts)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        for site in sites:
            driver.get(site)
            time.sleep(5)
            driver.save_screenshot("BreakageImages/" + "Chrome" + str(input[1]) + site.split(".")[1] + ".png")
        # driver.get("https://www.foxnews.com")
        # driver.get("https://www.cbs.com/shows/all-rise/video/HWypMj8VYUT5NPsNTzhiZIfSI_VX2ySe/all-rise-keep-ya-head-up/")
        # driver.save_screenshot("BreakageImages/test.jpg")
        # login test
        # driver.get("https://login.microsoftonline.com/589c76f5-ca15-41f9-884b-55ec15a0672a/saml2?SAMLRequest=fZJBb9swDIXv%2BxWG7rItz3JsIQmQJRgWoN2CJtthl0GR6UaALbmi1K7%2FfordYe1hvVJ8%2FPgetUQ59KPYBH8xd%2FAQAH3ye%2BgNiulhRYIzwkrUKIwcAIVX4ri5vRFFmovRWW%2BV7ckryfsKiQjOa2tIst%2BtyK8FqzmrCk6bRjW0zJuanlt%2Bph%2BhKhdFqaqSK5L8AIdRsyJxRBQiBtgb9NL4WMqLnDJGi%2FLEuOCF4OwnSXbRhzbST6qL9yOKLOvtvTbpoJWzaDtvTa8NpMoOGa8btag6TpVknJasa2hdl2fKOSjGZV4tCpld3RUk2fy1sLUGwwDuCO5RK%2Fh%2Bd%2FMPpaR5lJg%2BjTqFNszkaQBJDi%2BhfdKm1eb%2B%2FbzOcxOKL6fTgR6%2BHU9kvbzOEVMKbn0FRt4VpGMkLigf3Gxq2neZve5eztf%2BGjn73cH2Wj0nn60bpP%2F%2FGixlU0W3tJtaRTA4gtKdhjbG0ff2aetAeliRyAeSrWfo21%2B1%2FvAH&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=qlUPznFbYqWTA5yQAy4uPO3O%2F39cWkG6Sn9pS8CBmBH3VJMf2JmOwFgft6hYHywGJ%2FJUKdJ47Bl4gin1yU6z0Jp%2B5Lb70TMxihDvKXSe%2BKipNbD03HRTMEE%2FhDHQy2gl7Jy05eqiNAZzKTqhR9Y%2FetJD5MYygKYqvRlZdqJQL38nhOXnAQRrYZM5iwa5E4FPxtZOVjSKOcTMC9tJzBInfhPDrxfPwvKPKTHfHWafCunGZzdOrCRCy0cjiC83Ldrtqub9MYgb%2FeuR4Vkjww1ge0iE1H08WlckmXLMFIX95ywNkGcUiyVDsCi7zuuS3tEDWykNPUE7TO3vSe%2B6F1bsZA%3D%3D&sso_reload=true")
        # driver.implicitly_wait(10)
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
        # driver.find_element_by_id("i0116").send_keys("jharnois@wpi.edu")
        # driver.find_element_by_id('idSIButton9').click()
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'i0118')))
        # test = os.getenv("Testpass")
        # driver.implicitly_wait(10)
        # driver.find_element_by_id('i0118').send_keys(test)
        # driver.implicitly_wait(10)
        # time.sleep(3)
        # driver.find_element_by_id('idSIButton9').click()
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'ic-DashboardCard')))
        # driver.get("https://canvas.wpi.edu/courses/22560/external_tools/1771")
        # time.sleep(3)
        # firstFrame = driver.find_element_by_id('tool_content')
        # driver.switch_to.frame(firstFrame)
        # print(driver.find_element_by_tag_name("button"))
        # .contentWindow.frames
        # driver.start("test")
        # test = driver.find_element_by_class_name("fc-dialog-container")
        # driver.find_element_by_class_name("fc-dialog-container").send_keys("test")
        # driver.find_elements_by_name("btnK")[1].click()
        driver.quit()

    elif("f" in input):
        driver = webdriver.Firefox()
        if(1 in input):
            driver.install_addon(absPath + "Extensions\\Firefox\\adblock.xpi")
        if(2 in input):
             driver.install_addon(absPath + "adblockPlus.xpi")
        if(3 in input):
            driver.install_addon(absPath + "disconnect.xpi")
        if(4 in input):
             driver.install_addon(absPath + "duckduckgoEss.xpi")
        if(5 in input):
             driver.install_addon(absPath + "Extensions\\Firefox\\ghostery.xpi")
        if(6 in input):
             driver.install_addon(absPath + "Extensions\\Firefox\\privBadger.xpi")
        if(7 in input):
             driver.install_addon(absPath + "ublock.xpi")
        if(8 in input):
             driver.install_addon(absPath + "adGuard.xpi")
        if(9 in input):
             driver.install_addon(absPath + "Extensions\\Firefox\\noScript.xpi")
        if(10 in input):
             driver.install_addon(absPath + "httpsEverywhere.xpi")
        if(11 in input):
             driver.install_addon(absPath + "Extensions\\Firefox\\uBlockOrigin.xpi")
        if(12 in input):
            driver.install_addon(absPath + "Extensions\\Firefox\\blur.xpi")
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[1])
        # driver.get("https://www.cnn.com/audio/podcasts/corona-virus?episodeguid=e044092c-7766-49cf-9e71-ac84017a61d4")
        # time.sleep(3)
        # driver.find_element_by_id("play-button-circle-0").click()
        # time.sleep(8)
        # driver.save_screenshot("BreakageImages/test.png")
        # driver.get("https://www.washingtonpost.com/news/federal-eye/wp/2014/09/04/reporters-deaths-point-to-dangers-of-working-in-hotspots-abroad/?arc404=true")
        # driver.save_screenshot("BreakageImages/test2.png")
        # driver.get("https://www.cbs.com/shows/all-rise/video/HWypMj8VYUT5NPsNTzhiZIfSI_VX2ySe/all-rise-keep-ya-head-up/")
        # time.sleep(15)
        # driver.save_screenshot("BreakageImages/test3.png")
        # driver.get("https://login.microsoftonline.com/589c76f5-ca15-41f9-884b-55ec15a0672a/saml2?SAMLRequest=fZJBb9swDIXv%2BxWG7rItz3JsIQmQJRgWoN2CJtthl0GR6UaALbmi1K7%2FfordYe1hvVJ8%2FPgetUQ59KPYBH8xd%2FAQAH3ye%2BgNiulhRYIzwkrUKIwcAIVX4ri5vRFFmovRWW%2BV7ckryfsKiQjOa2tIst%2BtyK8FqzmrCk6bRjW0zJuanlt%2Bph%2BhKhdFqaqSK5L8AIdRsyJxRBQiBtgb9NL4WMqLnDJGi%2FLEuOCF4OwnSXbRhzbST6qL9yOKLOvtvTbpoJWzaDtvTa8NpMoOGa8btag6TpVknJasa2hdl2fKOSjGZV4tCpld3RUk2fy1sLUGwwDuCO5RK%2Fh%2Bd%2FMPpaR5lJg%2BjTqFNszkaQBJDi%2BhfdKm1eb%2B%2FbzOcxOKL6fTgR6%2BHU9kvbzOEVMKbn0FRt4VpGMkLigf3Gxq2neZve5eztf%2BGjn73cH2Wj0nn60bpP%2F%2FGixlU0W3tJtaRTA4gtKdhjbG0ff2aetAeliRyAeSrWfo21%2B1%2FvAH&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=qlUPznFbYqWTA5yQAy4uPO3O%2F39cWkG6Sn9pS8CBmBH3VJMf2JmOwFgft6hYHywGJ%2FJUKdJ47Bl4gin1yU6z0Jp%2B5Lb70TMxihDvKXSe%2BKipNbD03HRTMEE%2FhDHQy2gl7Jy05eqiNAZzKTqhR9Y%2FetJD5MYygKYqvRlZdqJQL38nhOXnAQRrYZM5iwa5E4FPxtZOVjSKOcTMC9tJzBInfhPDrxfPwvKPKTHfHWafCunGZzdOrCRCy0cjiC83Ldrtqub9MYgb%2FeuR4Vkjww1ge0iE1H08WlckmXLMFIX95ywNkGcUiyVDsCi7zuuS3tEDWykNPUE7TO3vSe%2B6F1bsZA%3D%3D&sso_reload=true")
        # driver.implicitly_wait(10)
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
        # driver.find_element_by_id("i0116").send_keys("jharnois@wpi.edu")
        # driver.find_element_by_id('idSIButton9').click()
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'i0118')))
        # test = os.getenv("Testpass")
        # driver.implicitly_wait(10)
        # driver.find_element_by_id('i0118').send_keys(test)
        # driver.implicitly_wait(10)
        # time.sleep(3)
        # driver.find_element_by_id('idSIButton9').click()
        # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'ic-DashboardCard')))
        # driver.get("https://canvas.wpi.edu/courses/22560/external_tools/1771")
        # time.sleep(3)
        # driver.save_screenshot("BreakageImages/test4.png")
        # driver.get("https://www.twitch.tv/")
        # time.sleep(3)
        # driver.save_screenshot("BreakageImages/test5.png")
        # driver.start("test")
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site)
        #     time.sleep(5)
        #     driver.save_screenshot("BreakageImages/test" + str(input[1]) + site.split(".")[1] + ".png")     
        # for site in sites:
        #     driver.get(site)   
        driver.quit()

    elif("e" in input):
        from msedge.selenium_tools import Edge, EdgeOptions
        # from selenium.webdriver import Edge
        from selenium.webdriver.edge.options import Options
        opts = EdgeOptions()
        opts.use_chromium = True
        if(1 in input):
            opts.add_extension("adblock.crx")
        if(2 in input):
            opts.add_extension("adblockPlus.crx")
        if(3 in input):
            opts.add_extension("adGuard.crx")
        if(4 in input):
            opts.add_extension("disconnect.crx")
        if(5 in input):
            opts.add_extension("duckduckgoEss.crx")
        if(6 in input):
            opts.add_extension("ghostery.crx")
        if(7 in input):
            opts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            opts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            opts.add_extension("noScript.crx")
        if(10 in input):
            opts.add_extension("privBadger.crx")
        if(11 in input):
            opts.add_extension("ublock.crx")  
        if(12 in input):
            opts.add_extension("uBlockOrigin.crx") 
        driver = Edge(options=opts)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        for site in sites:
            driver.get(site)
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        driver.quit()

    elif("o" in input):
        from selenium.webdriver.opera import options
        Oopts = options.ChromeOptions()
        Oopts.use_chromium = True
        if(1 in input):
            Oopts.add_extension("adblock.crx")
        if(2 in input):
            Oopts.add_extension("adblockPlus.crx")
        if(3 in input):
            Oopts.add_extension("adGuard.crx")
        if(4 in input):
            Oopts.add_extension("disconnect.crx")
        if(5 in input):
            Oopts.add_extension("duckduckgoEss.crx")
        if(6 in input):
            Oopts.add_extension("ghostery.crx")
        if(7 in input):
            Oopts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            Oopts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            Oopts.add_extension("noScript.crx")
        if(10 in input):
            Oopts.add_extension("privBadger.crx")
        if(11 in input):
            Oopts.add_extension("ublock.crx")  
        if(12 in input):
            Oopts.add_extension("uBlockOrigin.crx") 
        driver = webdriver.Opera(options=Oopts)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site)
        driver.quit()

    elif("b" in input):
        from selenium.webdriver.chrome.options import Options
        braveOpts = Options()
        bravePath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe'
        braveOpts.binary_location = bravePath
        driverPath = 'CD_87.exe'
        if(1 in input):
            braveOpts.add_extension("adblock.crx")
        if(2 in input):
            braveOpts.add_extension("adblockPlus.crx")
        if(3 in input):
            braveOpts.add_extension("adGuard.crx")
        if(4 in input):
            braveOpts.add_extension("disconnect.crx")
        if(5 in input):
            braveOpts.add_extension("duckduckgoEss.crx")
        if(6 in input):
            braveOpts.add_extension("ghostery.crx")
        if(7 in input):
            braveOpts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            braveOpts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            braveOpts.add_extension("noScript.crx")
        if(10 in input):
            braveOpts.add_extension("privBadger.crx")
        if(11 in input):
            braveOpts.add_extension("ublock.crx")  
        if(12 in input):
            braveOpts.add_extension("uBlockOrigin.crx")   
        driver = webdriver.Chrome(options=braveOpts, executable_path=driverPath)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        print('here')
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site)
            time.sleep(5)
            driver.save_screenshot("BreakageImages/" + "Brave" + site.split(".")[1] + ".png")
        driver.quit()

    elif("v" in input):
        from selenium.webdriver.chrome.options import Options
        vivOpts = Options()
        vivOpts.add_argument('--no-sandbox')
        vivOpts.add_argument('--disable-web-security')
        vivPath = 'C:\\Users\\Owner\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe'
        vivOpts.binary_location = vivPath
        driverPath = 'chromedriver.exe'
        if(1 in input):
            vivOpts.add_extension("adblock.crx")
        # if(2 in input):
        #     vivOpts.add_extension("adblockPlus.crx")
        # if(3 in input):
        #     vivOpts.add_extension("adGuard.crx")
        # if(4 in input):
        #     vivOpts.add_extension("disconnect.crx")
        # if(5 in input):
        #     vivOpts.add_extension("duckduckgoEss.crx")
        # if(6 in input):
        #     vivOpts.add_extension("ghostery.crx")
        # if(7 in input):
        #     vivOpts.add_extension("httpsEverywhere.crx")
        # if(8 in input):
        #     vivOpts.add_extension("myTrackingChoices.crx")
        # if(9 in input):
        #     vivOpts.add_extension("noScript.crx")
        # if(10 in input):
        #     vivOpts.add_extension("privBadger.crx")
        # if(11 in input):
        #     vivOpts.add_extension("ublock.crx")  
        # if(12 in input):
        #     vivOpts.add_extension("uBlockOrigin.crx")   
        print('here')
        driver = webdriver.Chrome(options=vivOpts, executable_path=driverPath)
        print('here')
        # p = psutil.Process(driver.service.process.pid)
        # print(p.children(recursive=True))
        print('here')
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site) 
        driver.quit()

    elif("i" in input):
        from selenium.webdriver.chrome.options import Options
        iriOpts = Options()
        iriPath = 'C:\\Program Files\\Iridium\\iridium.exe'
        iriOpts.binary_location = iriPath
        driverPath = 'CD_80.exe'
        if(1 in input):
            iriOpts.add_extension("adblock.crx")
        # if(2 in input):
        #     iriOpts.add_extension("adblockPlus.crx")
        # if(3 in input):
        #     iriOpts.add_extension("adGuard.crx")
        # if(4 in input):
        #     iriOpts.add_extension("disconnect.crx")
        # if(5 in input):
        #     iriOpts.add_extension("duckduckgoEss.crx")
        # if(6 in input):
        #     iriOpts.add_extension("ghostery.crx")
        # if(7 in input):
        #     iriOpts.add_extension("httpsEverywhere.crx")
        # if(8 in input):
        #     iriOpts.add_extension("myTrackingChoices.crx")
        # if(9 in input):
        #     iriOpts.add_extension("noScript.crx")
        # if(10 in input):
        #     iriOpts.add_extension("privBadger.crx")
        # if(11 in input):
        #     iriOpts.add_extension("ublock.crx")  
        # if(12 in input):
        #     iriOpts.add_extension("uBlockOrigin.crx")   
        driver = webdriver.Chrome(options=iriOpts, executable_path=driverPath)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site) 
        driver.quit()

    elif("u" in input):
        from selenium.webdriver.chrome.options import Options
        unOpts = Options()
        unPath = 'C:\\Users\\Owner\\AppData\\Local\\Chromium\\Application\\chrome.exe'
        unOpts.binary_location = unPath
        driverPath = 'chromedriver.exe'
        if(1 in input):
            unOpts.add_extension("adblock.crx")
        if(2 in input):
            unOpts.add_extension("adblockPlus.crx")
        if(3 in input):
            unOpts.add_extension("adGuard.crx")
        if(4 in input):
            unOpts.add_extension("disconnect.crx")
        if(5 in input):
            unOpts.add_extension("duckduckgoEss.crx")
        if(6 in input):
            unOpts.add_extension("ghostery.crx")
        if(7 in input):
            unOpts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            unOpts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            unOpts.add_extension("noScript.crx")
        if(10 in input):
            unOpts.add_extension("privBadger.crx")
        if(11 in input):
            unOpts.add_extension("ublock.crx")  
        if(12 in input):
            unOpts.add_extension("uBlockOrigin.crx")   
        driver = webdriver.Chrome(options=unOpts, executable_path=driverPath)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site) 
        driver.quit()

    elif("p" in input):
        from selenium.webdriver.chrome.options import Options
        epicOpts = Options()
        epicPath = 'C:\\Users\\Owner\\AppData\\Local\\Epic Privacy Browser\\Application\\epic.exe'
        epicOpts.binary_location = epicPath
        driverPath = 'CD_84.exe'
        if(1 in input):
            epicOpts.add_extension("adblock.crx")
        if(2 in input):
            epicOpts.add_extension("adblockPlus.crx")
        if(3 in input):
            epicOpts.add_extension("adGuard.crx")
        if(4 in input):
            epicOpts.add_extension("disconnect.crx")
        if(5 in input):
            epicOpts.add_extension("duckduckgoEss.crx")
        if(6 in input):
            epicOpts.add_extension("ghostery.crx")
        if(7 in input):
            epicOpts.add_extension("httpsEverywhere.crx")
        if(8 in input):
            epicOpts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            epicOpts.add_extension("noScript.crx")
        if(10 in input):
            epicOpts.add_extension("privBadger.crx")
        if(11 in input):
            epicOpts.add_extension("ublock.crx")  
        if(12 in input):
            epicOpts.add_extension("uBlockOrigin.crx")   
        driver = webdriver.Chrome(options=epicOpts, executable_path=driverPath)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site) 
        driver.quit()

def helper(start, domains, dumbArrOne):
    with open('CSVs/BrowsersExtensions/Firefox_ublockOrigin.csv', 'r') as r:
        with open('topSites.txt', 'r') as f:
            reader = csv.reader(r)
            count = 0
            for row in reader:
                lineBuild = []
                lineBuild.append(row[0])
                lineBuild.append(row[3])
                lineBuild.append(row[4])
                if(lineBuild[2] == '/' and lineBuild[1] in domains):
                    count = count + 1 
                if(lineBuild[2] != '/' and lineBuild[0] != '#'):
                    if(int(lineBuild[0]) > int(start)):
                        dumbArrOne[count - 1].append(lineBuild)
            return(dumbArrOne)

def getStats():
    count = 0 
    start = 0
    domainTrackers = ['Advertising', 'Site Analytics', 'Customer Interaction', 'Social', 'Essential', 'Audio/Video Player', 'Adult Advertising', 'Comments', 'First Party', 'Extension', 'Unknown']
    domainNumbers = [0,0,0,0,0,0,0,0,0,0,0]
    interactions = ['html', 'gif', 'css', 'png', 'plain', 'json', 'jpeg', 'javascript', 'webm', 'x-mpegURL', 'webp', 'octet-stream', 'x-m4v' ,'binary', 'x-javascript', 'xml', 'svg+xml', 'mp4', 'js', 'x-icon', 'MP2T', 'wasm']
    interactionsTracking = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    itemsArr = []
    domains = []
    domTypes = []
    currList = []
    returnList = []
    test = []
    dummy = []
    catList = []
    domainArr = ['']
    domainArrCount = [0]
    dumbArrOne = []

    # Lol I dont know what this is but 
    with open('FinalUniqueDomains.txt', 'r') as r:
        with open('Domains_per_site/Firefox_ublockOrigin.txt', 'w') as t:
            lines = r.readlines()
            # For each host that we have 
            for line in lines:
                line = line.split('\n')[0]
                domainArr[0] = line
                # Starting here maybe lol idk
                with open('CSVs/BrowsersExtensions/Firefox_ublockOrigin.csv', 'r') as r:
                    with open('topSites.txt', 'r') as f:
                        reader = csv.reader(r)
                        readerTwo = csv.reader(r)
                        siteLines = f.readlines()
                        for site in siteLines:
                            domains.append(site.split('\n')[0].split('//')[1].lower())
                        for lines in reader:
                            lineBuild = []
                            lineBuild.append(lines[0])
                            lineBuild.append(lines[3])
                            lineBuild.append(lines[4])
                            if(lineBuild[2] == '/' and 'www.google.com' in lines[3]):
                                start = lineBuild[0]
                            if(lineBuild[2] == '/' and lineBuild[1] in domains):
                                count = count + 1
                                arrInside = []
                                dumbArrOne.append(arrInside)
                    f.close()
                r.close()
                bigAssArr = helper(start, domains, dumbArrOne)
                #count by
                for i in range(len(bigAssArr)): 
                    #see if domainArr is inside 
                    for j in range(len(bigAssArr[i])): 
                        if((bigAssArr[i][j][1].split('.')[-2]+ '.' + bigAssArr[i][j][1].split('.')[-1]) in domainArr):
                            index = domainArr.index((bigAssArr[i][j][1].split('.')[-2]+ '.' + bigAssArr[i][j][1].split('.')[-1]))
                            domainArrCount[index] = domainArrCount[index] + 1                            
                            break
                t.write(str(domainArrCount[0]) + '\n')
                domainArrCount[0] = 0
                dumbArrOne = []
    

    # Real stats 
    # TODO: add counter to see if it returns all false for extra testing in the future to account for the falses in the for loops - for unknowns, not in database
    # r = open('CSVs/manualDatabase.csv', 'r')
    # t = open('CSVs/Browsers/Chrome_Vanilla.csv', 'r')
    # readerTwo = csv.reader(r)
    # reader = csv.reader(t)
    # #remove duplicates based on full host
    # for row in reader:
    #     if(row[11] != "" or row[11] == ""): # for cookies
    #         if(row[3] != 'Host'):
    #             if(row[3] not in dummy):
    #                 dummy.append(row[3])
    # for line in readerTwo:
    #     if(line[1] != 'Full Host with Comma'):
    #         test.append([line[1].split(".")[-2] + "." + line[1].split(".")[-1], line[2]])
    # for one in test:
    #     for two in dummy:
    #         if(two.split(".")[-2] + "." + two.split(".")[-1] == one[0]):
    #             # if(one[1] == "Extension"):
    #             #     print(two, one[0])
    #             # print(two, one[0])
    #             domainNumbers[domainTrackers.index(one[1])] = domainNumbers[domainTrackers.index(one[1])] + 1
    #             break
    # print(domainNumbers)
           
            # if(row[3] == line[1]):
            #     print(row, line)
    #     test.append(row[3])
    # print(test)
    # for lines in readerTwo:
    #     dummy.append(lines['Full Host with Comma'])
    # for things in test:
    #     for moreThings in dummy:
    #         if(things == moreThings):
    #             catList.append(things)
    # for hosts in catList:

                # for row in readerTwo:
                #     print(row['Full Host with Comma'], things)
                    # if(row['Full Host with Comma'] == things):
                    #     print(row['Category'])
            
            # print(lines['Full Host with Comma'] , "...In Database")
        #     if(lines['Full Host with Comma'] != row['Host']):
        #         # print(row['Host'], lines['Full Host with Comma'])

                

    # r = open("finalHosts.txt", "w")
    # with open('FinalDatabase.txt', 'r') as f:
    #     lines = f.readlines()
    #     join = ""
    #     count = 0
    #     for line in lines:
    #         line = line.split('\n')[0]
    #         print(line)
    #         join = join + line.split('\n')[0].split(".")[-2]
    #         join = join + '.' + line.split('\n')[0].split(".")[-1]
    #         count = count + 1
    #         print(count)
    #         print(join)
    #         r.write(join + '\n')
    #         join = ""
    #     print(lines)

    # For elimination of tunneling    
    
    # f = open('CSVs\\banana.csv', 'r')
    # q = open('CSVs\\trackingChoicesTrained.csv', 'w+')
    # reader = csv.DictReader(f)
    # # for lines in reader:
    # #     if(lines['Short Host'] not in q):
    # #         q.write(lines['Short Host'] + '\n')
    # lines = f.readlines()
    # for line in lines:
    #     if("Tunnel to" not in line):
    #         q.write(line)
    # q.close()
    # with open('ghostery_json.json') as r:
    #     trackingList = json.loads(r.read())
    # with open('newBraveTest.csv') as j:
        # reader = csv.DictReader(j)
    #     for row in reader:
            #For number of requests and narrowing down their domains
            # if(row['Privacy Info'] != ""):
                # count = count + 1 
                # loopVar = os.system('whois ' + row['Host'] + ' | findstr /C:"Domain Name:"')
                # if(not loopVar):
                #     print(loopVar)
                # else:
                #     print(os.system('whois ' + row['Host'] + ' | findstr "Domain Name:"'))
                # print('whois ' + row['Host'] + ' | findstr /C:"Domain Name:"')
                # domains.append(row['Host'].split(".")[-2]) #<---------------
                # test.append(row['Host'].split(".")[-1])
                # if(len(row['Host'].split(".")) > 2):
                #     dummy.append(row['Host'].split(".")[-3])
                # print(row['Host'])
                # if(row['Host'] not in domains):
                #     domains.append(row['Host'])
    #         if(row['Host'] not in domains):
    #             domains.append(row['Host'])
    # print(domains)
    # print(len(domains))

                # For Content Type 
                # if(row['Content-Type']):
                #     if(";" in row['Content-Type'].split("/")[1]):
                #         if(row['Content-Type'].split("/")[1].split(";")[0] in interactions):
                #             # print(interactions.index(row['Content-Type'].split("/")[1].split(";")[0]))
                #             interactionsTracking[interactions.index(row['Content-Type'].split("/")[1].split(";")[0])] = interactionsTracking[interactions.index(row['Content-Type'].split("/")[1].split(";")[0])] + 1
                #     else:
                #         if(row['Content-Type'].split("/")[1] in interactions):
                #             # print(interactions.index(row['Content-Type'].split("/")[1]))
                #             interactionsTracking[interactions.index(row['Content-Type'].split("/")[1])] = interactionsTracking[interactions.index(row['Content-Type'].split("/")[1])] + 1
                # print(interactionsTracking)
    # print(count)

    # for i in test:
    #     for j in domains:
    #         for k in trackingList:
    #             for l in dummy:
    #                 if(j in k):
    #                     # print(j, i)
    #                     print(l)

    # For getting the categories of the domains found from each browser; uncomment the arrow!
    # for keys in list(dict.fromkeys(read)):
    #     returnList.append(keys)
    # print(returnList)
    # for doms in returnList:
    #     for cats in domainTrackers:
    #         for items in trackingList[cats]:
    #             if(doms not in test):
    #                 if(doms in items.replace(" ", "").lower()):
    #                     # print(doms, cats)
    #                     domainNumbers[domainTrackers.index(cats)] = domainNumbers[domainTrackers.index(cats)] + 1
    # print(domainNumbers)    

    #     for items in trackingList[things]:
        
    # for doms in domains:
    #     print(domains)
        # if(domains[doms] in (items.replace(" ", "")).lower()):
        #     print((items.replace(" ", "")).lower())
        #     print(things)
    # print(itemsArr)
    
    # with open('trackingList.json') as r:
    #     trackingLists = json.loads(r.read())
    # with open('newMQP.csv') as j:
    #     reader = csv.DictReader(j)
    #     for things in trackingLists['categories']:
    #         for moreThings in trackingLists['categories'][things]:
    #             print(moreThings)
    #             for row in reader:
    #                 part = str(row['Host'].split('.')[-2])
    #         #     if(part in things):
            #         print(things)
                        
# __main__(["f", 1])
# __main__(["e", 1])
# __main__(["f", 2])
# __main__(["c", 5])
# __main__(["f", 4])
# __main__(["f", 5])
# __main__(["f", 6])
# __main__(["f", 7])#////////////////////////////////////<- fix
# __main__(["f", 8])
# __main__(["f", 9])
# __main__(["f", 10])
# __main__(["f", 11])
# __main__(["f", 12])


# __main__(["u"])
# __main__(["p"])
# __main__(["c", 13])
# __main__(["c", 9])
__main__(["b"])
# __main__(["c", 8])
# getStats()

#AdBlock +
#ublockOrigin
#Ghostery
#privBad
#noScript
#brave


# NoScript
# Youtube - 2
# Reddit - 1
# Amazon - 2
# Zoom - 1
# Shopify login - 2
# Ebay login - 2
# 
# 
# 
# 

# AdBlock
# CNN - 2
# Office - 2
# Fox News - 1
# 