import os
import psutil
import csv
import json
import numpy as np
from selenium import webdriver
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
    print("Starting process: " + str(os.getpid()))
    sites = openTopSites()
    if("c" in input):
        from selenium.webdriver.chrome.options import Options
        opts = Options()
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
        driver = webdriver.Chrome(options=opts)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        for site in sites:
            driver.get(site)
        # driver.get("https://www.google.com")
        # driver.find_element_by_name("q").send_keys("test")
        # driver.find_elements_by_name("btnK")[1].click()
        driver.quit()

    elif("f" in input):
        driver = webdriver.Firefox()
        if(1 in input):
            driver.install_addon(absPath + "adblock.xpi")
        if(2 in input):
             driver.install_addon(absPath + "adblockPlus.xpi")
        if(3 in input):
            driver.install_addon(absPath + "disconnect.xpi")
        if(4 in input):
             driver.install_addon(absPath + "duckduckgoEss.xpi")
        if(5 in input):
             driver.install_addon(absPath + "ghostery.xpi")
        if(6 in input):
             driver.install_addon(absPath + "privBadger.xpi")
        if(7 in input):
             driver.install_addon(absPath + "ublock.xpi")
        if(8 in input):
             driver.install_addon(absPath + "adGuard.xpi")
        if(9 in input):
             driver.install_addon(absPath + "noScript.xpi")
        if(10 in input):
             driver.install_addon(absPath + "httpsEverywhere.xpi")
        if(11 in input):
             driver.install_addon(absPath + "uBlockOrigin.xpi")
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[1])
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site)        
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
        driverPath = 'chromedriver.exe'
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
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site) 
        driver.quit()

def getStats():
    count = 0 
    domainTrackers = ['adv', 'siteAna', 'custInt', 'social', 'ess', 'audio', 'adultAdv', 'comments']
    itemsArr = []
    domains = []
    domTypes = []
    currList = []
    returnList = []
    # f = open('braveTest.csv', 'r')
    # q = open('newBraveTest.csv', 'w')
    # lines = f.readlines()
    # for line in lines:
    #     if("Tunnel to" not in line):
    #         q.write(line)
    # q.close()
    with open('ghostery_json.json') as r:
        trackingList = json.loads(r.read())
    with open('newChromeTest.csv') as j:
        reader = csv.DictReader(j)
        for row in reader:
            if(row['Privacy Info'] != ""):
                # print(os.system('whois ' + row['Host'] + ' | findstr "%Domain Name:"'))
                # print('whois ' + row['Host'] + ' | findstr "%Domain Name:"')
                domains.append(row['Host'].split(".")[-2])
    for keys in list(dict.fromkeys(domains)):
        returnList.append(keys)
    for doms in returnList:
        for cats in domainTrackers:
            for items in trackingList[cats]:
                if(doms in items.replace(" ", "").lower()):
                    print(doms, cats)
                    break
                

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
                        
# __main__(["f"])
# __main__(["e"])
# __main__(["c"])
# __main__(["o"])
# __main__(["b"])

getStats()

# Stats description - 
# Brave - 6999, 3470
# Chrome - 13277, 6558
# Edge - 11192, 5492
# FireFox - 12052, 5857
# Opera - 14720, 7292

# cookies - 
# Brave - 406
# Chrome - 1775
# Edge - 1261
# FireFox - 1415
# Opera - 1834