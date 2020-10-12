import os
import psutil
import csv
import json
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
        # for site in sites:
        #     driver.get(site)
        driver.get("https://www.google.com")
        driver.find_element_by_name("q").send_keys("test")
        driver.find_elements_by_name("btnK")[1].click()
        # driver.quit()

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
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
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
        # for site in sites:
        #     driver.get(site)
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[3])
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
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
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site)
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
        driver.get("https://www.yahoo.com") 
        driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site
# TODO get the rest of the extensions 

def getStats():
    f = open('MQP.csv', 'r')
    q = open('newMQP.csv', 'w')
    lines = f.readlines()
    for line in lines:
        if("Tunnel to" not in line):
            q.write(line)
    q.close()
    with open('ghostery_json.json') as r:
        trackingList = json.loads(r.read())
    with open('newMQP.csv') as j:
        reader = csv.DictReader(j)
        for row in reader:
            print(row['Host'])
    for things in trackingList:
        for items in trackingList[things]:
            if("Link" in items):
                print(items)
                print(things)
    
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
                        
# __main__(["f", 8])
# __main__(["e", 1])
# __main__(["f", 3,4])
getStats()
