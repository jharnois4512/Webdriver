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
    sites = openTopSites()
    if("c" in input):
        from selenium.webdriver.chrome.options import Options
        opts = Options()
        if(1 in input):
            opts.add_extension("Extensions\\Chrome\\adblock.crx")
        if(2 in input):
            opts.add_extension("adblockPlus.crx")
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
            opts.add_extension("myTrackingChoices.crx")
        if(9 in input):
            opts.add_extension("Extensions\\Chrome\\noScript.crx")
        if(10 in input):
            opts.add_extension("privBadger.crx")
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
        # for site in sites:
        #     driver.get(site)
        driver.start("https://www.google.com")
        # driver.find_element_by_name("q").send_keys("test")
        # driver.find_elements_by_name("btnK")[1].click()
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
             driver.install_addon(absPath + "Extensions\\Firefox\\uBlockOrigin.xpi")
        if(12 in input):
            driver.install_addon(absPath + "Extensions\\Firefox\\blur.xpi")
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        p = psutil.Process(driver.service.process.pid)
        print(p.children(recursive=True)[1])
        driver.start()
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        # for site in sites:
        #     driver.get(site)        
        # driver.quit()

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
        print('here')
        # driver.get("https://www.yahoo.com") 
        # driver.get("https://www.cnn.com")
        for site in sites:
            driver.get(site) 
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
    with open('CSVs/BrowsersExtensions/Firefox_AdBlockPlus.csv', 'r') as r:
        with open('topSites.txt', 'r') as f:
            reader = csv.reader(r)
            count = 0
            for row in reader:
                if(row[4] == '/' and row[3] in domains):
                    count = count + 1 
                if(row[4] != '/'):
                    if(row[0] > start):
                        dumbArrOne[count - 1].append(row)
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
        with open('How many times does x show up/Firefox_AdBlockPlusNew.txt', 'w') as t:
            lines = r.readlines()
            # For each host that we have 
            for line in lines:
                line = line.split('\n')[0]
                domainArr[0] = line
                # Starting here maybe lol idk
                with open('CSVs/BrowsersExtensions/Firefox_AdBlockPlus.csv', 'r') as r:
                    with open('topSites.txt', 'r') as f:
                        reader = csv.reader(r)
                        readerTwo = csv.reader(r)
                        siteLines = f.readlines()
                        for site in siteLines:
                            domains.append(site.split('\n')[0].split('//')[1].lower())
                        for lines in reader:
                            # print(siteLines)
                            if(lines[4] == '/' and 'www.google.com' in lines[3]):
                                start = lines[0]
                            if(lines[4] == '/' and lines[3] in domains):
                                count = count + 1
                                arrInside = []
                                dumbArrOne.append(arrInside)
                    f.close()
                r.close()
                # print(dumbArrOne)
                bigAssArr = helper(start, domains, dumbArrOne)
                #count by
                for i in range(len(bigAssArr)):   
                    #see if domainArr is inside 
                    for j in range(len(bigAssArr[i])):
                        if((bigAssArr[i][j][3].split('.')[-2]+ '.' + bigAssArr[i][j][3].split('.')[-1]) in domainArr):
                            index = domainArr.index((bigAssArr[i][j][3].split('.')[-2]+ '.' + bigAssArr[i][j][3].split('.')[-1]))
                            domainArrCount[index] = domainArrCount[index] + 1                            
                            break
                # print(line)
                # print(domainArrCount)
                # print(str(domainArrCount[0]))
                t.write(str(domainArrCount[0]) + '\n')
                domainArrCount[0] = 0
    

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
    
    # f = open('CSVs\Firefox_ublockOrigin_Manual.csv', 'r')
    # q = open('CSVs\BrowsersExtensions\Firefox_ublockOrigin.csv', 'w+')
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
# __main__(["f", 12])
# __main__(["c", 12])
getStats()

######## Stats description - 
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

# Number of Categories - Needs more work
# Brave - [76, 17, 23, 14, 7, 1, 1, 2]
# Chrome - [304, 37, 39, 20, 17, 8, 4, 2]
# Edge - [285, 36, 39, 20, 16, 8, 4, 2]
# Firefox - [285, 33, 29, 20, 16, 8, 3, 2]
# Opera - [303, 38, 38, 20, 17, 8, 4, 2]


######## With AdBlock
# Brave - 5536, 2728
# Chrome - 9782, 4829
# Edge - 9892, 4852
# Firefox - 8620, 4255
# Opera - 7673, 3788

# cookies - 
# Brave - 457
# Chrome - 975
# Edge - 916
# Firefox - 830
# Opera - 688

# - unique third-party domains from which at least object is retrieved
# - unique third-party domains that set at least one cookie in the browser
# - each of these can also be reported based upon the categories

# Number of unique domains that set a cookie
# Brave
# ['www.google.com', 'www.youtube.com', 'adservice.google.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'www.amazon.com', 'assoc-na.associates-amazon.com', 'www.yahoo.com', 's.amazon-adsystem.com', 'udc.yahoo.com', 'geo.yahoo.com', 'video.adaptv.advertising.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'www.facebook.com', 'www.zoom.us', 'www.reddit.com', 'www.wikipedia.org', 'www.ebay.com', 'ir.ebaystatic.com', 'www.office.com', 'ocsrest.ebay.com', 'login.live.com', 'login.microsoftonline.com', 'www.netflix.com', 'www.bing.com', 'outlook.live.com', 'www.instructure.com', 'pages.instructure.com', 'www.twitch.tv', 'www.microsoft.com', 'www.chaturbate.com', 'chaturbate.com', 'www.instagram.com', 'www.cnn.com', 'cdn.cookielaw.org', 'www.espn.com', 'tredir.espn.com', 'sp.auth.adobe.com', 'www.zillow.com', 'www.chase.com', 'midas.chase.com', 'sites.chase.com', 'www.etsy.com', 'www.linkedin.com', 'www.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', 'www.adobe.com', 'adobeid-na1.services.adobe.com', 'geolocation.onetrust.com', 'www.nytimes.com', 'www.aliexpress.com', 'login.aliexpress.ru', 'cdp.aliexpress.com', 'login.tmall.ru', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'us.ynuf.aliapp.org', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'www.walmart.com', 'cf-us.wal.co', 'www.twitter.com', 'fa-us-dyn.wal.co', 'zy-us-dyn.wal.co', 'cf-us-dyn.wal.co', 'i5-opt-v1.wal.co', 'i5-opt-pulsar.wal.co', 'ak-us-dyn.wal.co', 'i5-opt-v0.wal.co', 'twitter.com', 'www.livejasmin.com', 'www.wellsfargo.com', 'connect.secure.wellsfargo.com', 'ws.mmstat.com', 'imgur.com', 'www.salesforce.com', 'www.homedepot.com', 'optimizely-edge.salesforce.com', 'www.imdb.com', 'www.hulu.com', 'www.pornhub.com', 'www.msn.com', 'www.indeed.com', 'www.foxnews.com', 'omny.fm', 'assets.omny.fm', 'dpm.demdex.net', 'contributor.google.com', 'feeds-elections.foxnews.com', 'my.foxnews.com']
# 96
# Chrome
# ['www.google.com', 'www.youtube.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'www.amazon.com', 'assoc-na.associates-amazon.com', 's.amazon-adsystem.com', 'www.yahoo.com', 'udc.yahoo.com', 'ads.yahoo.com', 'cms.analytics.yahoo.com', 'ups.analytics.yahoo.com', 'service.idsync.analytics.yahoo.com', 'pr-bh.ybp.yahoo.com', 'geo.yahoo.com', 'www.facebook.com', 'dpm.demdex.net', 'pixel.advertising.com', 'tags.bluekai.com', 'b.gemini.yahoo.com', 'cx.atdmt.com', 'www.zoom.us', 'www.reddit.com', 'c.aaxads.com', 'id.rlcdn.com', 'www.wikipedia.org', 'pixel.quantserve.com', 'www.ebay.com', 'rover.ebay.com', 'www.office.com', 'ocsrest.ebay.com', 'svcs.ebay.com', 'pulsar.ebay.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'www.netflix.com', 'c1.microsoft.com', 'c.bing.com', 'www.bing.com', 'outlook.live.com', 'www.instructure.com', 'pages.instructure.com', 'bat.bing.com', 'settings.luckyorange.net', 'px.ads.linkedin.com', 'www.linkedin.com', 'p.adsymptotic.com', 'www.twitch.tv', 'analytics.twitter.com', 'bam.nr-data.net', 'www.microsoft.com', 'app.link', 'www.chaturbate.com', 'mscom.demdex.net', 'cm.everesttech.net', 'sync.mathtag.com', 'ib.adnxs.com', 'idsync.rlcdn.com', 'idpix.media6degrees.com', 'a.tribalfusion.com', 'px.owneriq.net', 'servedby.flashtalking.com', 'p.rfihub.com', 'rtd-tm.everesttech.net', 'match.adsrvr.org', 'jadserve.postrelease.com', 'bttrack.com', 'rtb.adentifi.com', 'dmpsync.3lift.com', 'ds.reson8.com', 'sync.crwdcntrl.net', 'dsum-sec.casalemedia.com', 'pixel.rubiconproject.com', 'us-u.openx.net', 'chaturbate.com', 'sync.search.spotxchange.com', 'image2.pubmatic.com', 'sync.srv.stackadapt.com', 'ssl-ccstatic.highwebmedia.com', 'roomimg.stream.highwebmedia.com', 'cdn.exoticads.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'cdn.cookielaw.org', 'warnermediagroup-com.videoplayerhub.com', 'mid.rkdms.com', 'www.ugdturner.com', 'tru.am', 'widgets.tree.com', 'widgets.outbrain.com', 'smetrics.cnn.com', 'mrb.upapi.net', 'turner2.demdex.net', 'assets.bounceexchange.com', 'umto.cnn.com', 'www.att.com', 'i.cdn.tbs.com', 'www.warnermediaprivacy.com', 'i.cdn.trutv.com', 'bleacherreport.com', 'i.cdn.tntdrama.com', 'widget-pixels.outbrain.com', 'ml314.com', 'odb.outbrain.com', 'ad-delivery.net', 'secure-us.imrworldwide.com', 'pixel.mtrcs.samba.tv', 'www.adultswim.com', 'myattlog.att.com', 'beacon.krxd.net', 'b1sync.zemanta.com', 'aa.agkn.com', 'rtb.mfadsrvr.com', 'sync.outbrain.com', 'x.bidswitch.net', 'pippio.com', 'px.powerlinks.com', 'ps.eyeota.net', 'dsp.adfarm1.adition.com', 'loadus.exelator.com', 'id.geistm.com', 'sofia.trustx.org', 'pixel-us-east.rubiconproject.com', 'creativecdn.com', 'sync.adotmob.com', 'prod.perf-serving.com', 'cnn.bounceexchange.com', 'www.espn.com', 'privacyportal-eu.onetrust.com', 'sw88.espn.com', 'tredir.espn.com', 'fastlane.rubiconproject.com', 'adserver-us.adtech.advertising.com', 'stags.bluekai.com', 'sp.auth.adobe.com', 'ssum-sec.casalemedia.com', 'nep.advangelists.com', 'secure.adnxs.com', 'c1.adform.net', 'token.rubiconproject.com', 'casale-match.dotomi.com', 'cm.eyereturn.com', 'id.sharedid.org', 'www.zillow.com', 'dsum.casalemedia.com', 'cookiex.ngd.yahoo.com', 'e.zg-api.com', 'pxl.jivox.com', 'pt.ispot.tv', 'www.chase.com', 'sync.jivox.com', 'ct.pinterest.com', 'www.etsy.com', 'sites.chase.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'rc.rlcdn.com', 'trkn.us', 'insight.adsrvr.org', 'tags.w55c.net', 'www.apple.com', 'lnkd.demdex.net', 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', 'tags.srv.stackadapt.com', 'sp.analytics.yahoo.com', 'bs.serving-sys.com', 'sslwidget.criteo.com', 'b92.yahoo.co.jp', 'simage2.pubmatic.com', 'cdn.bizible.com', 'cdn.bizibly.com', 'www.adobe.com', 'a.rfihub.com', '20799319p.rfihub.com', 'adobeid-na1.services.adobe.com', 'sstats.adobe.com', 'www.nytimes.com', 'geolocation.onetrust.com', 'match.prod.bidr.io', 'a.et.nytimes.com', 'contextual.media.net', 'nytimes.com', 'meter-svc.nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'play.google.com', 'secure.insightexpressai.com', 'u.openx.net', 'www.aliexpress.com', 'sc.iasds01.com', 'pixel-a.sitescout.com', 'um.simpli.fi', 'sync.ipredictive.com', 'ad.turn.com', 'cdp.aliexpress.com', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'login.aliexpress.ru', 'login.tmall.ru', 'gj.mmstat.com', 'us.ynuf.aliapp.org', 'oneid.mmstat.com', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'worcester.craigslist.org', 'cw.addthis.com', 'www.okta.com', 'geoip-js.com', 'www.walmart.com', 'j.6sc.co', 'js.clearbit.com', 'b.6sc.co', 'segments.company-target.com', 'pixel.tapad.com', 'beacon.walmart.com', 'tap.walmart.com', 'tapestry.tapad.com', 't.myvisualiq.net', 'cf-us.wal.co', 'fa-us-dyn.wal.co', 'www.twitter.com', 'ak-us-dyn.wal.co', 'i5-opt-v0.wal.co', 'i5-opt-pulsar.wal.co', 'cf-us-dyn.wal.co', 'twitter.com', 'www.livejasmin.com', 'i.liadm.com', 'ip-109-71-162-131.dditscdn.com', 'www.wellsfargo.com', 'connect.secure.wellsfargo.com', 'wellsfargobankna.demdex.net', 'ws.mmstat.com', 'log.mmstat.com', 'imgur.com', 'imgur.ccgateway.net', 'www9.smartadserver.com', 'loadeu.exelator.com', 'bh.contextweb.com', 'beacon.lynx.cognitivlabs.com', 'um2.eqads.com', 'rbp.mxptint.net', 'rtb-csync.smartadserver.com', 'odr.mookie1.com', 'www.salesforce.com', 'sync.tidaltv.com', 'px.steelhousemedia.com', 'trc.taboola.com', 'su.addthis.com', 'salesforcecom.demdex.net', 'omtr2.partners.salesforce.com', 'd.agkn.com', 'trc-events.taboola.com', 'www.homedepot.com', 'd.adroll.com', 'homedepot.demdex.net', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'cdn.quantummetric.com', 'siteintercept.qualtrics.com', 'optimizely-edge.salesforce.com', 'uipglob.semasio.net', 'www.imdb.com', 'ads.stickyadstv.com', 'sync.1rx.io', 'spl.zeotap.com', 'amazon.partners.tremorhub.com', 'px.surveywall-api.survata.com', 'ads.samba.tv', 'pi.ispot.tv', 'sync.taboola.com', 'image6.pubmatic.com', 'pixel.placed.com', 'ads.betweendigital.com', 'lciapi.ninthdecimal.com', 'sync.targeting.unrulymedia.com', 'www.hulu.com', 'sc-static.net', 'intljs.rmtag.com', 'tr.snapchat.com', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'collector-1564.tvsquared.com', 'di.rlcdn.com', 'nypi.dc-storm.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'hubt.pornhub.com', 'ads.trafficjunky.net', 'www.msn.com', 'web.vortex.data.msn.com', 'at.atwola.com', 'c.msn.com', 'adserver.adtech.advertising.com', 'web.ssp.yahoo.com', 'nym1-ib.adnxs.com', '15.zorosrv.com', 'cs.media.net', 'image8.pubmatic.com', 'www.indeed.com', 'onevideosync.uplynk.com', 'www.bizographics.com', 'match.sharethrough.com', 'secure.indeed.com', 'www.foxnews.com', 'omny.fm', 'js.taplytics.com', 'assets.omny.fm', 'foxnews.demdex.net', 'smetrics.foxnews.com', 'readmo.yahoo.com', 'feeds-elections.foxnews.com', 'foxnews-d.openx.net', 'r.turn.com', 'loadm.exelator.com', 'pm.w55c.net', 'pixel-sync.sitescout.com', 'cs.emxdgt.com', 'cdn.districtm.io', 'pixel.mathtag.com', 'gu.dyntrk.com', 'rtb.gumgum.com', 'ums.acuityplatform.com', 'sync.adaptv.advertising.com', 'dmp.brand-display.com', 'pulsepoint-match.dotomi.com', 'pubmatic-match.dotomi.com', 'sonata-notifications.taptapnetworks.com', 'image4.pubmatic.com', 'pixel.everesttech.net', 'simage4.pubmatic.com', 'sync.technoratimedia.com', 'tg.socdm.com', 'dmx.districtm.io', 'sync.adkernel.com', 'sync.resetdigital.co:10001', 'visitor.fiftyt.com', 'pixel.onaudience.com', 'pmp.mxptint.net', 'cm.adgrx.com', 'breitbart-com.videoplayerhub.com', 'resources.infolinks.com', 'trends.revcontent.com', 'router.infolinks.com', 'js.ad-score.com', 'rt3031.infolinks.com', 'data.ad-score.com', 'apex.go.sonobi.com', 'tr.blismedia.com', 'c.eu1.dyntrk.com', 'ads.yieldmo.com', 'api.intentiq.com', 'ap.lijit.com', 'aep.mxptint.net', 'onetag-sys.com', 'de.tynt.com', 'match.360yield.com', 'sync.extend.tv', 'cms.quantserve.com', 'ssc-cms.33across.com', 'sync.go.sonobi.com', 'ads.avct.cloud', 's.cpx.to', 'dmp.adform.net', 'pixel-eu.rubiconproject.com', 'tracking.emerse.com', 'sync.intentiq.com', 'tracks.momagic.com', 't.pswec.com', 'p4-cuzxorpw5gr2c-jnzgl3yrhhohvphf-280032-s1-v6exp3-v4.metric.gstatic.com', 'p4-hyzc2fbhsneik-fgjetsyb2q7kakve-386024-s1-v6exp3-v4.metric.gstatic.com']
# 378
# Edge
# ['www.google.com', 'play.google.com', 'www.youtube.com', 'accounts.google.com', 'googleads.g.doubleclick.net', 'securepubads.g.doubleclick.net', 'www.amazon.com', 'assoc-na.associates-amazon.com', 'ntp.msn.com', 'www.msn.com', 's.amazon-adsystem.com', 'www.yahoo.com', 'udc.yahoo.com', 'geo.yahoo.com', 'ads.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ups.analytics.yahoo.com', 'cms.analytics.yahoo.com', 'aa.agkn.com', 'dpm.demdex.net', 'tags.bluekai.com', 'pixel.advertising.com', 'www.facebook.com', 'cm.g.doubleclick.net', 'image8.pubmatic.com', 'ib.adnxs.com', 'bid.g.doubleclick.net', 'us-u.openx.net', 'b.gemini.yahoo.com', 'match.adsrvr.org', 'pixel.rubiconproject.com', 'bh.contextweb.com', 'pr-bh.ybp.yahoo.com', 'sync.mathtag.com', 'cs.emxdgt.com', 'cx.atdmt.com', 'www.zoom.us', 'www.reddit.com', 'c.aaxads.com', 'id.rlcdn.com', 'www.wikipedia.org', 'pixel.quantserve.com', 'www.ebay.com', 'rover.ebay.com', 'www.office.com', 'svcs.ebay.com', 'ocsrest.ebay.com', 'pulsar.ebay.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'www.netflix.com', 'c1.microsoft.com', 'c.bing.com', '4968236.fls.doubleclick.net', 'www.bing.com', 'outlook.live.com', 'www.instructure.com', 'bat.bing.com', 'pages.instructure.com', 'px.ads.linkedin.com', 'bam.nr-data.net', 'analytics.twitter.com', 'www.twitch.tv', 'app.link', 'www.microsoft.com', 'beacon.krxd.net', 'jslog.krxd.net', 'www.chaturbate.com', 'mscom.demdex.net', 'cm.everesttech.net', 'chaturbate.com', 'ssl-ccstatic.highwebmedia.com', 'roomimg.stream.highwebmedia.com', 'cdn.exoticads.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'cdn.cookielaw.org', 'warnermediagroup-com.videoplayerhub.com', 'mid.rkdms.com', 'www.ugdturner.com', 'tru.am', 'widgets.tree.com', 'widgets.outbrain.com', 'smetrics.cnn.com', 'assets.bounceexchange.com', 'mrb.upapi.net', 'i.cdn.tbs.com', 'i.cdn.tntdrama.com', 'www.warnermediaprivacy.com', 'www.att.com', 'bleacherreport.com', 'i.cdn.trutv.com', 'umto.cnn.com', 'widget-pixels.outbrain.com', 'ml314.com', 'secure-us.imrworldwide.com', 'odb.outbrain.com', 'ad-delivery.net', 'pixel.mtrcs.samba.tv', 'ad.doubleclick.net', 'www.adultswim.com', 'myattlog.att.com', 'cnn.bounceexchange.com', 'privacyportal-eu.onetrust.com', 'www.espn.com', 'sw88.espn.com', 'tredir.espn.com', 'www.zillow.com', 'e.zg-api.com', 'pt.ispot.tv', '4704202.fls.doubleclick.net', 'www.chase.com', 'pxl.jivox.com', 'www.etsy.com', 'midas.chase.com', 'rc.rlcdn.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'sites.chase.com', 'pippio.com', '8666735.fls.doubleclick.net', '9910951.fls.doubleclick.net', 'ct.pinterest.com', 'tags.w55c.net', 'insight.adsrvr.org', 'www.linkedin.com', 'trkn.us', 'www.apple.com', 'lnkd.demdex.net', 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', '8166291.fls.doubleclick.net', 'sp.analytics.yahoo.com', 'tags.srv.stackadapt.com', 'bs.serving-sys.com', 'b92.yahoo.co.jp', 'dnacdn.net', 'www.adobe.com', 'a.rfihub.com', 'adobeid-na1.services.adobe.com', 'sstats.adobe.com', 'geolocation.onetrust.com', 'www.nytimes.com', 'a.et.nytimes.com', 'nytimes.com', 'contextual.media.net', 'news.google.com', 'meter-svc.nytimes.com', 'a.nytimes.com', 'purr.nytimes.com', '5290727.fls.doubleclick.net', 'stags.bluekai.com', 'www.aliexpress.com', 'cdp.aliexpress.com', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'login.aliexpress.ru', 'us.ynuf.aliapp.org', 'gj.mmstat.com', 'login.tmall.ru', 'oneid.mmstat.com', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'geoip-js.com', 'www.walmart.com', 'j.6sc.co', 'jadserve.postrelease.com', 'js.clearbit.com', 'match.prod.bidr.io', 'b.6sc.co', 'pixel.tapad.com', 'segments.company-target.com', 'beacon.walmart.com', 'tap.walmart.com', 'secure.adnxs.com', 'a.tribalfusion.com', '8114842.fls.doubleclick.net', 'idsync.rlcdn.com', 'tapestry.tapad.com', 't.myvisualiq.net', 'loadus.exelator.com', 'www.twitter.com', 'cf-us.wal.co', 'i.liadm.com', 'www.livejasmin.com', 'twitter.com', 'dw.wmt.co', 'ip-109-71-162-131.dditscdn.com', 'www.wellsfargo.com', 'connect.secure.wellsfargo.com', 'wellsfargobankna.demdex.net', '2549153.fls.doubleclick.net', 'ws.mmstat.com', 'log.mmstat.com', 'imgur.com', 'imgur.ccgateway.net', 'www9.smartadserver.com', 'di.rlcdn.com', 'loadeu.exelator.com', 'www.salesforce.com', '2382028.fls.doubleclick.net', 'px.steelhousemedia.com', 'trc.taboola.com', 'omtr2.partners.salesforce.com', 'www.homedepot.com', 'trc-events.taboola.com', 'cdn.quantummetric.com', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'optimizely-edge.salesforce.com', 'www.imdb.com', 'd.adroll.com', 'spl.zeotap.com', 'ads.stickyadstv.com', 'sync.1rx.io', 'x.bidswitch.net', 'amazon.partners.tremorhub.com', 'c1.adform.net', 'odr.mookie1.com', 'ads.samba.tv', 'px.surveywall-api.survata.com', 'sync.search.spotxchange.com', 'ssum-sec.casalemedia.com', 'token.rubiconproject.com', 'bsw.digitru.st', 'us-east-sync.bidswitch.net', 'pixel.placed.com', 'image6.pubmatic.com', 'lciapi.ninthdecimal.com', 'pi.ispot.tv', 'sync.taboola.com', 'www.hulu.com', 'intljs.rmtag.com', 'collect.tealiumiq.com', 'sc-static.net', 'tr.snapchat.com', 'datacloud.tealiumiq.com', '3797690.fls.doubleclick.net', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'collector-1564.tvsquared.com', 'nypi.dc-storm.com', 'p.adsymptotic.com', 'www.pornhub.com', 'hubt.pornhub.com', 'ads.trafficjunky.net', 'a.adtng.com', 'web.vortex.data.msn.com', 'c.msn.com', 'at.atwola.com', 'web.ssp.yahoo.com', 'rtb-use.mfadsrvr.com', 'js.brealtime.com', 'biddr.brealtime.com', 'e1.emxdgt.com', 'www.indeed.com', 'sync-tm.everesttech.net', 'p.rfihub.com', 'pixel-sync.sitescout.com', 'ad.turn.com', 'sync.resetdigital.co', 'aorta.clickagy.com', 'www.foxnews.com', 'secure.indeed.com', 'omny.fm', 'js.taplytics.com', 'contributor.google.com', 'smetrics.foxnews.com', '8980432.fls.doubleclick.net', 'assets.omny.fm', 'feeds-elections.foxnews.com', 'foxnews-d.openx.net', 'fastlane.rubiconproject.com', 'sofia.trustx.org', 'breitbart-com.videoplayerhub.com', 'resources.infolinks.com', 'trends.revcontent.com', 'router.infolinks.com', 'b1sync.zemanta.com', 'rtb.mfadsrvr.com', 'bttrack.com', 'rt3036.infolinks.com', 'js.ad-score.com', 'apex.go.sonobi.com', 'de.tynt.com', 'ap.lijit.com', 'onetag-sys.com', 'ssc-cms.33across.com', 'sync.go.sonobi.com', 's.cpx.to', 'data.ad-score.com', 'api.intentiq.com', 'pixel-eu.rubiconproject.com']
# 298
# FireFox
# ['www.google.com', 'www.youtube.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'www.amazon.com', 'assoc-na.associates-amazon.com', 'www.yahoo.com', 's.amazon-adsystem.com', 'tags.bluekai.com', 'pixel.advertising.com', 'aa.agkn.com', 'x.bidswitch.net', 'udc.yahoo.com', 'geo.yahoo.com', 'oao-js-tag.onemobile.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'ups.analytics.yahoo.com', 'ssum-sec.casalemedia.com', 'secure.adnxs.com', 'us-u.openx.net', 'ib.adnxs.com', 'bh.contextweb.com', 'sync.mathtag.com', 'cs.emxdgt.com', 'match.adsrvr.org', 'contextual.media.net', 'rtb.mfadsrvr.com', 'pr-bh.ybp.yahoo.com', 'image8.pubmatic.com', 'dsum-sec.casalemedia.com', 'onevideosync.uplynk.com', 'ad.atdmt.com', 'image6.pubmatic.com', 'sync.go.sonobi.com', 'pm.w55c.net', 'gcm.ctnsnet.com', 'image2.pubmatic.com', 'c.eu1.dyntrk.com', 'image4.pubmatic.com', 'www.facebook.com', 'www.zoom.us', 'www.reddit.com', 'c.aaxads.com', 'id.rlcdn.com', 'www.wikipedia.org', 'www.ebay.com', 'rover.ebay.com', 'www.office.com', 'pulsar.ebay.com', 'login.microsoftonline.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'www.netflix.com', 'www.bing.com', 'outlook.live.com', 'www.instructure.com', 'bat.bing.com', 'pages.instructure.com', 'settings.luckyorange.net', 'px.ads.linkedin.com', 'www.linkedin.com', 'p.adsymptotic.com', 'www.twitch.tv', 'www.microsoft.com', 'www.chaturbate.com', 'c1.microsoft.com', 'c.bing.com', 'chaturbate.com', 'ssl-ccstatic.highwebmedia.com', 'cdn.exoticads.com', 'roomimg.stream.highwebmedia.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'cdn.cookielaw.org', 'tru.am', 'assets.bounceexchange.com', 'dpm.demdex.net', 'ml314.com', 'umto.cnn.com', 'mid.rkdms.com', 'warnermediagroup-com.videoplayerhub.com', 'www.ugdturner.com', 'mrb.upapi.net', 'bleacherreport.com', 'www.warnermediaprivacy.com', 'i.cdn.tbs.com', 'i.cdn.tntdrama.com', 'i.cdn.trutv.com', 'www.att.com', 'secure-us.imrworldwide.com', 'ad-delivery.net', 'myattlog.att.com', 'cnn.bounceexchange.com', 'www.adultswim.com', 'widgets.tree.com', 'widgets.outbrain.com', 'analytics.twitter.com', 'smetrics.cnn.com', 'cm.everesttech.net', 'turner2.demdex.net', 'widget-pixels.outbrain.com', 'htlb.casalemedia.com', 'www.espn.com', 'fastlane.rubiconproject.com', 'sofia.trustx.org', 'sw88.espn.com', 'beacon.krxd.net', 'tredir.espn.com', 'stags.bluekai.com', 'sp.auth.adobe.com', 'plus.espn.com', 'www.zillow.com', 'nep.advangelists.com', 'e.zg-api.com', 'www.chase.com', 'secure03b.chase.com', 'midas.chase.com', 'www.etsy.com', 'sites.chase.com', 'www.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', 'sp.analytics.yahoo.com', 'www.adobe.com', 'adobeid-na1.services.adobe.com', 'www.nytimes.com', 'a.et.nytimes.com', 'nytimes.com', 'meter-svc.nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'secure.insightexpressai.com', 'play.google.com', 'sc.iasds01.com', 'u.openx.net', 'pixel-us-east.rubiconproject.com', 'token.rubiconproject.com', 'i.w55c.net', 'ad.turn.com', 'um.simpli.fi', 'pixel-a.sitescout.com', 'sync.ipredictive.com', 'idsync.rlcdn.com', 'p.rfihub.com', 'pixel.rubiconproject.com', 'pippio.com', 'simage2.pubmatic.com', 'www.aliexpress.com', 'cdp.aliexpress.com', 'acs.aliexpress.com', 'gpsfront.aliexpress.com', 'login.aliexpress.ru', 'gj.mmstat.com', 'login.tmall.ru', 'us.ynuf.aliapp.org', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'geoip-js.com', 'geolocation.onetrust.com', 'jadserve.postrelease.com', 'js.clearbit.com', 'match.prod.bidr.io', 'j.6sc.co', 'segments.company-target.com', 'b.6sc.co', 'pixel.tapad.com', 'privacyportal.onetrust.com', 'www.walmart.com', 'd.adroll.com', 'beacon.walmart.com', 'tap.walmart.com', 'ct.pinterest.com', 'a.tribalfusion.com', 't.myvisualiq.net', 'tapestry.tapad.com', 'www.twitter.com', 'www.livejasmin.com', 'twitter.com', 'www.wellsfargo.com', 'connect.secure.wellsfargo.com', 'ws.mmstat.com', 'log.mmstat.com', 'imgur.com', 'pixel.quantserve.com', 'imgur.ccgateway.net', 'outlook.office.com', 'loadeu.exelator.com', 'www9.smartadserver.com', 'di.rlcdn.com', 'c1.adform.net', 'sync.1rx.io', 'rtb.adentifi.com', 'sync.intentiq.com', 'tr.blismedia.com', 'id.knsso.com', 'rbp.mxptint.net', 'sync1.intentiq.com', 'bttrack.com', 'rtb-csync.smartadserver.com', 'ums.acuityplatform.com', 'sync.targeting.unrulymedia.com', 'www.salesforce.com', 'salesforcecom.demdex.net', 'insight.adsrvr.org', 'omtr2.partners.salesforce.com', 'trc.taboola.com', 'px.steelhousemedia.com', 'trc-events.taboola.com', 'www.homedepot.com', 'homedepot.demdex.net', 'optimizely-edge.salesforce.com', 'www.imdb.com', 'www.hulu.com', 'sc-static.net', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'intljs.rmtag.com', 'ut.ra.linksynergy.com', 'tr.snapchat.com', 'consent.linksynergy.com', 'collector-1564.tvsquared.com', 'nypi.dc-storm.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'hubt.pornhub.com', 'a.adtng.com', 'www.msn.com', 'c.msn.com', 'web.vortex.data.msn.com', 'at.atwola.com', 'adserver.adtech.advertising.com', 'api.taboola.com', 'web.ssp.yahoo.com', 'www.bizographics.com', 'loadus.exelator.com', 'b1sync.zemanta.com', 'sync.outbrain.com', 'dsp.adfarm1.adition.com', 'match.sharethrough.com', 'ps.eyeota.net', 'sync.adotmob.com', 'creativecdn.com', 'id.geistm.com', 'hbx.media.net', 'adservice.google.com', 'cm.mgid.com', 'cs.lkqd.net', 'cm.eyereturn.com', 'cm.adgrx.com', 'casale-match.dotomi.com', 'dsum.casalemedia.com', 'px.powerlinks.com', 'www.indeed.com', 'g.bing.com', 'pt.ispot.tv', 'secure.indeed.com', 'www.foxnews.com', 'omny.fm', 'js.taplytics.com', 'assets.omny.fm', 'foxnews-d.openx.net', 'rtb.gumgum.com', 'foxnews.demdex.net', 'pulsepoint-match.dotomi.com', 'readmo.yahoo.com', 'pixel-sync.sitescout.com', 'smetrics.foxnews.com', 'cdn.districtm.io', 'sync.srv.stackadapt.com', 'bam-cell.nr-data.net', 'tg.socdm.com', 'sync.technoratimedia.com', 'feeds-elections.foxnews.com', 'loadm.exelator.com', 'r.turn.com', 'odr.mookie1.com', 'bam.nr-data.net', 'dnacdn.net', 'pubmatic-match.dotomi.com', 'pmp.mxptint.net', 'rcp.c.appier.net', 'sync.adaptv.advertising.com', 'visitor.fiftyt.com', 'cookiex.ngd.yahoo.com', 'dmx.districtm.io', 'simage4.pubmatic.com', 'pixel.onaudience.com', 'bcp.crwdcntrl.net', 'pool.admedo.com', 'sync.extend.tv', 'pixel.everesttech.net', 'sync.crwdcntrl.net', 'gocm.c.appier.net', 'sync.resetdigital.co:10001', 'sync.adkernel.com', 'px.owneriq.net', 'breitbart-com.videoplayerhub.com', 'cms.quantserve.com', 'resources.infolinks.com', 'router.infolinks.com', 'trends.revcontent.com', 'a.rfihub.com', 'aep.mxptint.net', 'beacon.lynx.cognitivlabs.com', 'rt3043.infolinks.com', 'de.tynt.com', 'ssc-cms.33across.com', 'onetag-sys.com', 's.cpx.to', 'api.intentiq.com', 'dmp.adform.net', 'ap.lijit.com', 'pixel-eu.rubiconproject.com', 'id5-sync.com', 'js.ad-score.com', 'rubiconcm.digitaleast.mobi', 'ads.avct.cloud', 'data.ad-score.com', 'd.turn.com', 'um2.eqads.com', 'match.adsby.bidtheatre.com', 'a.sportradarserving.com', 'acuityplatform.com', 'tracks.momagic.com', 'i.liadm.com', 'dsp.nrich.ai']
# 333
# Opera
# ['www.wikipedia.org', 'www.google.com', 'www.youtube.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'www.amazon.com', 'assoc-na.associates-amazon.com', 'www.yahoo.com', 'udc.yahoo.com', 'geo.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'ups.analytics.yahoo.com', 'cms.analytics.yahoo.com', 'tags.bluekai.com', 'www.facebook.com', 'dpm.demdex.net', 'pixel.advertising.com', 'beacon.krxd.net', 'aa.agkn.com', 'b.gemini.yahoo.com', 'us-u.openx.net', 'match.adsrvr.org', 'cs.emxdgt.com', 'sync-tm.everesttech.net', 'ib.adnxs.com', 'pixel.rubiconproject.com', 'image8.pubmatic.com', 'bh.contextweb.com', 'pr-bh.ybp.yahoo.com', 'sync.mathtag.com', 'x.bidswitch.net', 'image2.pubmatic.com', 'bsw.digitru.st', 'us-east-sync.bidswitch.net', 'onevideosync.uplynk.com', 'image4.pubmatic.com', 'cx.atdmt.com', 'www.zoom.us', 'www.reddit.com', 'c.aaxads.com', 'id.rlcdn.com', 's.amazon-adsystem.com', 'pixel.quantserve.com', 'www.ebay.com', 'rover.ebay.com', 'www.office.com', 'ocsrest.ebay.com', 'svcs.ebay.com', 'pulsar.ebay.com', 'src.ebay-us.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'www.netflix.com', 'c1.microsoft.com', 'c.bing.com', 'www.bing.com', 'outlook.live.com', 'www.instructure.com', 'bat.bing.com', 'settings.luckyorange.net', 'pages.instructure.com', 'px.ads.linkedin.com', 'www.linkedin.com', 'p.adsymptotic.com', 'www.twitch.tv', 'analytics.twitter.com', 'bam.nr-data.net', 'app.link', 'match.prod.bidr.io', 'insight.adsrvr.org', 'secure.insightexpressai.com', 'secure-dcr.imrworldwide.com', 'www.microsoft.com', 'www.chaturbate.com', 'dapadobeproxyql.azurewebsites.net', 'dapadobeproxytest.azurewebsites.net', 'mscom.demdex.net', 'cm.everesttech.net', 'chaturbate.com', 'idsync.rlcdn.com', 'rtd-tm.everesttech.net', 'idpix.media6degrees.com', 'p.rfihub.com', 'ssl-ccstatic.highwebmedia.com', 'roomimg.stream.highwebmedia.com', 'cdn.exoticads.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'cdn.cookielaw.org', 'mid.rkdms.com', 'warnermediagroup-com.videoplayerhub.com', 'www.ugdturner.com', 'tru.am', 'turner2.demdex.net', 'smetrics.cnn.com', 'widgets.tree.com', 'htlb.casalemedia.com', 'fastlane.rubiconproject.com', 'sofia.trustx.org', 'umto.cnn.com', 'mrb.upapi.net', 'assets.bounceexchange.com', 'i.cdn.tbs.com', 'i.cdn.tntdrama.com', 'i.cdn.trutv.com', 'www.warnermediaprivacy.com', 'bleacherreport.com', 'www.att.com', 'widgets.outbrain.com', 'ml314.com', 'widget-pixels.outbrain.com', 'pixel.mtrcs.samba.tv', 'ad-delivery.net', 'odb.outbrain.com', 'www.adultswim.com', 'myattlog.att.com', 'dsum-sec.casalemedia.com', 'ssum-sec.casalemedia.com', 'sync.search.spotxchange.com', 'b1sync.zemanta.com', 'sync.outbrain.com', 'cnn.bounceexchange.com', 'pippio.com', 'ps.eyeota.net', 'rtb.mfadsrvr.com', 'dsp.adfarm1.adition.com', 'loadus.exelator.com', 'px.powerlinks.com', 'id.geistm.com', 'pixel-us-east.rubiconproject.com', 'creativecdn.com', 'bttrack.com', 'sync.adotmob.com', 'token.rubiconproject.com', 'c1.adform.net', 'privacyportal-eu.onetrust.com', 'www.espn.com', 'pixel-sync.sitescout.com', 'cm.eyereturn.com', 'prg.kargo.com', 'cookiex.ngd.yahoo.com', 'ad4m.at', 'loadm.exelator.com', 'crb.kargo.com', 'pixel.tapad.com', 'sw88.espn.com', 'tredir.espn.com', 'entitlement.auth.adobe.com', 'adserver-us.adtech.advertising.com', 'sp.auth.adobe.com', 'plus.espn.com', 'ad.turn.com', 'stags.bluekai.com', 'secure.adnxs.com', 'pixel-a.sitescout.com', 'id.sharedid.org', 'casale-match.dotomi.com', 'um.simpli.fi', 'cm.adgrx.com', 'sync.ipredictive.com', 'pm.w55c.net', 'i.w55c.net', 'dsum.casalemedia.com', 'www.zillow.com', 'e.zg-api.com', 'www.chase.com', 'pt.ispot.tv', 'pxl.jivox.com', 'sync.jivox.com', 'ct.pinterest.com', 'bcp.crwdcntrl.net', 'secure01b.chase.com', 'midas.chase.com', 'sites.chase.com', 'www.etsy.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'rc.rlcdn.com', 'trkn.us', 'www.apple.com', 'lnkd.demdex.net', 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', 'tags.srv.stackadapt.com', 'sp.analytics.yahoo.com', 'sslwidget.criteo.com', 'bs.serving-sys.com', 'b92.yahoo.co.jp', 'cdn.bizible.com', 'cdn.bizibly.com', 'www.adobe.com', 'a.rfihub.com', '20799319p.rfihub.com', 'adobeid-na1.services.adobe.com', 'sstats.adobe.com', 'www.nytimes.com', 'geolocation.onetrust.com', 'adobe.demdex.net', 'segments.company-target.com', 'a.et.nytimes.com', 'contextual.media.net', 'nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'meter-svc.nytimes.com', 'www.aliexpress.com', 'play.google.com', 'sc.iasds01.com', 'login.aliexpress.ru', 'cdp.aliexpress.com', 'login.tmall.ru', 'acs.aliexpress.com', 'gpsfront.aliexpress.com', 'gj.mmstat.com', 'us.ynuf.aliapp.org', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'oneid.mmstat.com', 'worcester.craigslist.org', 'ynuf.alipay.com', 'www.okta.com', 'geoip-js.com', 'j.6sc.co', 'js.clearbit.com', 'jadserve.postrelease.com', 'b.6sc.co', 'privacyportal.onetrust.com', 'www.walmart.com', 'd.adroll.com', 'simage2.pubmatic.com', 'sync.taboola.com', 'beacon.walmart.com', 'tap.walmart.com', 'gum.criteo.com', 'a.tribalfusion.com', 'tapestry.tapad.com', 't.myvisualiq.net', 'www.twitter.com', 'www.livejasmin.com', 'i.liadm.com', 'twitter.com', 'ip-109-71-162-131.dditscdn.com', 'www.wellsfargo.com', 'connect.secure.wellsfargo.com', 'wellsfargobankna.demdex.net', 'prod5-eum-appdynamics.wellsfargo.com', 'ws.mmstat.com', 'log.mmstat.com', 'imgur.com', 'imgur.ccgateway.net', 'www9.smartadserver.com', 'loadeu.exelator.com', 'www.salesforce.com', 'px.steelhousemedia.com', 'trc.taboola.com', 'salesforcecom.demdex.net', 'omtr2.partners.salesforce.com', 'd.agkn.com', 'trc-events.taboola.com', 'www.homedepot.com', 'homedepot.demdex.net', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'cdn.quantummetric.com', 'siteintercept.qualtrics.com', 'pixel.mathtag.com', 'd.turn.com', 'pix.revjet.com', 'homedepot-app.quantummetric.com', 'd.btttag.com', 'optimizely-edge.salesforce.com', 'su.addthis.com', 'ads.scorecardresearch.com', 'match.sharethrough.com', 'www.imdb.com', 'www.hulu.com', 'sc-static.net', 'intljs.rmtag.com', 'tr.snapchat.com', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'collector-1564.tvsquared.com', 'nypi.dc-storm.com', 'di.rlcdn.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'hubt.pornhub.com', 'ads.trafficjunky.net', 'a.adtng.com', 'www.msn.com', 'web.vortex.data.msn.com', 'c.msn.com', 'at.atwola.com', 'adserver.adtech.advertising.com', 'web.ssp.yahoo.com', 'cs.media.net', 'sync.1rx.io', 'ums.acuityplatform.com', 'www.bizographics.com', 'hbx.media.net', 'cm.mgid.com', 'api.taboola.com', 'image6.pubmatic.com', 'pubmatic-match.dotomi.com', 'simage4.pubmatic.com', 'rtb-csync.smartadserver.com', 'rtb.gumgum.com', 'px.owneriq.net', 'pmp.mxptint.net', 'sync.technoratimedia.com', 'cs.lkqd.net', 'g.bing.com', 'www.indeed.com', 'secure.indeed.com', 'www.foxnews.com', 'omny.fm', 'js.taplytics.com', 'assets.omny.fm', 'foxnews.demdex.net', 'smetrics.foxnews.com', 'readmo.yahoo.com', 'foxnews-d.openx.net', 'feeds-elections.foxnews.com', 'r.turn.com', 'sync.adaptv.advertising.com', 'tr.blismedia.com', 'rbp.mxptint.net', 'sync.intentiq.com', 'nep.advangelists.com', 'beacon.lynx.cognitivlabs.com', 'match.deepintent.com', 'sync1.intentiq.com', 'pixel.everesttech.net', 'gocm.c.appier.net', 'rtb.adentifi.com', 'a1510.casalemedia.com', 'tracking.emerse.com', 'cms.quantserve.com', 'ads.yieldmo.com', 'match.360yield.com', 'gm.demdex.net', 'da.admission.net', 'trends.revcontent.com', 'resources.infolinks.com', 'router.infolinks.com', 'js.ad-score.com', 'rt3045.infolinks.com', 'data.ad-score.com', 'rtb.openx.net', 'dclk-match.dotomi.com', 'ssbsync.smartadserver.com', 'c.eu1.dyntrk.com', 'sync.extend.tv', 'de.tynt.com', 'onetag-sys.com', 'ap.lijit.com', 'sync.go.sonobi.com', 'ssc-cms.33across.com', 's.cpx.to', 'id.knsso.com', 'rubiconcm.digitaleast.mobi', 'sync.srv.stackadapt.com', 'ads.stickyadstv.com', 'gu.dyntrk.com', 'cm.smadex.com', 'dmp.adform.net', 'pixel-eu.rubiconproject.com', 'www.messenger.com']
# 375

# Number of unique domains that at least one object is retrieved
# Brave
# ['laptop-updates.brave.com', 'crlsets.brave.com', 'www.google.com', 'ssl.gstatic.com', 'fonts.gstatic.com', 'www.gstatic.com', 'ogs.google.com', 'apis.google.com', 'adservice.google.com', 'googleads.g.doubleclick.net', 'www.youtube.com', 'i.ytimg.com', 'fonts.googleapis.com', 'go-updater.brave.com', 'componentupdater.brave.com', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'yt3.ggpht.com', 's.ytimg.com', 'pagead2.googlesyndication.com', 'static.doubleclick.net', 'r1---sn-ab5l6nsr.googlevideo.com', 'www.amazon.com', 'r1---sn-ab5sznld.googlevideo.com', 'images-na.ssl-images-amazon.com', 'm.media-amazon.com', 'fls-na.amazon.com', 'assoc-na.associates-amazon.com', 'unagi-na.amazon.com', 'completion.amazon.com', 'unagi.amazon.com', 'd23tl967axkois.cloudfront.net', 'd2in0p32vp1pij.cloudfront.net', 'www.yahoo.com', 'c.amazon-adsystem.com', 's.amazon-adsystem.com', 'player.live-video.net', 'brave-core-ext.s3.brave.com', 'p3a.brave.com', 's.yimg.com', 'aka-cdn.adtechus.com', 'udc.yahoo.com', 'guce.yahoo.com', 'geo.yahoo.com', 'sb.scorecardresearch.com', 'video-api.yql.yahoo.com', 'video.adaptv.advertising.com', 's1.yimg.com', 'bats.video.yahoo.com', 'us.y.atwola.com', 'edgecast-cf-prod.yahoo.net', 'edgecast-vod.yahoo.net', 'opus.analytics.yahoo.com', 'tag.idsync.analytics.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'us-east-1.onemobile.yahoo.com', 'www.facebook.com', 'static.xx.fbcdn.net', 'facebook.com', 'www.zoom.us', 'd24cgw3uvb9a9h.cloudfront.net', 'static.ada.support', 'rollout.ada.support', 'zoom.ada.support', 'www.reddit.com', 'styles.redditmedia.com', 'preview.redd.it', 'external-preview.redd.it', 'b.thumbs.redditmedia.com', 'www.redditstatic.com', 'a.thumbs.redditmedia.com', 'gql.reddit.com', 'i.redd.it', 'v.redd.it', 'www.wikipedia.org', 'alb.reddit.com', 'www.myshopify.com', 'cdn.shopify.com', 'www.ebay.com', 'ir.ebaystatic.com', 'i.ebayimg.com', 'www.office.com', 'pages.ebay.com', 'ocsrest.ebay.com', 'secureir.ebaystatic.com', 'img-prod-cms-rt-microsoft-com.akamaized.net', 'statics-marketingsites-eus-ms-com.akamaized.net', 'www.microsoft.com', 'blobs.officehome.msocdn.com', 'mem.gfx.ms', 'login.live.com', 'login.microsoftonline.com', 'logincdn.msauth.net', 'www.netflix.com', 'codex.nflxext.com', 'assets.nflxext.com', 'www.bing.com', 'www.live.com', 'outlook.live.com', 'ow2.res.office365.com', 'r4.res.office365.com', 'www.instructure.com', 'cdnjs.cloudflare.com', 'maps.googleapis.com', 'pages.instructure.com', 'fast.wistia.com', 'cdn.livechatinc.com', 'secure.livechatinc.com', 'www.twitch.tv', 'embedwistia-a.akamaihd.net', 'embed-fastly.wistia.com', 'p.twitchcdn.net', 'static.twitchcdn.net', 'video-edge-b8150b.pdx01.abs.hls.ttvnw.net', 'gql.twitch.tv', 'pubsub-edge.twitch.tv', 'static-cdn.jtvnw.net', 'irc-ws.chat.twitch.tv', 'api.twitch.tv', 'usher.ttvnw.net', 'video-weaver.lax03.hls.ttvnw.net', 'video-edge-834e50.ord02.abs.hls.ttvnw.net', 'microsoftmscompoc.tt.omtrdc.net', 'www.chaturbate.com', 'chaturbate.com', 'www.instagram.com', 'connect.facebook.net', 'www.cnn.com', 'www.i.cdn.cnn.com', 'agility.cnn.com', 'cdn.cookielaw.org', 'cdn.cnn.com', 'data.cnn.com', 'www.espn.com', 'a.espncdn.com', 'secure.espn.com', 'dcf.espn.com', 'a2.espncdn.com', 'a4.espncdn.com', 'a3.espncdn.com', 'a1.espncdn.com', 'www.googletagservices.com', 'site.web.api.espn.com', 'tredir.espn.com', 'cdn.registerdisney.go.com', 'fan.api.espn.com', 'platform.twitter.com', 'broadband.espn.com', 'entitlement.auth.adobe.com', 'api-app.espn.com', 'onefeed.fan.api.espn.com', 'sp.auth.adobe.com', 'secure.espncdn.com', 's.secure.espncdn.com', 'sw88.espn.com', 'syndication.twitter.com', 'cdn.unid.go.com', 'www.zillow.com', 'www.zillowstatic.com', 'www.chase.com', 'static.chasecdn.com', 'midas.chase.com', 'sites.chase.com', 'target.chase.com', 'www.etsy.com', 'img0.etsystatic.com', 'i.etsystatic.com', 'js.sentry-cdn.com', 'www.linkedin.com', 'static-exp1.licdn.com', 'platform.linkedin.com', 'www.apple.com', 'securemvt.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'dropbox.com', 'cfl.dropboxstatic.com', 'www.adobe.com', 'static.adobelogin.com', 's7d1.scene7.com', 'use.typekit.net', 'geo2.adobe.com', 'assets.adobedtm.com', 'adobeid-na1.services.adobe.com', 'ims-na1.adobelogin.com', 'geo.adobe.com', 'adobe.tt.omtrdc.net', 'geolocation.onetrust.com', 'www.nytimes.com', 'g1.nyt.com', 'static01.nyt.com', 'samizdat-graphql.nytimes.com', 'www.googletagmanager.com', 'www.aliexpress.com', 'assets.alicdn.com', 'aeu.alicdn.com', 'ae01.alicdn.com', 'aeis.alicdn.com', 'login.aliexpress.ru', 'cdp.aliexpress.com', 'g.alicdn.com', 'login.tmall.ru', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'us.ynuf.aliapp.org', '7anrz9.tdum.alibaba.com', 'campaign.aliexpress.com', 'fourier.taobao.com', 'acjs.aliyun.com', 'message.aliexpress.com', 'lighthouse.aliexpress.com', 'i.alicdn.com', 'ald-lamp-us.alicdn.com', 'www.craigslist.org', 'img.alicdn.com', 'geo.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'polyfill.io', 'p.typekit.net', 'www.walmart.com', 'wt1ugse0be.execute-api.us-west-2.amazonaws.com', 'i5.wal.co', 'i5.walmartimages.com', 'ak-us.wal.co', 'cf-us.wal.co', 'fa-us.wal.co', 'www.twitter.com', 'fa-us-dyn.wal.co', 'zy-us.wal.co', 'zy-us-dyn.wal.co', 'twitter.com', 'cf-us-dyn.wal.co', 'i5-opt-v1.wal.co', 'i5-opt-pulsar.wal.co', 'ak-us-dyn.wal.co', 'i5-opt-v0.wal.co', 'abs.twimg.com', 'pbs.twimg.com', 'api.twitter.com', 'www.livejasmin.com', 'staticx2.dditscdn.com', 'staticx4.dditscdn.com', 'staticx1.dditscdn.com', 'staticx3.dditscdn.com', 'imgx0.dditscdn.com', 'imgx3.dditscdn.com', 'imgx1.dditscdn.com', 'jaws.dditscdn.com', 'api-gateway.dditsadn.com', 'dss-relay-109-71-164-49.dditscdn.com', 'www.wellsfargo.com', 'static.wellsfargo.com', 'www01.wellsfargomedia.com', 'www04.wellsfargomedia.com', 'connect.secure.wellsfargo.com', 'www20.wellsfargomedia.com', 'www.tmall.com', 'at.alicdn.com', 'ws.mmstat.com', 'top-tmm.taobao.com', 'suggest.taobao.com', 'aldh5.tmall.com', 'www.imgur.com', 'imgur.com', 's.imgur.com', 'api.imgur.com', 'quantcast.mgr.consensu.org', 'i.imgur.com', 'www.force.com', 'www.salesforce.com', 'c1.sfdcstatic.com', 'a.sfdcstatic.com', 'service.force.com', 'www.homedepot.com', 'nexus.ensighten.com', 'assets.homedepot-static.com', 'contentgrid.homedepot-static.com', 'assets-qa.homedepot-static.com', 'homedepot.tt.omtrdc.net', 'clickstream-killswitch.hd-personalization-prod.gcp.homedepot.com', 'localization.thdws.com', '1ad356638475.cdn4.forter.com', 'lptag.liveperson.net', 'clickstream-producer.hd-personalization-prod.gcp.homedepot.com', '9190c8bb802c436c8a80719f22db73af-1ad356638475.cdn.forter.com', 'images.homedepot-static.com', 'www.res-x.com', 'cdn0.forter.com', 'cdn9.forter.com', 'mr.homedepot.com', 'optimizely-edge.salesforce.com', 'www.imdb.com', 'ia.media-imdb.com', 'www.hulu.com', 'c.evidon.com', 'assetshuluimcom-a.akamaihd.net', 'secure.hulu.com', 'www.pornhub.com', 'ci.phncdn.com', 'static.trafficjunky.com', 'di.phncdn.com', 'cdn1d-static-shared.phncdn.com', 'cdn1-smallimg.phncdn.com', 'www.msn.com', 'static-global-s-msn-com.akamaized.net', 'img-s-msn-com.akamaized.net', 'r.bing.com', 'www.indeed.com', 'd3hbwax96mbv6t.cloudfront.net', 'd3fw5vlhllyvee.cloudfront.net', 'autocomplete.indeed.com', 'cdn.ravenjs.com', 'pxl.indeed.com', 'www.foxnews.com', 'static.foxnews.com', 'global.fncstatic.com', 'a57.foxnews.com', 'omny.fm', 'webcontentassessor.global.ssl.fastly.net', 'assets.omny.fm', 'cdn.raygun.io', 'dpm.demdex.net', 'ajax.googleapis.com', 'contributor.google.com', 'www.omnycontent.com', 'feeds-elections.foxnews.com', 'apps.foxnews.com', 'my.foxnews.com', 'api.foxnews.com', 'www.breitbart.com', 'idms.foxbusiness.com', 'cdn.jsdelivr.net', 'media.breitbart.com', 'breitbartproduction.disqus.com']
# 336
# Chrome
# ['accounts.google.com', 'www.google.com', 'fonts.gstatic.com', 'ssl.gstatic.com', 'www.gstatic.com', 'apis.google.com', 'ogs.google.com', 'www.googleapis.com', 'adservice.google.com', 'www.youtube.com', 'fonts.googleapis.com', 'i.ytimg.com', 'googleads.g.doubleclick.net', 'securepubads.g.doubleclick.net', 'yt3.ggpht.com', 's.ytimg.com', 'static.doubleclick.net', 'www.amazon.com', 'pagead2.googlesyndication.com', 'images-na.ssl-images-amazon.com', 'm.media-amazon.com', 'fls-na.amazon.com', 'assoc-na.associates-amazon.com', 'unagi-na.amazon.com', 'completion.amazon.com', 'unagi.amazon.com', 'c.amazon-adsystem.com', 'player.live-video.net', 'd23tl967axkois.cloudfront.net', 'd2in0p32vp1pij.cloudfront.net', 's.amazon-adsystem.com', 'www.yahoo.com', 'usher.ttvnw.net', 's.yimg.com', 'player.stats.live-video.net', 'aka-cdn.adtechus.com', 'guce.yahoo.com', 'udc.yahoo.com', 'opus.analytics.yahoo.com', 'tag.idsync.analytics.yahoo.com', 'us.y.atwola.com', 'ads.yahoo.com', 'cms.analytics.yahoo.com', 'ups.analytics.yahoo.com', 'service.idsync.analytics.yahoo.com', 'pr-bh.ybp.yahoo.com', 'geo.yahoo.com', 'us-east-1.onemobile.yahoo.com', 'cdn.cmp.advertising.com', 'www.googletagservices.com', 'www.facebook.com', 'dpm.demdex.net', 'audex.userreport.com', 'pixel.advertising.com', 'tags.bluekai.com', 'tag.sp.advertising.com', 'b.gemini.yahoo.com', 'static.xx.fbcdn.net', 'facebook.com', 'cx.atdmt.com', 'www.zoom.us', 'd24cgw3uvb9a9h.cloudfront.net', 'static.ada.support', 'www.googletagmanager.com', 'www.google-analytics.com', 'rollout.ada.support', 'zoom.us', 'consent.trustarc.com', 'zoom.ada.support', 'www.reddit.com', 'www.redditstatic.com', 'preview.redd.it', 'external-preview.redd.it', 'b.thumbs.redditmedia.com', 'styles.redditmedia.com', 'a.thumbs.redditmedia.com', 'c.aaxads.com', 'gql.reddit.com', 'www.redditmedia.com', 'i.redd.it', 'www.aaxdetect.com', 'l3.aaxads.com', 'alb.reddit.com', 'id.rlcdn.com', 'www.wikipedia.org', 'sb.scorecardresearch.com', 'secure.quantserve.com', 'rules.quantcount.com', 'pixel.quantserve.com', 'www.myshopify.com', 'cdn.shopify.com', 'www.ebay.com', 'ir.ebaystatic.com', 'i.ebayimg.com', 'rover.ebay.com', 'srv.main.ebayrtm.com', 'www.office.com', 'cs.ns1p.net', 'pages.ebay.com', 'ocsrest.ebay.com', 's.ns1p.net', 'svcs.ebay.com', 'www.microsoft.com', 'pulsar.ebay.com', 'img-prod-cms-rt-microsoft-com.akamaized.net', 'statics-marketingsites-eus-ms-com.akamaized.net', 'mem.gfx.ms', 'blobs.officehome.msocdn.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'logincdn.msauth.net', 'www.netflix.com', 'c1.microsoft.com', 'c.bing.com', 'browser.pipe.aria.microsoft.com', 'codex.nflxext.com', 'assets.nflxext.com', 'ae.nflximg.net', 'ichnaea-web.netflix.com', '4968236.fls.doubleclick.net', 'www.googleadservices.com', 'www.bing.com', 'www.live.com', 'outlook.live.com', 'az725175.vo.msecnd.net', 'ow2.res.office365.com', 'r4.res.office365.com', 'www.instructure.com', 'pages.instructure.com', 'maps.googleapis.com', 'cdnjs.cloudflare.com', 'fast.wistia.com', 'dev.visualwebsiteoptimizer.com', 'cdn.livechatinc.com', 'pro.ip-api.com', 'static.ads-twitter.com', 'bat.bing.com', 'snap.licdn.com', 'connect.facebook.net', 'munchkin.marketo.net', 'www.googleoptimize.com', 'stats.g.doubleclick.net', 'd10lpsik1i8c69.cloudfront.net', 'secure.livechatinc.com', 'settings.luckyorange.net', 'px.ads.linkedin.com', '449-bvj-543.mktoresp.com', 't.co', 'www.linkedin.com', 'p.adsymptotic.com', 'js-agent.newrelic.com', 'www.twitch.tv', 'analytics.twitter.com', 'bam.nr-data.net', 'embedwistia-a.akamaihd.net', 'embed-fastly.wistia.com', 'p.twitchcdn.net', 'static.twitchcdn.net', 'video-edge-b8150b.pdx01.abs.hls.ttvnw.net', 'pubsub-edge.twitch.tv', 'gql.twitch.tv', 'irc-ws.chat.twitch.tv', 'static-cdn.jtvnw.net', 'app.link', 'cdn.krxd.net', 'api.twitch.tv', 'd2v02itv0y9u9t.cloudfront.net', 'cdn-gl.imrworldwide.com', 'api2.branch.io', 'microsoftmscompoc.tt.omtrdc.net', 'cdnssl.clicktale.net', 'www.chaturbate.com', 'mscom.demdex.net', 'cm.everesttech.net', 'c.clicktale.net', 'sync.mathtag.com', 'ib.adnxs.com', 'idsync.rlcdn.com', 'ing-district.clicktale.net', 'cm.g.doubleclick.net', 'update.googleapis.com', 'idpix.media6degrees.com', 'rtd.tubemogul.com', 'a.tribalfusion.com', 'clientservices.googleapis.com', 'px.owneriq.net', 'servedby.flashtalking.com', 'p.rfihub.com', 'rtd-tm.everesttech.net', 'match.adsrvr.org', 'jadserve.postrelease.com', 'bttrack.com', 'rtb.adentifi.com', 'dmpsync.3lift.com', 'sync-tm.everesttech.net', 'ds.reson8.com', 'sync.crwdcntrl.net', 'dsum-sec.casalemedia.com', 'pixel.rubiconproject.com', 'us-u.openx.net', 'chaturbate.com', 'sync.search.spotxchange.com', 'trc.taboola.com', 'image2.pubmatic.com', 'sync.srv.stackadapt.com', 'ssl-ccstatic.highwebmedia.com', 'google.com', 'roomimg.stream.highwebmedia.com', 'beacons.gcp.gvt2.com', 'cdn.exoticads.com', 'certify-js.alexametrics.com', 'adserver.exoticads.com', 'certify.alexametrics.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'www.i.cdn.cnn.com', 'graph.instagram.com', 'cdn.cookielaw.org', 'amplify.outbrain.com', 'cdn.cnn.com', 'agility.cnn.com', 'cdn.jsdelivr.net', 'cdn3.optimizely.com', 'warnermediagroup-com.videoplayerhub.com', 'mid.rkdms.com', 'api.rlcdn.com', 'd2uap9jskdzp2.cloudfront.net', 'a125375509.cdn.optimizely.com', 'cdn.adsafeprotected.com', 'cdn.segment.com', 'www.ugdturner.com', 'static.chartbeat.com', 'tag.bounceexchange.com', 'tru.am', 'get.s-onetag.com', 'acdn.adnxs.com', 'cdn.boomtrain.com', 'tr.outbrain.com', 'cdn.ml314.com', 'widgets.tree.com', 'as-sec.casalemedia.com', 'widgets.outbrain.com', 'smetrics.cnn.com', 'i.clean.gg', 'dw7nrwnn2bkh1.cloudfront.net', 'mrb.upapi.net', 'turner2.demdex.net', 'assets.bounceexchange.com', 'umto.cnn.com', 'data.cnn.com', 'logx.optimizely.com', 'onetag-geo.s-onetag.com', 'w.usabilla.com', 'api.segment.io', 'pixel.adsafeprotected.com', 'beacon.s-onetag.com', 'mab.chartbeat.com', 'www.att.com', 'zion.api.cnn.io', 'i.cdn.tbs.com', 'www.warnermediaprivacy.com', 'i.cdn.trutv.com', 'bleacherreport.com', 'i.cdn.tntdrama.com', 'tcheck.outbrainimg.com', 'widget-pixels.outbrain.com', 'consumer.krxd.net', 'ml314.com', 'geo-location.s-onetag.com', 'log.outbrainimg.com', 'onetag-geo-grouping.s-onetag.com', 'people.api.boomtrain.com', 'odb.outbrain.com', 'ad-delivery.net', 'secure-us.imrworldwide.com', 'ad.doubleclick.net', 'mcdp-nydc1.outbrain.com', 's.cdn.turner.com', 'onsiterecs.api.boomtrain.com', 'backend.upapi.net', 'z.moatads.com', 'ads.celtra.com', 'cache-ssl.celtra.com', 'pixel.moatads.com', 'pixel.mtrcs.samba.tv', 'tps.doubleverify.com', 'track.celtra.com', 'static.adsafeprotected.com', 'dt.adsafeprotected.com', 'maxcdn.bootstrapcdn.com', 'www.greatbigstory.com', 'www.adultswim.com', 's2.go-mpulse.net', 'myattlog.att.com', 's.go-mpulse.net', 'beacon.krxd.net', 'b1sync.zemanta.com', 'aa.agkn.com', 'rtb.mfadsrvr.com', 'sync.outbrain.com', 'x.bidswitch.net', 'dis.criteo.com', 'pippio.com', 'px.powerlinks.com', 'ps.eyeota.net', 'dsp.adfarm1.adition.com', 'sync-jp.im-apps.net', 'loadus.exelator.com', 'id.geistm.com', 'sofia.trustx.org', 'c.go-mpulse.net', 'pixel-us-east.rubiconproject.com', 'creativecdn.com', 'sync.adotmob.com', 'usermatch.krxd.net', 'prod.perf-serving.com', 'ams.creativecdn.com', '173c5b0c.akstat.io', 'cnn.bounceexchange.com', 'trial-eum-clientnsv4-s.akamaihd.net', 'trial-eum-clienttons-s.akamaihd.net', 'qll7g7tiqfb2qx4r6wba-poylb9-139695cf1-clientnsv4-s.akamaihd.net', '130-215-243-126_s-104-129-67-168_ts-1603401090-clienttons-s.akamaihd.net', 'events.bouncex.net', 'www.espn.com', 'signal-metrics-collector-beta.s-onetag.com', 'connect-metrics-collector.s-onetag.com', 'privacyportal-eu.onetrust.com', 'a.espncdn.com', 'secure.espn.com', 'www.summerhamster.com', 'dcf.espn.com', 'a3.espncdn.com', 'a1.espncdn.com', 'a2.espncdn.com', 'a4.espncdn.com', 'sw88.espn.com', 'site.web.api.espn.com', 'tredir.espn.com', 'cdn.registerdisney.go.com', 'espndotcom.tt.omtrdc.net', 'platform.twitter.com', 'fan.api.espn.com', 'entitlement.auth.adobe.com', 'broadband.espn.com', 'd.impactradius-event.com', 'fastlane.rubiconproject.com', 'adserver-us.adtech.advertising.com', 'api-app.espn.com', 'stags.bluekai.com', 'onefeed.fan.api.espn.com', 'tpc.googlesyndication.com', 'sp.auth.adobe.com', '2a89b9dc9f171855261585fbbaa9b6b7.safeframe.googlesyndication.com', 'px.moatads.com', 'mb.moatads.com', 'geo.moatads.com', 'secure.espncdn.com', 's.secure.espncdn.com', '8397396.fls.doubleclick.net', 'vision.fn-pz.com', 'secure-gl.imrworldwide.com', 'cdn.unid.go.com', 'eus.rubiconproject.com', 'ssum-sec.casalemedia.com', 'syndication.twitter.com', 'nep.advangelists.com', 'unid.go.com', 'secure.adnxs.com', 'secure-sdk.imrworldwide.com', 'c1.adform.net', 'token.rubiconproject.com', 'casale-match.dotomi.com', 'cm.eyereturn.com', 'd.adroll.com', 'id.sharedid.org', 'nmcsync.imrworldwide.com', '8ygzq5aq0gwttnxwqc5iadl4zzarg1603401099.nuid.imrworldwide.com', 'www.zillow.com', 'dsum.casalemedia.com', 'cookiex.ngd.yahoo.com', 'www.zillowstatic.com', 'e.zg-api.com', 'collector-pxhyx10rg3.px-cloud.net', '4704202.fls.doubleclick.net', 'pxl.jivox.com', 's.pinimg.com', 'pt.ispot.tv', 'www.chase.com', 'sync.jivox.com', 'ct.pinterest.com', 'static.chasecdn.com', 'midas.chase.com', 'www.etsy.com', 'analytics.chase.com', 'target.chase.com', 'sites.chase.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'rc.rlcdn.com', 'i.etsystatic.com', 'img0.etsystatic.com', '8666735.fls.doubleclick.net', '9910951.fls.doubleclick.net', 'www.dwin1.com', 'web.btncdn.com', 'resources.xg4ken.com', 'js.adsrvr.org', 'trkn.us', 'insight.adsrvr.org', 'tags.w55c.net', 'static-exp1.licdn.com', 'platform.linkedin.com', 'www.apple.com', 'lnkd.demdex.net', 'securemvt.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'dropbox.com', 'cfl.dropboxstatic.com', 'marketing.dropbox.com', 'tags.tiqcdn.com', 'static.criteo.net', '8166291.fls.doubleclick.net', 'snapengage.dropbox.com', 
# 'secure-ds.serving-sys.com', 'tags.srv.stackadapt.com', 'cdn.bizible.com', 'b92.yahoo.co.jp', 'sp.analytics.yahoo.com', 'bs.serving-sys.com', 'sslwidget.criteo.com', 'gum.criteo.com', 'storage.googleapis.com', 'www.snapengage.com', 'simage2.pubmatic.com', 'cdn.bizibly.com', 'www.adobe.com', 'c1.rfihub.net', 'a.rfihub.com', '20799319p.rfihub.com', 'static.adobelogin.com', 's7d1.scene7.com', 'use.typekit.net', 'geo2.adobe.com', 'adobeid-na1.services.adobe.com', 'assets.adobedtm.com', 'ims-na1.adobelogin.com', 'geo.adobe.com', 'sstats.adobe.com', 'www.nytimes.com', 'geolocation.onetrust.com', 'adobe.tt.omtrdc.net', 'api.demandbase.com', 'www.everestjs.net', 'scripts.demandbase.com', 'pixel.everesttech.net', 'universal.iperceptions.com', 'adobeioruntime.net', 'lasteventf-tm.everesttech.net', 'api.company-target.com', 'match.prod.bidr.io', 'g1.nyt.com', 'static01.nyt.com', 'samizdat-graphql.nytimes.com', 'als-svc.nytimes.com', 'a.et.nytimes.com', 'news.google.com', 'contextual.media.net', 'nytimes.com', 'rumcdn.geoedge.be', '55cf1a49aa07af3a2a26bec375e413a5.safeframe.googlesyndication.com', 'hblg.media.net', 'cdneast2-xch.media.net', 'dd.nytimes.com', 'meter-svc.nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'content.api.nytimes.com', 'cslogger.media.net', 'mwcm.nytimes.com', 'a1.nyt.com', 'tags.bkrtx.com', '5290727.fls.doubleclick.net', 'play.google.com', 'pnytimes.chartbeat.net', 'static01.nytimes.com', 'secure.insightexpressai.com', 'u.openx.net', 'ads.pubmatic.com', 'www.aliexpress.com', 'eb2.3lift.com', 'vp.nyt.com', 'sc.iasds01.com', 'pixel-a.sitescout.com', 'um.simpli.fi', 'sync.ipredictive.com', 'ad.turn.com', 'assets.alicdn.com', 'aeu.alicdn.com', 'ae01.alicdn.com', 'hbxlp.media.net', 'aeis.alicdn.com', 'g.alicdn.com', 'cdp.aliexpress.com', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'login.aliexpress.ru', 'login.tmall.ru', 'gj.mmstat.com', 'us.ynuf.aliapp.org', 'cfcmli.tdum.alibaba.com', 'fourier.taobao.com', 'campaign.aliexpress.com', 'i.alicdn.com', 'ald-lamp-us.alicdn.com', 'acjs.aliyun.com', 'retcode-us-west-1.arms.aliyuncs.com', 'img.alicdn.com', 'oneid.mmstat.com', 'message.aliexpress.com', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'geo.craigslist.org', 'worcester.craigslist.org', 'cw.addthis.com', 'www.okta.com', 'polyfill.io', 'p.typekit.net', 'geoip-js.com', '855-qah-699.mktoresp.com', 'wt1ugse0be.execute-api.us-west-2.amazonaws.com', 'www.walmart.com', 'j.6sc.co', 'cdn.heapanalytics.com', 'j.mrpdata.net', 'bid.g.doubleclick.net', 'c.6sc.co', 'js.clearbit.com', 'web.chtbl.com', 'b.6sc.co', 'js.driftt.com', 'heapanalytics.com', 'segments.company-target.com', 'pixel.tapad.com', 'x.clearbit.com', 'tag.demandbase.com', 'site-optimization-api.company-target.com', 'i5.wal.co', 'i5.walmartimages.com', 'beacon.walmart.com', 'b.wal.co', 'collector-pxu6b0qd2s.px-cloud.net', '82f993aae96f34c61bf9c5e80abbf767.safeframe.googlesyndication.com', 'tap.walmart.com', '8114842.fls.doubleclick.net', 'vt.myvisualiq.net', 'tapestry.tapad.com', 't.myvisualiq.net', 'cdn.doubleverify.com', 'csi.gstatic.com', 'cdn3.doubleverify.com', 'zy-us.wal.co', 'ak-us.wal.co', 'cf-us.wal.co', 
# 'fa-us.wal.co', 'fa-us-dyn.wal.co', 'tps10257.doubleverify.com', 'www.twitter.com', 'ak-us-dyn.wal.co', 'i5-opt-v0.wal.co', 'i5-opt-pulsar.wal.co', 'cf-us-dyn.wal.co', 'twitter.com', 'abs.twimg.com', 'pbs.twimg.com', 'api.twitter.com', 'www.livejasmin.com', 'i.liadm.com', 'i6.liadm.com', 'staticx4.dditscdn.com', 'staticx3.dditscdn.com', 'staticx2.dditscdn.com', 'staticx1.dditscdn.com', 'imgx0.dditscdn.com', 'imgx3.dditscdn.com', 'imgx2.dditscdn.com', 'imgx1.dditscdn.com', 'jaws.dditscdn.com', 'd31qbv1cthcecs.cloudfront.net', 'analytics.google.com', 'static.dditscdn.com', 'api-gateway.dditsadn.com', 'ip-109-71-162-131.dditscdn.com', 'dss-relay-109-71-164-55.dditscdn.com', 'www.wellsfargo.com', 'static.hotjar.com', 'vars.hotjar.com', 'script.hotjar.com', 'static.wellsfargo.com', 'www01.wellsfargomedia.com', 'www04.wellsfargomedia.com', 'connect.secure.wellsfargo.com', 'www20.wellsfargomedia.com', 'www.tmall.com', 'wellsfargobankna.demdex.net', '2549153.fls.doubleclick.net', 'cdn.appdynamics.com', 'at.alicdn.com', 'aldh5.tmall.com', 'top-tmm.taobao.com', 'suggest.taobao.com', 'log.mmstat.com', 'ac.mmstat.com', 'gm.mmstat.com', 'ws.mmstat.com', 'www.imgur.com', 'imgur.com', 's.imgur.com', 'quantcast.mgr.consensu.org', 'api.imgur.com', 'api.amplitude.com', 'imgur.ccgateway.net', 'oa.openxcdn.net', 'ced.sascdn.com', 'ced-ns.sascdn.com', 'tagan.adlightning.com', 'test.quantcast.mgr.consensu.org', 'i.imgur.com', 'cdn.ccgateway.net', 'carbon-cdn.ccgateway.net', 'www9.smartadserver.com', 'secure-assets.rubiconproject.com', 'clipcentric-a.akamaihd.net', 'loadeu.exelator.com', 'analytics.ccgateway.net', 'ad.clipcentric.com', 'tr.clipcentric.com', 'bh.contextweb.com', 'www.force.com', 'beacon.lynx.cognitivlabs.com', 'um2.eqads.com', 'rbp.mxptint.net', 'rtb-csync.smartadserver.com', 'odr.mookie1.com', 'www.salesforce.com', 'sync.tidaltv.com', 'c1.sfdcstatic.com', 'a.sfdcstatic.com', 'cdn.optimizely.com', 'a10681260716.cdn.optimizely.com', 'cdn.taboola.com', '2382028.fls.doubleclick.net', 'c.contentsquare.net', 'px.steelhousemedia.com', 'su.addthis.com', 'salesforcecom.demdex.net', 'omtr2.partners.salesforce.com', 'd.agkn.com', 'trc-events.taboola.com', 'service.force.com', 's.adroll.com', 'script.google.com', 'www.homedepot.com', 'd.adroll.mgr.consensu.org', '173c5b09.akstat.io', 'nexus.ensighten.com', 'assets.homedepot-static.com', 'contentgrid.homedepot-static.com', 'homedepot.demdex.net', 'client.px-cloud.net', 'ds-aksb-a.akamaihd.net', 'homedepot.tt.omtrdc.net', 'localization.thdws.com', 'clickstream-killswitch.hd-personalization-prod.gcp.homedepot.com', 'collector-pxj770cp7y.px-cloud.net', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'lptag.liveperson.net', 'cdn.quantummetric.com', '1ad356638475.cdn4.forter.com', '6gpwkrxh.micpn.com', 'siteintercept.qualtrics.com', '14ac2f9b630b4d1390c8ed50bcb74cee-1ad356638475.cdn.forter.com', 'optimizely-edge.salesforce.com', 'cdn3.forter.com', 'cds.taboola.com', 'uipglob.semasio.net', 'www.imdb.com', 'ia.media-imdb.com', 'aax-us-east.amazon-adsystem.com', 's.media-imdb.com', 'ads.stickyadstv.com', 'sync.1rx.io', 'spl.zeotap.com', 'amazon.partners.tremorhub.com', 'px.surveywall-api.survata.com', 'usersync.samplicio.us', 'ads.samba.tv', 'pi.ispot.tv', 'sync.taboola.com', 'image6.pubmatic.com', 'pixel.placed.com', 'ads.betweendigital.com', 'lciapi.ninthdecimal.com', 'sync.targeting.unrulymedia.com', 'www.hulu.com', 'c.evidon.com', 'assetshuluimcom-a.akamaihd.net', 'secure.hulu.com', 'metcon.hulu.com', 'vortex.hulu.com', 'sc-static.net', 'intljs.rmtag.com', '3797690.fls.doubleclick.net', 'collector-1564.tvsquared.com', 'tr.snapchat.com', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'di.rlcdn.com', 'nypi.dc-storm.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'vc.hotjar.io', 'in.hotjar.com', 'di.phncdn.com', 'static.trafficjunky.com', 'ci.phncdn.com', 'hubt.pornhub.com', 'cdn1d-static-shared.phncdn.com', 'cdn1-smallimg.phncdn.com', 'ads.trafficjunky.net', 'hw-cdn.trafficjunky.net', 'hw-cdn2.trafficjunky.net', 'vz-cdn2.trafficjunky.net', 'www.msn.com', 'static-global-s-msn-com.akamaized.net', 's.aolcdn.com', 'web.vortex.data.msn.com', 'confiant.msn.com', 'at.atwola.com', 'c.msn.com', 'msn.lockerdome.com', 'arc.msn.com', 'adserver.adtech.advertising.com', 'web.ssp.yahoo.com', 'nym1-ib.adnxs.com', 'prod-m-node-1113.ssp.yahoo.com', 'protected-by.clarium.io', 'cdn.adnxs.com', 'lg3.media.net', '15.zorosrv.com', 'cdn1.lockerdomecdn.com', 'vidstat.taboola.com', 'cs.media.net', 'imprnjmp.taboola.com', 'rb.adnxs.com', 'cvision.media.net', 'image8.pubmatic.com', 'www.indeed.com', 'match.taboola.com', 'onevideosync.uplynk.com', 'wf.taboola.com', 's3.amazonaws.com', 'r.bing.com', 'img-s-msn-com.akamaized.net', 'www.bizographics.com', 'vidstatb.taboola.com', 'srtb.msn.com', 'd3hbwax96mbv6t.cloudfront.net', 'd3fw5vlhllyvee.cloudfront.net', 'visitor.omnitagjs.com', 'match.sharethrough.com', 'ib.3lift.com', 'autocomplete.indeed.com', 'cdn.ravenjs.com', 't.indeed.com', 'secure.indeed.com', 'pxl.indeed.com', 'www.foxnews.com', 'static.foxnews.com', 'global.fncstatic.com', 'a57.foxnews.com', 'omny.fm', 'js.taplytics.com', 'webcontentassessor.global.ssl.fastly.net', 'contributor.google.com', 'assets.omny.fm', 'cdn.raygun.io', 'ajax.googleapis.com', '8980432.fls.doubleclick.net', 'foxnews.demdex.net', 'fundingchoicesmessages.google.com', 'smetrics.foxnews.com', 'www.omnycontent.com', 'ping.chartbeat.net', 'readmo.yahoo.com', 'mabping.chartbeat.net', 'api.nova.foxnews.com', 'bam-cell.nr-data.net', 'feeds-elections.foxnews.com', 'aswpsdkus.com', 'apps.foxnews.com', 'my.foxnews.com', 'api.foxnews.com', 'hbopenbid.pubmatic.com', 'bidder.criteo.com', 'foxnews-d.openx.net', 'ads.yieldmo.com', 'www.foxbusiness.com', '063f62e59a7ccccb4b087387a12fbdd6.safeframe.googlesyndication.com', '17d0991b.akstat.io', 'js-sec.indexww.com', 'foxnewsplayer-a.akamaihd.net', 'pixel.invitemedia.com', '79423.analytics.edgekey.net', 'r.turn.com', 'loadm.exelator.com', 'pm.w55c.net', 'ma1498-r.analytics.edgekey.net', 'amp.akamaized.net', '247preview.foxnews.com', 'rtb.openx.net', 'pixel-sync.sitescout.com', 'public.media.foxnews.com', 'x.dlx.addthis.com', 'load77.exelator.com', 'sync.adap.tv', 'cs.emxdgt.com', 'cdn.districtm.io', 'cti.w55c.net', 'pixel.mathtag.com', 'gu.dyntrk.com', 'rtb.gumgum.com', 'ums.acuityplatform.com', 'pix.impdesk.com', 'green.erne.co', 'sync.adaptv.advertising.com', 'dmp.brand-display.com', 'pulsepoint-match.dotomi.com', 'pubmatic-match.dotomi.com', 'sonata-notifications.taptapnetworks.com', 'image4.pubmatic.com', 'simage4.pubmatic.com', 'fcmatch.google.com', 'fonts.google.com', 'sync.technoratimedia.com', 'tg.socdm.com', 'fcmatch.youtube.com', 'dmx.districtm.io', 'sync.adkernel.com', 'us.creativecdn.com', 'us.shb-sync.com', 'www.breitbart.com', 'sync.resetdigital.co:10001', 'visitor.fiftyt.com', 'pixel.onaudience.com', 'pmp.mxptint.net', 'cm.adgrx.com', 'dmx.us-east-15.districtm.io', 'r.bidswitch.net', 'scripts.webcontentassessor.com', 'media.breitbart.com', 'hb.emxdgt.com', 'breitbartproduction.disqus.com', 'breitbart-com.videoplayerhub.com', 'f622adb0f78fe7121ee54e10e2a7a00e.safeframe.googlesyndication.com', 'trends.revcontent.com', 'resources.infolinks.com', 'router.infolinks.com', 'scripts.mf.webcontentassessor.com', 'ak.sail-horizon.com', 'd1bvk193qme2fc.cloudfront.net', 'js.ad-score.com', 'rt3031.infolinks.com', 'cdn.revcontent.com', 'api.sail-personalize.com', 'images.revcontent.com', 'imasdk.googleapis.com', 'data.ad-score.com', 'media.revcontent.com', 'apex.go.sonobi.com', 'partner.googleadservices.com', 'encrypted-tbn1.gstatic.com', 'encrypted-tbn3.gstatic.com', 'encrypted-tbn2.gstatic.com', 'tr.blismedia.com', 'p4-hyzc2fbhsneik-fgjetsyb2q7kakve-if-v6exp3-v4.metric.gstatic.com', 'p4-cuzxorpw5gr2c-jnzgl3yrhhohvphf-if-v6exp3-v4.metric.gstatic.com', 'ssbsync.smartadserver.com', 'c.eu1.dyntrk.com', 'r1---sn-ab5l6nzd.googlevideo.com', 'api.intentiq.com', 'ap.lijit.com', 'aep.mxptint.net', 'img.revcontent.com', 'onetag-sys.com', 'de.tynt.com', 'match.360yield.com', 'sync.go.sonobi.com', 'sync.extend.tv', 'cms.quantserve.com', 'ssc-cms.33across.com', 'ads.avct.cloud', 'assets.revcontent.com', 's.cpx.to', 'dmp.adform.net', 'pixel-eu.rubiconproject.com', 'tracking.emerse.com', 'cms-xch-chicago.33across.com', 'sync.intentiq.com', 'cms-xch.33across.com', 'tracks.momagic.com', 'eu-u.openx.net', 't.pswec.com', 'p4-cuzxorpw5gr2c-jnzgl3yrhhohvphf-280032-i2-v6exp3-ds.metric.ipv6test.net', 'p4-hyzc2fbhsneik-fgjetsyb2q7kakve-386024-i1-v6exp3.ds.metric.gstatic.com', 'p4-cuzxorpw5gr2c-jnzgl3yrhhohvphf-280032-i1-v6exp3-ds.metric.ipv6test.com', 'p4-hyzc2fbhsneik-fgjetsyb2q7kakve-386024-i2-v6exp3.v4.metric.gstatic.com', 'p4-cuzxorpw5gr2c-jnzgl3yrhhohvphf-280032-s1-v6exp3-v4.metric.gstatic.com', 'p4-hyzc2fbhsneik-fgjetsyb2q7kakve-386024-s1-v6exp3-v4.metric.gstatic.com']      
# 924
# Edge
# ['arc.msn.com', 'www.google.com', 'fonts.gstatic.com', 'ssl.gstatic.com', 'www.gstatic.com', 'ogs.google.com', 'apis.google.com', 'adservice.google.com', 'play.google.com', 'www.youtube.com', 'fonts.googleapis.com', 'i.ytimg.com', 'accounts.google.com', 'googleads.g.doubleclick.net', 'securepubads.g.doubleclick.net', 'yt3.ggpht.com', 's.ytimg.com', 'static.doubleclick.net', 'pagead2.googlesyndication.com', 'www.amazon.com', 'r2---sn-ab5sznly.googlevideo.com', 'images-na.ssl-images-amazon.com', 'edge.microsoft.com', 'm.media-amazon.com', 'fls-na.amazon.com', 'assoc-na.associates-amazon.com', 'ntp.msn.com', 'unagi-na.amazon.com', 'assets.msn.com', 'completion.amazon.com', 'www.msn.com', 'aax-us-east.amazon-adsystem.com', 'aan.amazon.com', 'img-s-msn-com.akamaized.net', 's.amazon-adsystem.com', 'd23tl967axkois.cloudfront.net', 'unagi.amazon.com', 'player.live-video.net', 'www.yahoo.com', 'd2in0p32vp1pij.cloudfront.net', 'usher.ttvnw.net', 's.yimg.com', 'r.bing.com', 'www.bing.com', 'udc.yahoo.com', 'geo.yahoo.com', 'aka-cdn.adtechus.com', 'guce.yahoo.com', 'opus.analytics.yahoo.com', 'tag.idsync.analytics.yahoo.com', 'us.y.atwola.com', 'ads.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ups.analytics.yahoo.com', 'us-east-1.onemobile.yahoo.com', 'cms.analytics.yahoo.com', 'aa.agkn.com', 'dpm.demdex.net', 'tags.bluekai.com', 'pixel.advertising.com', 'audex.userreport.com', 'www.facebook.com', 'cdn.cmp.advertising.com', 'dis.criteo.com', 'www.googletagservices.com', 'sb.scorecardresearch.com', 'cm.g.doubleclick.net', 'image8.pubmatic.com', 'ib.adnxs.com', 'bid.g.doubleclick.net', 'us-u.openx.net', 'b.gemini.yahoo.com', 'match.adsrvr.org', 'pixel.rubiconproject.com', 'bh.contextweb.com', 'pr-bh.ybp.yahoo.com', 'sync.mathtag.com', 'cs.emxdgt.com', 'api.msn.com', 'static.xx.fbcdn.net', 'facebook.com', 'fbcdn.net', 'cx.atdmt.com', 'fbsbx.com', 'connect.facebook.net', 'browser.pipe.aria.microsoft.com', 'www.zoom.us', 'd24cgw3uvb9a9h.cloudfront.net', 'static.ada.support', 'www.google-analytics.com', 'www.googletagmanager.com', 'rollout.ada.support', 'zoom.ada.support', 'zoom.us', 'consent.trustarc.com', 'www.reddit.com', 'www.redditstatic.com', 'preview.redd.it', 'styles.redditmedia.com', 'external-preview.redd.it', 'b.thumbs.redditmedia.com', 'i.redd.it', 'a.thumbs.redditmedia.com', 'gql.reddit.com', 'www.redditmedia.com', 'c.amazon-adsystem.com', 'c.aaxads.com', 'www.aaxdetect.com', 'l3.aaxads.com', 'gateway.reddit.com', 'id.rlcdn.com', 'www.wikipedia.org', 'secure.quantserve.com', 'alb.reddit.com', 'rules.quantcount.com', 'pixel.quantserve.com', 'www.myshopify.com', 'cdn.shopify.com', 'www.ebay.com', 'ir.ebaystatic.com', 'i.ebayimg.com', 'rover.ebay.com', 'www.office.com', 'svcs.ebay.com', 'ocsrest.ebay.com', 'pages.ebay.com', 'srv.main.ebayrtm.com', 'www.microsoft.com', 'blobs.officehome.msocdn.com', 'statics-marketingsites-eus-ms-com.akamaized.net', 'mem.gfx.ms', 'img-prod-cms-rt-microsoft-com.akamaized.net', 'pulsar.ebay.com', 'csi.gstatic.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'www.netflix.com', 'logincdn.msauth.net', 'c1.microsoft.com', 'c.bing.com', 'codex.nflxext.com', 'assets.nflxext.com', 'ae.nflximg.net', '4968236.fls.doubleclick.net', 'www.googleadservices.com', 'ichnaea-web.netflix.com', 'www.live.com', 'outlook.live.com', 'ow2.res.office365.com', 'az725175.vo.msecnd.net', 'r4.res.office365.com', 'www.instructure.com', 'pages.instructure.com', 'cdnjs.cloudflare.com', 'maps.googleapis.com', 'dev.visualwebsiteoptimizer.com', 'fast.wistia.com', 'cdn.livechatinc.com', 'pro.ip-api.com', 'snap.licdn.com', 'bat.bing.com', 'munchkin.marketo.net', 'www.googleoptimize.com', 'static.ads-twitter.com', 'secure.livechatinc.com', 'stats.g.doubleclick.net', 'px.ads.linkedin.com', '449-bvj-543.mktoresp.com', 't.co', 'js-agent.newrelic.com', 'bam.nr-data.net', 'analytics.twitter.com', 'www.twitch.tv', 'embedwistia-a.akamaihd.net', 'embed-fastly.wistia.com', 'static.twitchcdn.net', 'p.twitchcdn.net', 'gql.twitch.tv', 'video-edge-b8150b.pdx01.abs.hls.ttvnw.net', 'pubsub-edge.twitch.tv', 'irc-ws.chat.twitch.tv', 'static-cdn.jtvnw.net', 'api.twitch.tv', 'app.link', 'cdn.krxd.net', 'cdn-gl.imrworldwide.com', 'd2v02itv0y9u9t.cloudfront.net', 'api2.branch.io', 'countess.twitch.tv', 'consumer.krxd.net', 'secure-sts-prod.imrworldwide.com', 'video-weaver.dfw02.hls.ttvnw.net', 'beacon.krxd.net', 'jslog.krxd.net', 'video-edge-8c7934.iad05.abs.hls.ttvnw.net', 'www.chaturbate.com', 'microsoftmscompoc.tt.omtrdc.net', 'mscom.demdex.net', 'cdnssl.clicktale.net', 'cm.everesttech.net', 'c.clicktale.net', 'chaturbate.com', 'ing-district.clicktale.net', 'ssl-ccstatic.highwebmedia.com', 'roomimg.stream.highwebmedia.com', 'cdn.exoticads.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'graph.instagram.com', 'www.i.cdn.cnn.com', 'cdn.cnn.com', 'agility.cnn.com', 'amplify.outbrain.com', 'cdn.cookielaw.org', 'cdn.jsdelivr.net', 'cdn3.optimizely.com', 'api.rlcdn.com', 'd2uap9jskdzp2.cloudfront.net', 'warnermediagroup-com.videoplayerhub.com', 'a125375509.cdn.optimizely.com', 'mid.rkdms.com', 'cdn.adsafeprotected.com', 'cdn.segment.com', 'www.ugdturner.com', 'static.chartbeat.com', 'tag.bounceexchange.com', 'tru.am', 'get.s-onetag.com', 'widgets.tree.com', 'cdn.boomtrain.com', 'tr.outbrain.com', 'cdn.ml314.com', 'acdn.adnxs.com', 'widgets.outbrain.com', 'data.cnn.com', 'turner2.demdex.net', 'smetrics.cnn.com', 'mab.chartbeat.com', 'w.usabilla.com', 
# 'assets.bounceexchange.com', 'i.clean.gg', 'mrb.upapi.net', 'i.cdn.tbs.com', 'dw7nrwnn2bkh1.cloudfront.net', 'beacon.s-onetag.com', 'i.cdn.tntdrama.com', 'onetag-geo.s-onetag.com', 'www.warnermediaprivacy.com', 'www.att.com', 'people.api.boomtrain.com', 'bleacherreport.com', 'i.cdn.trutv.com', 'umto.cnn.com', 'logx.optimizely.com', 'pixel.adsafeprotected.com', 'api.segment.io', 'as-sec.casalemedia.com', 'maxcdn.bootstrapcdn.com', 'tcheck.outbrainimg.com', 'widget-pixels.outbrain.com', 'ml314.com', 'log.outbrainimg.com', 'onetag-geo-grouping.s-onetag.com', 'onsiterecs.api.boomtrain.com', 'geo-location.s-onetag.com', 's.cdn.turner.com', 'secure-us.imrworldwide.com', 'odb.outbrain.com', 'ad-delivery.net', 'z.moatads.com', 'ad.doubleclick.net', 'ads.celtra.com', 'backend.upapi.net', 'pixel.moatads.com', 'cache-ssl.celtra.com', 'tps.doubleverify.com', 'pixel.mtrcs.samba.tv', 'static.adsafeprotected.com', 'track.celtra.com', 'www.adultswim.com', 'dt.adsafeprotected.com', 's.go-mpulse.net', 's2.go-mpulse.net', 'myattlog.att.com', 'ds-aksb-a.akamaihd.net', 'c.go-mpulse.net', 'cnn.bounceexchange.com', 'www.greatbigstory.com', 'events.bouncex.net', '36ebc234.akstat.io', 'privacyportal-eu.onetrust.com', 'www.espn.com', 'connect-metrics-collector.s-onetag.com', 'signal-metrics-collector-beta.s-onetag.com', 'tpc.googlesyndication.com', 'trial-eum-clienttons-s.akamaihd.net', 'trial-eum-clientnsv4-s.akamaihd.net', 'a.espncdn.com', 'secure.espn.com', '173c5b08.akstat.io', 'dcf.espn.com', 'a2.espncdn.com', 'a1.espncdn.com', 'a3.espncdn.com', 'a4.espncdn.com', 'site.web.api.espn.com', 'sw88.espn.com', 'tredir.espn.com', 'd.impactradius-event.com', 'cdn.registerdisney.go.com', 'fan.api.espn.com', 'platform.twitter.com', 'entitlement.auth.adobe.com', 'www.zillow.com', 'broadband.espn.com', 'espndotcom.tt.omtrdc.net', 'www.zillowstatic.com', 'e.zg-api.com', 'collector-pxhyx10rg3.px-cloud.net', '4704202.fls.doubleclick.net', 'pt.ispot.tv', 'www.chase.com', 'usermatch.krxd.net', 'pxl.jivox.com', 'static.chasecdn.com', 'www.etsy.com', 'analytics.chase.com', 'target.chase.com', 'midas.chase.com', 'rc.rlcdn.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'sites.chase.com', 'pippio.com', 'i.etsystatic.com', 'img0.etsystatic.com', '8666735.fls.doubleclick.net', '9910951.fls.doubleclick.net', 'www.dwin1.com', 's.pinimg.com', 'web.btncdn.com', 'ct.pinterest.com', 'resources.xg4ken.com', 'js.adsrvr.org', 'tags.w55c.net', 'insight.adsrvr.org', 'www.linkedin.com', 'trkn.us', 'static-exp1.licdn.com', 'platform.linkedin.com', 'www.apple.com', 'lnkd.demdex.net', 'securemvt.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'dropbox.com', 'cfl.dropboxstatic.com', 'marketing.dropbox.com', '8166291.fls.doubleclick.net', 'tags.tiqcdn.com', 'static.criteo.net', 'secure-ds.serving-sys.com', 'sp.analytics.yahoo.com', 'tags.srv.stackadapt.com', 'snapengage.dropbox.com', 'b92.yahoo.co.jp', 'cdn.bizible.com', 'storage.googleapis.com', 'gum.criteo.com', 'sslwidget.criteo.com', 'bs.serving-sys.com', 'www.snapengage.com', 'ag.gbc.criteo.com', 'gem.gbc.criteo.com', 'dnacdn.net', 'csm.va.us.criteo.net', 'www.adobe.com', 'c1.rfihub.net', 'a.rfihub.com', 'use.typekit.net', 's7d1.scene7.com', 'static.adobelogin.com', 'geo2.adobe.com', 'assets.adobedtm.com', 'adobeid-na1.services.adobe.com', 'ims-na1.adobelogin.com', 'geo.adobe.com', 'sstats.adobe.com', 'geolocation.onetrust.com', 'adobe.tt.omtrdc.net', 'www.nytimes.com', 'api.demandbase.com', 'scripts.demandbase.com', 'pixel.everesttech.net', 'g1.nyt.com', 'static01.nyt.com', 'samizdat-graphql.nytimes.com', 'a.et.nytimes.com', 'als-svc.nytimes.com', 'nytimes.com', 'news.google.com', 'contextual.media.net', 'rumcdn.geoedge.be', 'dd.nytimes.com', 'meter-svc.nytimes.com', 'content.api.nytimes.com', 'a.nytimes.com', 'purr.nytimes.com', 'cdneast2-xch.media.net', '869fe4124e7da5e5e087e653295531f8.safeframe.googlesyndication.com', 'cslogger.media.net', 'mwcm.nytimes.com', '5290727.fls.doubleclick.net', 'a1.nyt.com', 'tags.bkrtx.com', 'stags.bluekai.com', 'www.aliexpress.com', 'pnytimes.chartbeat.net', 'assets.alicdn.com', 'aeu.alicdn.com', 'aeis.alicdn.com', 'g.alicdn.com', 'ae01.alicdn.com', 'cdp.aliexpress.com', 'gpsfront.aliexpress.com', 'acs.aliexpress.com', 'login.aliexpress.ru', 'us.ynuf.aliapp.org', 'gj.mmstat.com', 'login.tmall.ru', '95aq37.tdum.alibaba.com', 'fourier.taobao.com', 'campaign.aliexpress.com', 'i.alicdn.com', 'ald-lamp-us.alicdn.com', 'acjs.aliyun.com', 'retcode-us-west-1.arms.aliyuncs.com', 'img.alicdn.com', 'oneid.mmstat.com', 'message.aliexpress.com', 'lighthouse.aliexpress.com', 'www.craigslist.org', 'geo.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'polyfill.io', 'p.typekit.net', 'geoip-js.com', '855-qah-699.mktoresp.com', 'wt1ugse0be.execute-api.us-west-2.amazonaws.com', 'api.company-target.com', 'www.walmart.com', 'j.6sc.co', 'cdn.heapanalytics.com', 'j.mrpdata.net', 'jadserve.postrelease.com', 'js.clearbit.com', 'c.6sc.co', 'secure.adnxs.com', 'web.chtbl.com', 'match.prod.bidr.io', 'heapanalytics.com', 'b.6sc.co', 'tag.demandbase.com', 'pixel.tapad.com', 'x.clearbit.com', 'segments.company-target.com', 'i5.walmartimages.com', 'i5.wal.co', 'beacon.walmart.com', 'b.wal.co', 'collector-pxu6b0qd2s.px-cloud.net', '098820f14a9f0a356bcf0375b550fc18.safeframe.googlesyndication.com', 'tap.walmart.com', '8114842.fls.doubleclick.net', 'a.tribalfusion.com', 'vt.myvisualiq.net', 'idsync.rlcdn.com', 'tapestry.tapad.com', 't.myvisualiq.net', 'loadus.exelator.com', 'cdn.doubleverify.com', 'cdn3.doubleverify.com', 'tps10220.doubleverify.com', 'www.twitter.com', 'fa-us.wal.co', 'ak-us.wal.co', 'cf-us.wal.co', 'i.liadm.com', 'twitter.com', 'abs.twimg.com', 'www.livejasmin.com', 'pbs.twimg.com', 'api.twitter.com', 'staticx2.dditscdn.com', 'staticx4.dditscdn.com', 'staticx1.dditscdn.com', 'staticx3.dditscdn.com', 'dw.wmt.co', 'imgx0.dditscdn.com', 'imgx3.dditscdn.com', 'imgx1.dditscdn.com', 'imgx2.dditscdn.com', 'jaws.dditscdn.com', 'd31qbv1cthcecs.cloudfront.net', 'analytics.google.com', 'static.dditscdn.com', 'certify.alexametrics.com', 'api-gateway.dditsadn.com', 'ip-109-71-162-131.dditscdn.com', 'dss-relay-109-71-164-52.dditscdn.com', 'static.hotjar.com', 'www.wellsfargo.com', 'vars.hotjar.com', 'script.hotjar.com', 'static.wellsfargo.com', 'connect.secure.wellsfargo.com', 'www01.wellsfargomedia.com', 'www04.wellsfargomedia.com', 'www20.wellsfargomedia.com', 'www.tmall.com', 'wellsfargobankna.demdex.net', '2549153.fls.doubleclick.net', 'cdn.appdynamics.com', 'at.alicdn.com', 'aldh5.tmall.com', 'top-tmm.taobao.com', 'suggest.taobao.com', 'log.mmstat.com', 'gm.mmstat.com', 'ws.mmstat.com', 'ac.mmstat.com', 'www.imgur.com', 'imgur.com', 's.imgur.com', 'quantcast.mgr.consensu.org', 'api.imgur.com', 'imgur.ccgateway.net', 'api.amplitude.com', 'ced-ns.sascdn.com', 'oa.openxcdn.net', 'tagan.adlightning.com', 'ced.sascdn.com', 'test.quantcast.mgr.consensu.org', 'i.imgur.com', 'cdn.ccgateway.net', 'carbon-cdn.ccgateway.net', 'www9.smartadserver.com', 'clipcentric-a.akamaihd.net', 'di.rlcdn.com', 'loadeu.exelator.com', 'ad.clipcentric.com', 'tr.clipcentric.com', 'load77.exelator.com', 'www.force.com', 'www.salesforce.com', 'c1.sfdcstatic.com', 'cdn.optimizely.com', 'a.sfdcstatic.com', 'a10681260716.cdn.optimizely.com', '2382028.fls.doubleclick.net', 'cdn.taboola.com', 'px.steelhousemedia.com', 'c.contentsquare.net', 'trc.taboola.com', 'service.force.com', 'omtr2.partners.salesforce.com', 'salesforcecom.demdex.net', 'www.homedepot.com', 'trc-events.taboola.com', 'assets.homedepot-static.com', 'nexus.ensighten.com', 'contentgrid.homedepot-static.com', 'client.px-cloud.net', 'localization.thdws.com', 'homedepot.demdex.net', 'clickstream-killswitch.hd-personalization-prod.gcp.homedepot.com', 'collector-pxj770cp7y.px-cloud.net', 'homedepot.tt.omtrdc.net', 'cdn.quantummetric.com', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'optimizely-edge.salesforce.com', 's.adroll.com', 'cds.taboola.com', 'www.imdb.com', 'd.adroll.mgr.consensu.org', 'd.adroll.com', 'qll7g7tiqfb2qx4r6t6a-p5u7u9-aa18dcd0f-clientnsv4-s.akamaihd.net', '130-215-243-126_s-104-129-67-168_ts-1603400956-clienttons-s.akamaihd.net', '17d09914.akstat.io', 'ia.media-imdb.com', 's.media-imdb.com', 'spl.zeotap.com', 'ads.stickyadstv.com', 'sync.1rx.io', 'x.bidswitch.net', 'amazon.partners.tremorhub.com', 'usersync.samplicio.us', 'c1.adform.net', 'odr.mookie1.com', 'ads.samba.tv', 'px.surveywall-api.survata.com', 'sync.search.spotxchange.com', 'ssum-sec.casalemedia.com', 'lm.serving-sys.com', 'token.rubiconproject.com', 'bsw.digitru.st', 'us-east-sync.bidswitch.net', 'pixel.placed.com', 'image6.pubmatic.com', 'lciapi.ninthdecimal.com', 'pi.ispot.tv', 'sync.taboola.com', 'www.hulu.com', 'c.evidon.com', 'assetshuluimcom-a.akamaihd.net', 'secure.hulu.com', 'metcon.hulu.com', 'vortex.hulu.com', 'intljs.rmtag.com', 'collect.tealiumiq.com', 'sc-static.net', 'collector-1564.tvsquared.com', '3797690.fls.doubleclick.net', 'tr.snapchat.com', 'datacloud.tealiumiq.com', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'nypi.dc-storm.com', 'p.adsymptotic.com', 'vc.hotjar.io', 'in.hotjar.com', 'www.pornhub.com', 'static.trafficjunky.com', 'ci.phncdn.com', 'di.phncdn.com', 'hubt.pornhub.com', 'cdn1d-static-shared.phncdn.com', 'cdn1-smallimg.phncdn.com', 'ads.trafficjunky.net', 'a.adtng.com', 'vz-cdn2.trafficjunky.net', 'hw-cdn2.adtng.com', 'hw-cdn2.trafficjunky.net', 'static-global-s-msn-com.akamaized.net', 's.aolcdn.com', 'confiant.msn.com', 'web.vortex.data.msn.com', 'c.msn.com', 'at.atwola.com', 'msn.lockerdome.com', 'web.ssp.yahoo.com', 'prod-m-node-1113.ssp.yahoo.com', 'imp.emxdgt.com', 'de9a11s35xj3d.cloudfront.net', 'd31otfhas71ais.cloudfront.net', 'a3665.casalemedia.com', 'rtb-use.mfadsrvr.com', 'js.brealtime.com', 'biddr.brealtime.com', 'protected-by.clarium.io', 'e1.emxdgt.com', 'cdn1.lockerdomecdn.com', 'www.indeed.com', 'rtb.mfadsrvr.com', 'sync-tm.everesttech.net', 'p.rfihub.com', 'pixel-sync.sitescout.com', 'ad.turn.com', 'sync.resetdigital.co', 'ads.revjet.com', 'aorta.clickagy.com', 'cdn.revjet.com', 'd3fw5vlhllyvee.cloudfront.net', 'd3hbwax96mbv6t.cloudfront.net', 'www.foxnews.com', 'cdn.ravenjs.com', 'autocomplete.indeed.com', 't.indeed.com', 'secure.indeed.com', 'pxl.indeed.com', 'static.foxnews.com', 'global.fncstatic.com', 'a57.foxnews.com', 'omny.fm', 'webcontentassessor.global.ssl.fastly.net', 'js.taplytics.com', 'contributor.google.com', '8980432.fls.doubleclick.net', 'smetrics.foxnews.com', 'fundingchoicesmessages.google.com', 'assets.omny.fm', 'readmo.yahoo.com', 'foxnews.demdex.net', 'mabping.chartbeat.net', 'cdn.raygun.io', 'ping.chartbeat.net', 'api.nova.foxnews.com', 'feeds-elections.foxnews.com', 'ajax.googleapis.com', 'aswpsdkus.com', 'apps.foxnews.com', 'bam-cell.nr-data.net', 'my.foxnews.com', 'api.foxnews.com', 'www.omnycontent.com', 'hbopenbid.pubmatic.com', 'bidder.criteo.com', 'foxnews-d.openx.net', 'fastlane.rubiconproject.com', 'www.breitbart.com', 'ads.yieldmo.com', 'sofia.trustx.org', '36f58c293453d6ac0773f2d692bf8b27.safeframe.googlesyndication.com', 'www.foxbusiness.com', 'js-sec.indexww.com', 'ads.pubmatic.com', 'eus.rubiconproject.com', 'scripts.webcontentassessor.com', 'media.breitbart.com', 'hb.emxdgt.com', 'breitbartproduction.disqus.com', 'certify-js.alexametrics.com', 'd327faa1d81f219f3dfe435272b578c9.safeframe.googlesyndication.com', 'breitbart-com.videoplayerhub.com', 'resources.infolinks.com', 'cdn.ampproject.org', 'partner.googleadservices.com', 'trends.revcontent.com', 'router.infolinks.com', 'd1bvk193qme2fc.cloudfront.net', 'cdn.revcontent.com', 'b1sync.zemanta.com', 'bttrack.com', 'encrypted-tbn3.gstatic.com', 'rt3036.infolinks.com', 'encrypted-tbn2.gstatic.com', 'js.ad-score.com', 'encrypted-tbn1.gstatic.com', 'ak.sail-horizon.com', 'images.revcontent.com', 'r1---sn-ab5szn7y.googlevideo.com', 'imasdk.googleapis.com', 'media.revcontent.com', 'apex.go.sonobi.com', 'secure-assets.rubiconproject.com', 'de.tynt.com', 'ap.lijit.com', 'onetag-sys.com', 'ssc-cms.33across.com', 'sync.go.sonobi.com', 's.cpx.to', 'data.ad-score.com', 'api.intentiq.com', 'api.sail-personalize.com', 'pixel-eu.rubiconproject.com', 'nav.smartscreen.microsoft.com', 'smartscreen-prod.microsoft.com']
# 761
# FireFox
# ['detectportal.firefox.com', 'www.google.com', 'www.gstatic.com', 'firefox.settings.services.mozilla.com', 'apis.google.com', 'content-signature-2.cdn.mozilla.net', 'www.youtube.com', 'fonts.googleapis.com', 'fonts.gstatic.com', 'i.ytimg.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'yt3.ggpht.com', 's.ytimg.com', 'static.doubleclick.net', 'www.amazon.com', 'r3---sn-ab5szn7l.googlevideo.com', 'pagead2.googlesyndication.com', 'images-na.ssl-images-amazon.com', 'm.media-amazon.com', 'fls-na.amazon.com', 'completion.amazon.com', 'assoc-na.associates-amazon.com', 'aax-us-east.amazon-adsystem.com', 'unagi-na.amazon.com', 'd23tl967axkois.cloudfront.net', 'd2in0p32vp1pij.cloudfront.net', 'player.live-video.net', 'usher.ttvnw.net', 'video-weaver.ord02.hls.ttvnw.net', 'unagi.amazon.com', 'www.yahoo.com', 's.amazon-adsystem.com', 'tags.bluekai.com', 'pixel.advertising.com', 'aa.agkn.com', 'x.bidswitch.net', 's.yimg.com', 'guce.yahoo.com', 'sb.scorecardresearch.com', 'udc.yahoo.com', 'geo.yahoo.com', 'us.y.atwola.com', 'opus.analytics.yahoo.com', 'tag.idsync.analytics.yahoo.com', 'aka-cdn.adtechus.com', 'oao-js-tag.onemobile.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'us-east-1.onemobile.yahoo.com', 'ups.analytics.yahoo.com', 'adservice.google.com', 'partner.googleadservices.com', 'www.googletagservices.com', 'ssum-sec.casalemedia.com', 'cm.g.doubleclick.net', 'secure.adnxs.com', 'us-u.openx.net', 'ib.adnxs.com', 'bh.contextweb.com', 'sync.mathtag.com', 'cs.emxdgt.com', 'match.adsrvr.org', 'contextual.media.net', 'apx.moatads.com', 'geo.moatads.com', 'rtb.mfadsrvr.com', 'pr-bh.ybp.yahoo.com', 'tpc.googlesyndication.com', 'image8.pubmatic.com', 'dsum-sec.casalemedia.com', 's0.2mdn.net', 'onevideosync.uplynk.com', 'cdnjs.cloudflare.com', 'googleads4.g.doubleclick.net', 'ad.atdmt.com', 'image6.pubmatic.com', 'sync.go.sonobi.com', 'pm.w55c.net', 'gcm.ctnsnet.com', 'image2.pubmatic.com', 'c.eu1.dyntrk.com', 'image4.pubmatic.com', 'www.facebook.com', 'ade.googlesyndication.com', 'static.xx.fbcdn.net', 'facebook.com', 'www.zoom.us', 'd24cgw3uvb9a9h.cloudfront.net', 'static.ada.support', 'www.googletagmanager.com', 'www.google-analytics.com', 'consent.trustarc.com', 'zoom.us', 'rollout.ada.support', 'zoom.ada.support', 'www.reddit.com', 'styles.redditmedia.com', 'preview.redd.it', 'www.redditstatic.com', 'b.thumbs.redditmedia.com', 'external-preview.redd.it', 'i.redd.it', 'a.thumbs.redditmedia.com', 'c.amazon-adsystem.com', 'c.aaxads.com', 'gql.reddit.com', 'www.redditmedia.com', 'www.aaxdetect.com', 'l3.aaxads.com', 'id.rlcdn.com', 'alb.reddit.com', 'gateway.reddit.com', 'www.wikipedia.org', 'oops.redditmedia.com', 'www.myshopify.com', 'cdn.shopify.com', 'www.ebay.com', 'ir.ebaystatic.com', 'i.ebayimg.com', 'rover.ebay.com', 'www.office.com', 'www.microsoft.com', 'pulsar.ebay.com', 'blobs.officehome.msocdn.com', 'statics-marketingsites-eus-ms-com.akamaized.net', 'img-prod-cms-rt-microsoft-com.akamaized.net', 'mem.gfx.ms', 'login.microsoftonline.com', 'login.live.com', 'web.vortex.data.microsoft.com', 'logincdn.msauth.net', 'www.netflix.com', 'browser.pipe.aria.microsoft.com', 'codex.nflxext.com', 'assets.nflxext.com', 'ae.nflximg.net', 'www.googleadservices.com', '4968236.fls.doubleclick.net', 'ichnaea-web.netflix.com', 'cx.atdmt.com', 'www.bing.com', 'www.live.com', 'outlook.live.com', 'az725175.vo.msecnd.net', 'ow2.res.office365.com', 'r4.res.office365.com', 'www.instructure.com', 'maps.googleapis.com', 'pages.instructure.com', 'fast.wistia.com', 'dev.visualwebsiteoptimizer.com', 'pro.ip-api.com', 'connect.facebook.net', 'static.ads-twitter.com', 'd10lpsik1i8c69.cloudfront.net', 'cdn.livechatinc.com', 'bat.bing.com', 'snap.licdn.com', 'www.googleoptimize.com', 'secure.livechatinc.com', 'munchkin.marketo.net', 'stats.g.doubleclick.net', 't.co', 'settings.luckyorange.net', 'px.ads.linkedin.com', '449-bvj-543.mktoresp.com', 'www.linkedin.com', 'p.adsymptotic.com', 'www.twitch.tv', 'static.twitchcdn.net', 'p.twitchcdn.net', 'video-edge-b8150b.pdx01.abs.hls.ttvnw.net', 'pubsub-edge.twitch.tv', 'irc-ws.chat.twitch.tv', 'gql.twitch.tv', 'www.chaturbate.com', 'c1.microsoft.com', 'c.bing.com', 'chaturbate.com', 'ssl-ccstatic.highwebmedia.com', 'cdn.exoticads.com', 'roomimg.stream.highwebmedia.com', 'adserver.exoticads.com', 'certify-js.alexametrics.com', 'content.exoticads.com', 'certify.alexametrics.com', 'js-agent.newrelic.com', 'www.instagram.com', 'www.cnn.com', 'graph.instagram.com', 'cdn.cnn.com', 'cdn.cookielaw.org', 'cdn.jsdelivr.net', 'cdn3.optimizely.com', 'agility.cnn.com', 'cdn.segment.com', 'www.i.cdn.cnn.com', 'amplify.outbrain.com', 'static.chartbeat.com', 'tag.bounceexchange.com', 'tru.am', 'get.s-onetag.com', 'cdn.boomtrain.com', 'assets.bounceexchange.com', 'dpm.demdex.net', 'cdn.ml314.com', 'onetag-geo.s-onetag.com', 'beacon.s-onetag.com', 'tr.outbrain.com', 'data.cnn.com', 'api.segment.io', 'people.api.boomtrain.com', 'ml314.com', 'umto.cnn.com', 'api.rlcdn.com', 'mid.rkdms.com', 'cdn.krxd.net', 'warnermediagroup-com.videoplayerhub.com', 'www.ugdturner.com', 'a125375509.cdn.optimizely.com', 'cdn.adsafeprotected.com', 'acdn.adnxs.com', 'd2uap9jskdzp2.cloudfront.net', 'mab.chartbeat.com', 'w.usabilla.com', 'mrb.upapi.net', 'bleacherreport.com', 'www.warnermediaprivacy.com', 'i.cdn.tbs.com', 'i.cdn.tntdrama.com', 'i.cdn.trutv.com', 'dw7nrwnn2bkh1.cloudfront.net', 'i.clean.gg', 'www.att.com', 'logx.optimizely.com', 'secure-us.imrworldwide.com', 's.go-mpulse.net', 'ad-delivery.net', 'ad.doubleclick.net', 's2.go-mpulse.net', 'backend.upapi.net', 'consumer.krxd.net', 'myattlog.att.com', 's.cdn.turner.com', 'cnn.bounceexchange.com', 'events.bouncex.net', 'www.greatbigstory.com', 'www.adultswim.com', 'beacon.krxd.net', 'widgets.tree.com', 'widgets.outbrain.com', 'analytics.twitter.com', 'smetrics.cnn.com', 'cm.everesttech.net', 'turner2.demdex.net', 'pixel.adsafeprotected.com', 'c.go-mpulse.net', 'widget-pixels.outbrain.com', 'as-sec.casalemedia.com', 'log.outbrainimg.com', 'onetag-geo-grouping.s-onetag.com', 'onsiterecs.api.boomtrain.com', 'signal-metrics-collector-beta.s-onetag.com', 'connect-metrics-collector.s-onetag.com', 'geo-location.s-onetag.com', 'htlb.casalemedia.com', 'www.espn.com', 'bidder.criteo.com', 'fastlane.rubiconproject.com', 'sofia.trustx.org', 'secure.espn.com', 'dcf.espn.com', 'a.espncdn.com', 'www.summerhamster.com', 'a3.espncdn.com', 'a4.espncdn.com', 'a1.espncdn.com', 'a2.espncdn.com', '173c5b0f.akstat.io', 'sw88.espn.com', 'idsync.rlcdn.com', 'usermatch.krxd.net', 'site.web.api.espn.com', 'platform.twitter.com', 'tredir.espn.com', 'd.impactradius-event.com', 'broadband.espn.com', 'espndotcom.tt.omtrdc.net', 'entitlement.auth.adobe.com', 'api-app.espn.com', 'stags.bluekai.com', 'sp.auth.adobe.com', 'cdn.registerdisney.go.com', 'fan.api.espn.com', 'mb.moatads.com', 'px.moatads.com', 'onefeed.fan.api.espn.com', 'syndication.twitter.com', 'secure.espncdn.com', '8397396.fls.doubleclick.net', 'z.moatads.com', 'secure-gl.imrworldwide.com', 'plus.espn.com', 'eus.rubiconproject.com', 'cdn-gl.imrworldwide.com', 'pespn.chartbeat.net', 'www.zillow.com', 'cdn.unid.go.com', 'tags.bkrtx.com', 'www.zillowstatic.com', 'nep.advangelists.com', 'e.zg-api.com', 'collector-pxhyx10rg3.px-cloud.net', 'www.chase.com', 'static.chasecdn.com', 'secure03b.chase.com', 'midas.chase.com', 'target.chase.com', 'www.etsy.com', 'sites.chase.com', 'analytics.chase.com', 'i.etsystatic.com', 'img0.etsystatic.com', '8666735.fls.doubleclick.net', 'static-exp1.licdn.com', 'www.apple.com', 'securemvt.apple.com', 
# 'securemetrics.apple.com', 'www.dropbox.com', 'cfl.dropboxstatic.com', 'dropbox.com', 'marketing.dropbox.com', '8166291.fls.doubleclick.net', 'static.criteo.net', 'bid.g.doubleclick.net', 'tags.tiqcdn.com', 'gum.criteo.com', 'sslwidget.criteo.com', 'sp.analytics.yahoo.com', 'www.dropboxstatic.com', 'www.adobe.com', 'ag.gbc.criteo.com', 'gem.gbc.criteo.com', 'dnacdn.net', 'use.typekit.net', 'geo2.adobe.com', 'static.adobelogin.com', 's7d1.scene7.com', 'assets.adobedtm.com', 'geo.adobe.com', 'images-tv.adobe.com', 'adobeid-na1.services.adobe.com', 'www.nytimes.com', 'g1.nyt.com', 'static01.nyt.com', 'news.google.com', 'als-svc.nytimes.com', 'samizdat-graphql.nytimes.com', 'a.et.nytimes.com', 'rumcdn.geoedge.be', 'nytimes.com', 'meter-svc.nytimes.com', 'hblg.media.net', 'content.api.nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'cdneast2-xch.media.net', 'dd.nytimes.com', 'cslogger.media.net', 'static01.nytimes.com', 'vp.nyt.com', 'secure.insightexpressai.com', 'static.adsafeprotected.com', 'play.google.com', 'a1.nyt.com', 'sc.iasds01.com', 'ads.pubmatic.com', 'mwcm.nytimes.com', 'u.openx.net', 'eb2.3lift.com', '5290727.fls.doubleclick.net', 'dt.adsafeprotected.com', 'pnytimes.chartbeat.net', 'sync-tm.everesttech.net', 'fonts.google.com', 'pixel-us-east.rubiconproject.com', 'token.rubiconproject.com', 'i.w55c.net', 'ad.turn.com', 'um.simpli.fi', 'pixel-a.sitescout.com', 'sync.ipredictive.com', 'p.rfihub.com', 'pixel.rubiconproject.com', 'pippio.com', 'simage2.pubmatic.com', 'www.aliexpress.com', 'hbxlp.media.net', 'aeu.alicdn.com', 'assets.alicdn.com', 'g.alicdn.com', 'aeis.alicdn.com', 'ae01.alicdn.com', 'cdp.aliexpress.com', 'acs.aliexpress.com', 'gpsfront.aliexpress.com', 'cmapp9.tdum.alibaba.com', 'login.aliexpress.ru', 'gj.mmstat.com', 'login.tmall.ru', 'us.ynuf.aliapp.org', 'campaign.aliexpress.com', 'i.alicdn.com', 'fourier.taobao.com', 'acjs.aliyun.com', 'ald-lamp-us.alicdn.com', 'message.aliexpress.com', 'lighthouse.aliexpress.com', 'retcode-us-west-1.arms.aliyuncs.com', 'img.alicdn.com', 'www.craigslist.org', 'geo.craigslist.org', 'worcester.craigslist.org', 'www.okta.com', 'p.typekit.net', 'polyfill.io', 'geoip-js.com', '855-qah-699.mktoresp.com', 'wt1ugse0be.execute-api.us-west-2.amazonaws.com', 'geolocation.onetrust.com', 'api.company-target.com', 'j.mrpdata.net', 'scripts.demandbase.com', 'jadserve.postrelease.com', 'cdn.heapanalytics.com', 'js.clearbit.com', 'match.prod.bidr.io', 'j.6sc.co', 'tag.demandbase.com', 'x.clearbit.com', 'js.driftt.com', 'web.chtbl.com', 'c.6sc.co', 'site-optimization-api.company-target.com', 'heapanalytics.com', 'segments.company-target.com', 'b.6sc.co', 'pixel.tapad.com', 'privacyportal.onetrust.com', 's.adroll.com', 'www.walmart.com', 'd.adroll.mgr.consensu.org', 'i5.walmartimages.com', 'i5.wal.co', 'd.adroll.com', 'beacon.walmart.com', 'b.wal.co', 'collector-pxu6b0qd2s.px-cloud.net', 
# 'tap.walmart.com', '8114842.fls.doubleclick.net', 'vt.myvisualiq.net', 'ct.pinterest.com', 'a.tribalfusion.com', 't.myvisualiq.net', 'tapestry.tapad.com', 'www.twitter.com', 'twitter.com', 'abs.twimg.com', 'pbs.twimg.com', 'www.livejasmin.com', 'api.twitter.com', 'staticx1.dditscdn.com', 'staticx4.dditscdn.com', 'staticx2.dditscdn.com', 'staticx3.dditscdn.com', 'imgx0.dditscdn.com', 'imgx1.dditscdn.com', 'imgx3.dditscdn.com', 'imgx2.dditscdn.com', 'd31qbv1cthcecs.cloudfront.net', 'jaws.dditscdn.com', 'analytics.google.com', 'static.dditscdn.com', 'api-gateway.dditsadn.com', 'www.wellsfargo.com', 'static.wellsfargo.com', 'connect.secure.wellsfargo.com', 'www01.wellsfargomedia.com', 'www04.wellsfargomedia.com', 'cdn.appdynamics.com', 'www.tmall.com', 'at.alicdn.com', 'aldh5.tmall.com', 'top-tmm.taobao.com', 'log.mmstat.com', 'suggest.taobao.com', 'ac.mmstat.com', 'gm.mmstat.com', 'ws.mmstat.com', 'www.imgur.com', 'imgur.com', 's.imgur.com', 'quantcast.mgr.consensu.org', 'api.imgur.com', 'api.amplitude.com', 'i.imgur.com', 'pixel.quantserve.com', 'secure.quantserve.com', 'oa.openxcdn.net', 'imgur.ccgateway.net', 'tagan.adlightning.com', 'ced.sascdn.com', 'ced-ns.sascdn.com', 'cdn.ccgateway.net', 'carbon-cdn.ccgateway.net', 'test.quantcast.mgr.consensu.org', 'rules.quantcount.com', 'outlook.office.com', 'loadeu.exelator.com', 'www9.smartadserver.com', 'analytics.ccgateway.net', 'secure-assets.rubiconproject.com', 'clipcentric-a.akamaihd.net', 'di.rlcdn.com', 'tr.clipcentric.com', 'c1.adform.net', 'sync.1rx.io', 'rtb.adentifi.com', 'sync.intentiq.com', 'tr.blismedia.com', 'id.knsso.com', 'rbp.mxptint.net', 'sync1.intentiq.com', 'bttrack.com', 'rtb-csync.smartadserver.com', 'ums.acuityplatform.com', 'sync.targeting.unrulymedia.com', 'www.force.com', 'www.salesforce.com', 'cdn.optimizely.com', 'c1.sfdcstatic.com', 'a.sfdcstatic.com', 'a10681260716.cdn.optimizely.com', '2382028.fls.doubleclick.net', 'c.contentsquare.net', 'salesforcecom.demdex.net', 'service.force.com', 'cdn.taboola.com', 'insight.adsrvr.org', 'omtr2.partners.salesforce.com', 'trc.taboola.com', 'px.steelhousemedia.com', 'trc-events.taboola.com', 'www.homedepot.com', '17d09917.akstat.io', 'assets.homedepot-static.com', 'nexus.ensighten.com', 'contentgrid.homedepot-static.com', 'client.px-cloud.net', 'collector-pxj770cp7y.px-cloud.net', 'localization.thdws.com', 'homedepot.demdex.net', 'clickstream-killswitch.hd-personalization-prod.gcp.homedepot.com', 'homedepot.tt.omtrdc.net', 'optimizely-edge.salesforce.com', 'd35u1vg1q28b3w.cloudfront.net', 'www.imdb.com', 'ia.media-imdb.com', 'www.hulu.com', 's.media-imdb.com', 'assetshuluimcom-a.akamaihd.net', 'secure.hulu.com', 'metcon.hulu.com', 'vortex.hulu.com', 'js.adsrvr.org', '3797690.fls.doubleclick.net', 'sc-static.net', 'c.evidon.com', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'static.hotjar.com', 'intljs.rmtag.com', 'vars.hotjar.com', 'script.hotjar.com', 'collector-1564.tvsquared.com', 'ut.ra.linksynergy.com', 'tr.snapchat.com', 'consent.linksynergy.com', 'in.hotjar.com', 'vc.hotjar.io', 'nypi.dc-storm.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'ci.phncdn.com', 'static.trafficjunky.com', 'hubt.pornhub.com', 'di.phncdn.com', 'cdn1d-static-shared.phncdn.com', 'cdn1-smallimg.phncdn.com', 'ads.trafficjunky.net', 'media.trafficjunky.net', 'a.adtng.com', 'hw-cdn2.ang-content.com', 'www.msn.com', 'ew.phncdn.com', 'static-global-s-msn-com.akamaized.net', 'confiant.msn.com', 'c.msn.com', 'arc.msn.com', 'clientservices.googleapis.com', 'web.vortex.data.msn.com', 'ssl.gstatic.com', 's.aolcdn.com', 'clients4.google.com', 'at.atwola.com', 'update.googleapis.com', 'adserver.adtech.advertising.com', 'img-s-msn-com.akamaized.net', 'oauthaccountmanager.googleapis.com', 'ib.3lift.com', 'api.taboola.com', 'web.ssp.yahoo.com', 'www.bizographics.com', 'srtb.msn.com', 'r.bing.com', 'gce-sc.bidswitch.net', 'us-east-sync.bidswitch.net', 'loadus.exelator.com', 'prod-m-node-1113.ssp.yahoo.com', 'dis.criteo.com', 'b1sync.zemanta.com', 'sync.outbrain.com', 'dsp.adfarm1.adition.com', 'match.sharethrough.com', 'cmp-cdn.ghostery.com', 'ps.eyeota.net', 'sync.crwdcntrl.net', 'sync.adotmob.com', 'creativecdn.com', 'visitor.omnitagjs.com', 'id.geistm.com', 'hbx.media.net', 'pdc.bidswitch.net', 'sync-jp.im-apps.net', 'cm.mgid.com', 'ams.creativecdn.com', 'cs.lkqd.net', 'cm.eyereturn.com', 'cm.adgrx.com', 'casale-match.dotomi.com', 'lg3.media.net', 'dsum.casalemedia.com', 'res-a.akamaihd.net', 'cvision.media.net', 'safe-browsing-quorum.privacy.ghostery.net', 'api.ghostery.net', 'cdn.ghostery.com', 'offers-api.ghostery.net', 'px.powerlinks.com', 'd27xxe7juh1us6.cloudfront.net', 'www.indeed.com', 'd3fw5vlhllyvee.cloudfront.net', 'd3hbwax96mbv6t.cloudfront.net', 'g.bing.com', 'autocomplete.indeed.com', 'cdn.ravenjs.com', 'pt.ispot.tv', 't.indeed.com', 'secure.indeed.com', 'pxl.indeed.com', 'www.foxnews.com', 'sentry.indeed.com', 'static.foxnews.com', 'global.fncstatic.com', 'a57.foxnews.com', 'contributor.google.com', 'omny.fm', 'webcontentassessor.global.ssl.fastly.net', 'js.taplytics.com', '8980432.fls.doubleclick.net', 'hbopenbid.pubmatic.com', 'fundingchoicesmessages.google.com', 'assets.omny.fm', 'foxnews-d.openx.net', 'ajax.googleapis.com', 'cdn.raygun.io', 'rtb.gumgum.com', 'foxnews.demdex.net', 'pulsepoint-match.dotomi.com', 'readmo.yahoo.com', 'pixel-sync.sitescout.com', 'smetrics.foxnews.com', 'cdn.districtm.io', 'api.nova.foxnews.com', 'sync.srv.stackadapt.com', 'bam-cell.nr-data.net', 'tg.socdm.com', 'sync.technoratimedia.com', 'feeds-elections.foxnews.com', 'apps.foxnews.com', 'pixel.everesttech.net', 'mabping.chartbeat.net', 'js-sec.indexww.com', 'loadm.exelator.com', 'r.turn.com', 'ping.chartbeat.net', 'odr.mookie1.com', 'bam.nr-data.net', 'www.omnycontent.com', 'sync.adap.tv', 'aswpsdkus.com', 'pixel.invitemedia.com', 'api.foxnews.com', 'rtb.openx.net', 'my.foxnews.com', 'pubmatic-match.dotomi.com', 'load77.exelator.com', 'x.dlx.addthis.com', 'pmp.mxptint.net', 'rcp.c.appier.net', 'sync.adaptv.advertising.com', 'visitor.fiftyt.com', 'cookiex.ngd.yahoo.com', 'dmx.districtm.io', 'simage4.pubmatic.com', 'pixel.onaudience.com', 'bcp.crwdcntrl.net', 'pool.admedo.com', 'sync.extend.tv', 'gocm.c.appier.net', 'sync.resetdigital.co:10001', 'sync.adkernel.com', 'match.taboola.com', 'fcmatch.google.com', 'px.owneriq.net', 'dmx.us-east-12.districtm.io', 'www.foxbusiness.com', 'fcmatch.youtube.com', 'foxnewsplayer-a.akamaihd.net', 'trial-eum-clientnsv4-s.akamaihd.net', 'trial-eum-clienttons-s.akamaihd.net', '79423.analytics.edgekey.net', 'amp.akamaized.net', '36cc2473.akstat.io', 'csm.va.us.criteo.net', 'www.breitbart.com', '247preview.foxnews.com', 'media.breitbart.com', 'scripts.webcontentassessor.com', 'hb.emxdgt.com', 'breitbart-com.videoplayerhub.com', 'breitbartproduction.disqus.com', 'cms.quantserve.com', 'cdn.ampproject.org', 'resources.infolinks.com', '882ace8937590710fa9fbc8094a96472.safeframe.googlesyndication.com', 'trends.revcontent.com', 'router.infolinks.com', 'encrypted-tbn1.gstatic.com', 'ak.sail-horizon.com', 'a.rfihub.com', 'encrypted-tbn0.gstatic.com', 'encrypted-tbn2.gstatic.com', 'encrypted-tbn3.gstatic.com', 'aep.mxptint.net', 'beacon.lynx.cognitivlabs.com', 'rt3043.infolinks.com', 'cti.w55c.net', 'de.tynt.com', 'api.sail-personalize.com', 'ads.playground.xyz', 'ssc-cms.33across.com', 'onetag-sys.com', 's.cpx.to', 'cdn-sec.optmd.com', 'api.intentiq.com', 'cdn.revcontent.com', 'd1bvk193qme2fc.cloudfront.net', 'imasdk.googleapis.com', 'dmp.adform.net', 'ap.lijit.com', 'pixel-eu.rubiconproject.com', 'id5-sync.com', 'js.ad-score.com', 'easylist-downloads.adblockplus.org', 'rubiconcm.digitaleast.mobi', 'ads.avct.cloud', 'images.revcontent.com', 'data.ad-score.com', 'media.revcontent.com', 'r.bidswitch.net', 'd.turn.com', 'um2.eqads.com', 'img.revcontent.com', 'match.adsby.bidtheatre.com', 'a.sportradarserving.com', 'cms-xch-chicago.33across.com', 'acuityplatform.com', 'assets.revcontent.com', 'tracks.momagic.com', 'eu-u.openx.net', 'i.liadm.com', 'cms-xch.33across.com', 'dsp.nrich.ai', 'i6.liadm.com']
# 807
# Opera
# ['autoupdate.geo.opera.com', 'features.opera-api.com', 'exchange.opera.com', 'speeddials.opera.com', 'www.google.com', 'www.bing.com', 'duckduckgo.com', 'search.yahoo.com', 'www.amazon.com', 'www.wikipedia.org', 'sd-suggestions.operacdn.com', 'sd-images.operacdn.com', 'ssl.gstatic.com', 'fonts.gstatic.com', 'www.gstatic.com', 'af.opera.com', 'weather.opera-api.com', 'apis.google.com', 'ogs.google.com', 'adservice.google.com', 'www.youtube.com', 'merchandise.opera-api.com', 'fonts.googleapis.com', 'android.clients.google.com', 'i.ytimg.com', 'googleads.g.doubleclick.net', 'accounts.google.com', 'securepubads.g.doubleclick.net', 'yt3.ggpht.com', 's.ytimg.com', 'pagead2.googlesyndication.com', 'static.doubleclick.net', 'r2---sn-ab5l6nzd.googlevideo.com', 'images-na.ssl-images-amazon.com', 'addons.opera.com', 'm.media-amazon.com', 'fls-na.amazon.com', 'assoc-na.associates-amazon.com', 'unagi-na.amazon.com', 'addons-media.operacdn.com', 'completion.amazon.com', 'd23tl967axkois.cloudfront.net', 'd2in0p32vp1pij.cloudfront.net', 'player.live-video.net', 'usher.ttvnw.net', 'aax-us-east.amazon-adsystem.com', 'unagi.amazon.com', 'player.stats.live-video.net', 'www.yahoo.com', 's.yimg.com', 'aka-cdn.adtechus.com', 'guce.yahoo.com', 'udc.yahoo.com', 'download3.operacdn.com', 'geo.yahoo.com', 'sb.scorecardresearch.com', 'tag.idsync.analytics.yahoo.com', 'us.y.atwola.com', 'opus.analytics.yahoo.com', 'service.idsync.analytics.yahoo.com', 'ads.yahoo.com', 'us-east-1.onemobile.yahoo.com', 'ups.analytics.yahoo.com', 'cdn.cmp.advertising.com', 'cms.analytics.yahoo.com', 'desktop-dna.osp.opera.software', 'www.googletagservices.com', 'cm.g.doubleclick.net', 'tags.bluekai.com', 'www.facebook.com', 'dpm.demdex.net', 'pixel.advertising.com', 'beacon.krxd.net', 'aa.agkn.com', 'b.gemini.yahoo.com', 'us-u.openx.net', 'match.adsrvr.org', 'audex.userreport.com', 'cs.emxdgt.com', 'sync-tm.everesttech.net', 'ib.adnxs.com', 'pixel.rubiconproject.com', 'image8.pubmatic.com', 'bh.contextweb.com', 'pr-bh.ybp.yahoo.com', 'sync.mathtag.com', 'x.bidswitch.net', 'image2.pubmatic.com', 'bsw.digitru.st', 'us-east-sync.bidswitch.net', 'onevideosync.uplynk.com', 'image4.pubmatic.com', 'update.googleapis.com', 'static.xx.fbcdn.net', 'facebook.com', 'cx.atdmt.com', 'www.zoom.us', 'd24cgw3uvb9a9h.cloudfront.net', 'static.ada.support', 'rollout.ada.support', 'www.googletagmanager.com', 'www.google-analytics.com', 'zoom.ada.support', 'zoom.us', 'consent.trustarc.com', 'www.reddit.com', 'www.redditstatic.com', 'preview.redd.it', 'external-preview.redd.it', 'styles.redditmedia.com', 'a.thumbs.redditmedia.com', 'b.thumbs.redditmedia.com', 'c.aaxads.com', 'gql.reddit.com', 'c.amazon-adsystem.com', 'www.redditmedia.com', 'i.redd.it', 'www.aaxdetect.com', 'l3.aaxads.com', 'alb.reddit.com', 'gateway.reddit.com', 'id.rlcdn.com', 'secure.quantserve.com', 'f0abe9047903a33dbd30da7d20d4073c.safeframe.googlesyndication.com', 'tpc.googlesyndication.com', 's.amazon-adsystem.com', 'rules.quantcount.com', 'pixel.quantserve.com', 'www.messenger.com', 'www.myshopify.com', 'scontent-bos3-1.xx.fbcdn.net', 'connect.facebook.net', 'cdn.shopify.com', 'www.ebay.com', 'ir.ebaystatic.com', 'rover.ebay.com', 'i.ebayimg.com', 'srv.main.ebayrtm.com', 'www.office.com', 'cs.ns1p.net', 'ocsrest.ebay.com', 'pages.ebay.com', 's.ns1p.net', 'svcs.ebay.com', 'secureir.ebaystatic.com', 'level3-static.ebaycdn.net', 'pulsar.ebay.com', '5cb8dfb79d8bcafa04cc923d34175dc2.safeframe.googlesyndication.com', 'b.ns1p.net', 'src.ebay-us.com', 'www.microsoft.com', 'statics-marketingsites-eus-ms-com.akamaized.net', 'img-prod-cms-rt-microsoft-com.akamaized.net', 'blobs.officehome.msocdn.com', 'mem.gfx.ms', 'login.live.com', 'web.vortex.data.microsoft.com', 'login.microsoftonline.com', 'browser.pipe.aria.microsoft.com', 'www.netflix.com', 'logincdn.msauth.net', 'c1.microsoft.com', 'c.bing.com', 'codex.nflxext.com', 'assets.nflxext.com', 'ae.nflximg.net', 'ichnaea-web.netflix.com', 'www.googleadservices.com', '4968236.fls.doubleclick.net', 'www.live.com', 'outlook.live.com', 'ow2.res.office365.com', 'az725175.vo.msecnd.net', 'r4.res.office365.com', 'www.instructure.com', 'fast.wistia.com', 'pages.instructure.com', 'cdnjs.cloudflare.com', 'maps.googleapis.com', 'dev.visualwebsiteoptimizer.com', 'www.googleoptimize.com', 'snap.licdn.com', 'static.ads-twitter.com', 'bat.bing.com', 'munchkin.marketo.net', 'd10lpsik1i8c69.cloudfront.net', 'pro.ip-api.com', 'cdn.livechatinc.com', 'stats.g.doubleclick.net', 'settings.luckyorange.net', 't.co', '449-bvj-543.mktoresp.com', 'secure.livechatinc.com', 'px.ads.linkedin.com', 'www.linkedin.com', 'p.adsymptotic.com', 'js-agent.newrelic.com', 'www.twitch.tv', 'analytics.twitter.com', 'bam.nr-data.net', 'embed-fastly.wistia.com', 'embedwistia-a.akamaihd.net', 'distillery.wistia.com', 'pipedream.wistia.com', 'p.twitchcdn.net', 'static.twitchcdn.net', 'fg8vvsvnieiv3ej16jby.litix.io', 'video-edge-b8150b.pdx01.abs.hls.ttvnw.net', 'gql.twitch.tv', 'static-cdn.jtvnw.net', 'pubsub-edge.twitch.tv', 'irc-ws.chat.twitch.tv', 'cdn.krxd.net', 'api.twitch.tv', 'app.link', 'd2v02itv0y9u9t.cloudfront.net', 'cdn-gl.imrworldwide.com', 'api2.branch.io', 'countess.twitch.tv', 'video-weaver.sea01.hls.ttvnw.net', 'consumer.krxd.net', '3bb1423cffef94636be19d4ffc7ca4e3.safeframe.googlesyndication.com', 'video-edge-8b7c38.iad05.abs.hls.ttvnw.net', 'secure-sts-prod.imrworldwide.com', 'js.adsrvr.org', 'match.prod.bidr.io', 'insight.adsrvr.org', 'f8be433c57c697e5c77d53c4fdd31153.redinuid.imrworldwide.com', 'ad.doubleclick.net', 'secure.insightexpressai.com', 'pixel.adsafeprotected.com', 'static.adsafeprotected.com', 'secure-dcr.imrworldwide.com', 'n4q0www2fr2ywao9uyjmzi4dojn5a1603401547.nuid.imrworldwide.com', 'usermatch.krxd.net', 'microsoftmscompoc.tt.omtrdc.net', 'www.chaturbate.com', 'cdnssl.clicktale.net', 'dapadobeproxyql.azurewebsites.net', 'dapadobeproxytest.azurewebsites.net', 'mscom.demdex.net', 'cm.everesttech.net', 'c.clicktale.net', 'ing-district.clicktale.net', 'chaturbate.com', 'idsync.rlcdn.com', 'rtd.tubemogul.com', 'rtd-tm.everesttech.net', 'idpix.media6degrees.com', 'p.rfihub.com', 'ssl-ccstatic.highwebmedia.com', 'roomimg.stream.highwebmedia.com', 'cdn.exoticads.com', 'adserver.exoticads.com', 'content.exoticads.com', 'www.instagram.com', 'www.cnn.com', 'graph.instagram.com', 'www.i.cdn.cnn.com', 'agility.cnn.com', 'cdn.cnn.com', 'amplify.outbrain.com', 'cdn.cookielaw.org', 'cdn.jsdelivr.net', 'api.rlcdn.com', 'cdn3.optimizely.com', 'a125375509.cdn.optimizely.com', 'cdn.adsafeprotected.com', 'cdn.segment.com', 'mid.rkdms.com', 'warnermediagroup-com.videoplayerhub.com', 'tag.bounceexchange.com', 'd2uap9jskdzp2.cloudfront.net', 'static.chartbeat.com', 'www.ugdturner.com', 'as-sec.casalemedia.com', 'dw7nrwnn2bkh1.cloudfront.net', 'tru.am', 'i.clean.gg', 'turner2.demdex.net', 'cdn.boomtrain.com', 'get.s-onetag.com', 'smetrics.cnn.com', 'logx.optimizely.com', 'api.segment.io', 'widgets.tree.com', 'htlb.casalemedia.com', 'bidder.criteo.com', 'fastlane.rubiconproject.com', 'sofia.trustx.org', 'mab.chartbeat.com', 'tr.outbrain.com', 'cdn.ml314.com', 'zion.api.cnn.io', 'acdn.adnxs.com', 'umto.cnn.com', 'people.api.boomtrain.com', 'mrb.upapi.net', 'data.cnn.com', 'assets.bounceexchange.com', 'onetag-geo.s-onetag.com', 'i.cdn.tbs.com', 'i.cdn.tntdrama.com', 'i.cdn.trutv.com', 'www.warnermediaprivacy.com', 'bleacherreport.com', 'www.att.com', 'widgets.outbrain.com', 'static.criteo.net', 'w.usabilla.com', 'ads.celtra.com', 'z.moatads.com', 'beacon.s-onetag.com', 'onsiterecs.api.boomtrain.com', 'cache-ssl.celtra.com', 'eus.rubiconproject.com', 'js-sec.indexww.com', 'pixel.moatads.com', 'tps.doubleverify.com', 'log.outbrainimg.com', 'tcheck.outbrainimg.com', 'secure-us.imrworldwide.com', 'ml314.com', 'widget-pixels.outbrain.com', 'pixel.mtrcs.samba.tv', 'onetag-geo-grouping.s-onetag.com', 'geo-location.s-onetag.com', 's.cdn.turner.com', 'ad-delivery.net', 'odb.outbrain.com', 'track.celtra.com', 'backend.upapi.net', 'mcdp-nydc1.outbrain.com', 'dt.adsafeprotected.com', 'www.adultswim.com', 'www.greatbigstory.com', 'connect-metrics-collector.s-onetag.com', 'signal-metrics-collector-beta.s-onetag.com', 'maxcdn.bootstrapcdn.com', 's2.go-mpulse.net', 'myattlog.att.com', 'dsum-sec.casalemedia.com', 'ssum-sec.casalemedia.com', 'sync.search.spotxchange.com', 's.go-mpulse.net', 'b1sync.zemanta.com', 'sync.outbrain.com', 'cnn.bounceexchange.com', 'c.go-mpulse.net', 'dis.criteo.com', 'events.bouncex.net', 'pippio.com', 'ps.eyeota.net', 'rtb.mfadsrvr.com', 'dsp.adfarm1.adition.com', 'loadus.exelator.com', 'sync-jp.im-apps.net', 'px.powerlinks.com', 'id.geistm.com', '173c5b09.akstat.io', 'pixel-us-east.rubiconproject.com', 'creativecdn.com', 'bttrack.com', 'sync.crwdcntrl.net', 'sync.adotmob.com', 'ams.creativecdn.com', 'token.rubiconproject.com', 'c1.adform.net', 'privacyportal-eu.onetrust.com', 'www.espn.com', 'pixel-sync.sitescout.com', 'cm.eyereturn.com', 'prg.kargo.com', 'cookiex.ngd.yahoo.com', 'ad4m.at', 'loadm.exelator.com', 'crb.kargo.com', 'pixel.tapad.com', 'www.summerhamster.com', 'a.espncdn.com', 'secure.espn.com', 'dcf.espn.com', 'a2.espncdn.com', 'a1.espncdn.com', 'a3.espncdn.com', 'a4.espncdn.com', 'sw88.espn.com', 'site.web.api.espn.com', 'tredir.espn.com', 'espndotcom.tt.omtrdc.net', 'fan.api.espn.com', 'cdn.registerdisney.go.com', 'd.impactradius-event.com', 'broadband.espn.com', 'platform.twitter.com', 'entitlement.auth.adobe.com', 'api-app.espn.com', 'adserver-us.adtech.advertising.com', 'sp.auth.adobe.com', 'onefeed.fan.api.espn.com', '58e895f65000fc07b980e30f1bc0162c.safeframe.googlesyndication.com', 'mb.moatads.com', 'px.moatads.com', 'geo.moatads.com', 'secure.espncdn.com', 's.secure.espncdn.com', '8397396.fls.doubleclick.net', 'vision.fn-pz.com', 'plus.espn.com', 'secure-gl.imrworldwide.com', 'ad.turn.com', 'stags.bluekai.com', 'syndication.twitter.com', 'cdn.unid.go.com', 'unid.go.com', 'fastcast.semfs.engsvc.go.com', 'p72765941-de44-4d35-9008-f04aecf96df2-34-230-72-182.fastcast.semfs.engsvc.go.com:9573', 'secure.adnxs.com', 'pixel-a.sitescout.com', 'id.sharedid.org', 'secure-sdk.imrworldwide.com', 'casale-match.dotomi.com', 'um.simpli.fi', 'cm.adgrx.com', 'fcast.espncdn.com', 'sync.ipredictive.com', '8gbxhqr4ikmdtgimof0sbpjyu9zb81603401643.nuid.imrworldwide.com', 'd.adroll.com', 'pm.w55c.net', 'i.w55c.net', 'dsum.casalemedia.com', 'nmcsync.imrworldwide.com', 'www.zillow.com', 'www.zillowstatic.com', 'collector-pxhyx10rg3.px-cloud.net', 'e.zg-api.com', '4704202.fls.doubleclick.net', 's.pinimg.com', 'www.chase.com', 'pt.ispot.tv', 'bid.g.doubleclick.net', 'pxl.jivox.com', 'sync.jivox.com', 'ct.pinterest.com', 'bcp.crwdcntrl.net', 's.thebrighttag.com', 'static.chasecdn.com', 'secure01b.chase.com', 'midas.chase.com', 'target.chase.com', 'sites.chase.com', 'analytics.chase.com', 'www.etsy.com', 'jpmcbankna.demdex.net', 'dc.ads.linkedin.com', 'rc.rlcdn.com', 'i.etsystatic.com', 'img0.etsystatic.com', '8666735.fls.doubleclick.net', '9910951.fls.doubleclick.net', 'resources.xg4ken.com', 'web.btncdn.com', 'www.dwin1.com', 'trkn.us', 'tags.w55c.net', 'static-exp1.licdn.com', 'platform.linkedin.com', 'www.apple.com', 'lnkd.demdex.net', 'securemvt.apple.com', 'securemetrics.apple.com', 'www.dropbox.com', 'dropbox.com', 'cfl.dropboxstatic.com', 'marketing.dropbox.com', '8166291.fls.doubleclick.net', 'tags.tiqcdn.com', 'snapengage.dropbox.com', 'storage.googleapis.com', 'secure-ds.serving-sys.com', 'b92.yahoo.co.jp', 'tags.srv.stackadapt.com', 'cdn.bizible.com', 'sp.analytics.yahoo.com', 'www.snapengage.com', 'sslwidget.criteo.com', 'gum.criteo.com', 'bs.serving-sys.com', 'cdn.bizibly.com', 'c1.rfihub.net', 'www.adobe.com', 'a.rfihub.com', '20799319p.rfihub.com', 'static.adobelogin.com', 'use.typekit.net', 's7d1.scene7.com', 'geo2.adobe.com', 'assets.adobedtm.com', 'adobeid-na1.services.adobe.com', 'ims-na1.adobelogin.com', 'images-tv.adobe.com', 'geo.adobe.com', 'sstats.adobe.com', 'adobe.tt.omtrdc.net', 'www.nytimes.com', 'geolocation.onetrust.com', 'api.demandbase.com', 'www.everestjs.net', 'servedby.flashtalking.com', 'universal.iperceptions.com', 'pixel.everesttech.net', 'scripts.demandbase.com', 'adobeioruntime.net', 'lasteventf-tm.everesttech.net', 'adobe.demdex.net', 'api.company-target.com', 'segments.company-target.com', 'g1.nyt.com', 'static01.nyt.com', 'samizdat-graphql.nytimes.com', 'als-svc.nytimes.com', 'a.et.nytimes.com', 'news.google.com', 'contextual.media.net', 'rumcdn.geoedge.be', 'nytimes.com', 'a4557867bae3c43943dd31b76756da2d.safeframe.googlesyndication.com', 'hblg.media.net', 'cdneast2-xch.media.net', 'dd.nytimes.com', 'content.api.nytimes.com', 'purr.nytimes.com', 'a.nytimes.com', 'meter-svc.nytimes.com', 'cslogger.media.net', 'a1.nyt.com', 'mwcm.nytimes.com', '5290727.fls.doubleclick.net', 'tags.bkrtx.com', 'pnytimes.chartbeat.net', 'static01.nytimes.com', 'www.aliexpress.com', 'vp.nyt.com', 'play.google.com', 'sc.iasds01.com', 'assets.alicdn.com', 'aeu.alicdn.com', 'ae01.alicdn.com', 'aeis.alicdn.com', 'g.alicdn.com', 'login.aliexpress.ru', 'cdp.aliexpress.com', 'login.tmall.ru', 'acs.aliexpress.com', 'gpsfront.aliexpress.com', 'gj.mmstat.com', 'us.ynuf.aliapp.org', 'cukb48.tdum.alibaba.com', 'fourier.taobao.com', 'campaign.aliexpress.com', 'i.alicdn.com', 'acjs.aliyun.com', 'ald-lamp-us.alicdn.com', 'message.aliexpress.com', 'lighthouse.aliexpress.com', 'retcode-us-west-1.arms.aliyuncs.com', 'img.alicdn.com', 'www.craigslist.org', 'geo.craigslist.org', 'oneid.mmstat.com', 'worcester.craigslist.org', 'ynuf.alipay.com', 'www.okta.com', 'polyfill.io', 'p.typekit.net', 'geoip-js.com', '855-qah-699.mktoresp.com', 'wt1ugse0be.execute-api.us-west-2.amazonaws.com', 'js.driftt.com', 'j.6sc.co', 'cdn.heapanalytics.com', 'js.clearbit.com', 'c.6sc.co', 'jadserve.postrelease.com', 'j.mrpdata.net', 'b.6sc.co', 'web.chtbl.com', 'heapanalytics.com', 'x.clearbit.com', 'tag.demandbase.com', 'site-optimization-api.company-target.com', 'privacyportal.onetrust.com', 'www.walmart.com', 's.adroll.com', 'd.adroll.mgr.consensu.org', 'simage2.pubmatic.com', 'sync.taboola.com', 'eb2.3lift.com', 'i5.walmartimages.com', 'i5.wal.co', 'beacon.walmart.com', 'collector-pxu6b0qd2s.px-cloud.net', 'b.wal.co', 'df830545f14182e60a06c7ec1afea2f6.safeframe.googlesyndication.com', 'tap.walmart.com', '8114842.fls.doubleclick.net', 'a.tribalfusion.com', 'vt.myvisualiq.net', 'tapestry.tapad.com', 't.myvisualiq.net', 'cdn.doubleverify.com', 'www.twitter.com', 'cdn3.doubleverify.com', 'twitter.com', 'tps10200.doubleverify.com', 'abs.twimg.com', 'www.livejasmin.com', 'i.liadm.com', 'pbs.twimg.com', 'api.twitter.com', 'i6.liadm.com', 'staticx4.dditscdn.com', 'staticx2.dditscdn.com', 'staticx1.dditscdn.com', 'staticx3.dditscdn.com', 'imgx0.dditscdn.com', 'imgx1.dditscdn.com', 'imgx3.dditscdn.com', 'jaws.dditscdn.com', 'd31qbv1cthcecs.cloudfront.net', 'static.dditscdn.com', 'analytics.google.com', 'api-gateway.dditsadn.com', 'certify.alexametrics.com', 'ip-109-71-162-131.dditscdn.com', 'dss-relay-109-71-164-57.dditscdn.com', 'www.wellsfargo.com', 'static.hotjar.com', 'script.hotjar.com', 'vars.hotjar.com', 'static.wellsfargo.com', 'www01.wellsfargomedia.com', 'www04.wellsfargomedia.com', 'connect.secure.wellsfargo.com', 'www20.wellsfargomedia.com', 'wellsfargobankna.demdex.net', '2549153.fls.doubleclick.net', 'www.tmall.com', 'cdn.appdynamics.com', 'prod5-eum-appdynamics.wellsfargo.com', 'at.alicdn.com', 'aldh5.tmall.com', 'suggest.taobao.com', 'top-tmm.taobao.com', 'log.mmstat.com', 'gm.mmstat.com', 'ws.mmstat.com', 'ac.mmstat.com', 'www.imgur.com', 'imgur.com', 's.imgur.com', 'quantcast.mgr.consensu.org', 'api.imgur.com', 'api.amplitude.com', 'ced.sascdn.com', 'oa.openxcdn.net', 'imgur.ccgateway.net', 'ced-ns.sascdn.com', 'test.quantcast.mgr.consensu.org', 'tagan.adlightning.com', 'i.imgur.com', 'carbon-cdn.ccgateway.net', 'cdn.ccgateway.net', 'www9.smartadserver.com', 'loadeu.exelator.com', 'analytics.ccgateway.net', 'www.force.com', 'www.salesforce.com', 'c1.sfdcstatic.com', 'a.sfdcstatic.com', 'cdn.optimizely.com', 'a10681260716.cdn.optimizely.com', 'cdn.taboola.com', '2382028.fls.doubleclick.net', 'service.force.com', 'px.steelhousemedia.com', 'c.contentsquare.net', 'trc.taboola.com', 'salesforcecom.demdex.net', 'omtr2.partners.salesforce.com', 'd.agkn.com', 'trc-events.taboola.com', 'www.homedepot.com', 'nexus.ensighten.com', 'assets.homedepot-static.com', 'contentgrid.homedepot-static.com', 'homedepot.demdex.net', 'client.px-cloud.net', 'homedepot.tt.omtrdc.net', 'localization.thdws.com', 'clickstream-killswitch.hd-personalization-prod.gcp.homedepot.com', 'collector-pxj770cp7y.px-cloud.net', 'clickstream-producer.hd-personalization-prod.gcp.homedepot.com', 'zn_42v6draxyafsjmv-homedepot.siteintercept.qualtrics.com', 'cdn.quantummetric.com', 'lptag.liveperson.net', '1ad356638475.cdn4.forter.com', 'siteintercept.qualtrics.com', '6gpwkrxh.micpn.com', 'pixel.mathtag.com', 'fls.doubleclick.net', 'd.turn.com', 'pix.revjet.com', 'swasc.homedepot.com', 'track.securedvisit.com', 'homedepot-sync.quantummetric.com', 
# 'homedepot-app.quantummetric.com', 'cdn9.forter.com', 'cdn0.forter.com', 'track.sv.rkdms.com', 'images.homedepot-static.com', 'mr.homedepot.com', 'pix-us.revjet.com', 'd.btttag.com', 'cdn3.forter.com', 'optimizely-edge.salesforce.com', 'a64b1f6da3a1424aa736ec353566d481-1ad356638475.cdn.forter.com', 'cds.taboola.com', 'su.addthis.com', 'ads.scorecardresearch.com', 'match.sharethrough.com', 'trial-eum-clientnsv4-s.akamaihd.net', 'trial-eum-clienttons-s.akamaihd.net', 'www.imdb.com', '130-215-243-126_s-104-129-67-169_ts-1603401880-clienttons-s.akamaihd.net', 'qll7g7tiqfb2qx4r7cma-p63azq-949199fc1-clientnsv4-s.akamaihd.net', '173c5b05.akstat.io', 'fcmatch.google.com', 'fcmatch.youtube.com', 'ia.media-imdb.com', 's.media-imdb.com', 'www.hulu.com', 'c.evidon.com', 'assetshuluimcom-a.akamaihd.net', 'secure.hulu.com', 'metcon.hulu.com', 'vortex.hulu.com', 'sc-static.net', 'intljs.rmtag.com', 'collector-1564.tvsquared.com', 'tr.snapchat.com', '3797690.fls.doubleclick.net', 'collect.tealiumiq.com', 'datacloud.tealiumiq.com', 'ut.ra.linksynergy.com', 'consent.linksynergy.com', 'nypi.dc-storm.com', 'di.rlcdn.com', 'in.hotjar.com', 'tags.rd.linksynergy.com', 'www.pornhub.com', 'static.trafficjunky.com', 'ci.phncdn.com', 'di.phncdn.com', 'hubt.pornhub.com', 'cdn1d-static-shared.phncdn.com', 'cdn1-smallimg.phncdn.com', 'ads.trafficjunky.net', 'a.adtng.com', 'vz-cdn2.trafficjunky.net', 'hw-cdn2.trafficjunky.net', 'vz-cdn2.adtng.com', 'hw-cdn2.adtng.com', 'www.msn.com', 'static-global-s-msn-com.akamaized.net', 's.aolcdn.com', 'web.vortex.data.msn.com', 'confiant.msn.com', 'c.msn.com', 'at.atwola.com', 'arc.msn.com', 'msn.lockerdome.com', 'adserver.adtech.advertising.com', 'web.ssp.yahoo.com', 'prod-m-node-1113.ssp.yahoo.com', 'protected-by.clarium.io', 'aktrack.pubmatic.com', 's0.2mdn.net', 'ads.pubmatic.com', 'cms.quantserve.com', 'cs.media.net', 'sync.1rx.io', 'ums.acuityplatform.com', 'srtb.msn.com', 'r.bing.com', 'choices.truste.com', 'cdn1.lockerdomecdn.com', 'www.bizographics.com', 'ib.3lift.com', 'hbx.media.net', 'cm.mgid.com', 'visitor.omnitagjs.com', 'img.img-taboola.com', 'zem.outbrainimg.com', 'api.taboola.com', 'b1-nydc1.zemanta.com', 'b1t-nydc1.zemanta.com', 'stas.outbrain.com', 'googleads4.g.doubleclick.net', 'ade.googlesyndication.com', 'cvision.media.net', 'image6.pubmatic.com', 'pubmatic-match.dotomi.com', 'code.createjs.com', 'simage4.pubmatic.com', 'rtb-csync.smartadserver.com', 'rtb.gumgum.com', 'px.owneriq.net', 'pmp.mxptint.net', 'sync.technoratimedia.com', 'cs.lkqd.net', 'choices.trustarc.com', 'g.bing.com', 'fonts.google.com', 'www.indeed.com', 'd3hbwax96mbv6t.cloudfront.net', 'd3fw5vlhllyvee.cloudfront.net', 'autocomplete.indeed.com', 't.indeed.com', 'cdn.ravenjs.com', 'pxl.indeed.com', 'secure.indeed.com', 'www.foxnews.com', 'static.foxnews.com', 'global.fncstatic.com', 'a57.foxnews.com', 'omny.fm', 'js.taplytics.com', 'webcontentassessor.global.ssl.fastly.net', '8980432.fls.doubleclick.net', 'assets.omny.fm', 'cdn.raygun.io', 'contributor.google.com', 'foxnews.demdex.net', 'ajax.googleapis.com', 'fundingchoicesmessages.google.com', 'smetrics.foxnews.com', 'hbopenbid.pubmatic.com', 'readmo.yahoo.com', 'foxnews-d.openx.net', 'www.omnycontent.com', 'feeds-elections.foxnews.com', 'api.nova.foxnews.com', '9252a1372a03b812f48b2b05ce1974bd.safeframe.googlesyndication.com', 'ping.chartbeat.net', 'mabping.chartbeat.net', 'cdn.ampproject.org', 'csi.gstatic.com', 'aswpsdkus.com', 'bam-cell.nr-data.net', 'apps.foxnews.com', 'my.foxnews.com', 'api.foxnews.com', 'www.foxbusiness.com', '17d09915.akstat.io', 'foxnewsplayer-a.akamaihd.net', '79423.analytics.edgekey.net', 'ma1498-r.analytics.edgekey.net', 'amp.akamaized.net', 'public.media.foxnews.com', '247preview.foxnews.com', 'pixel.invitemedia.com', 'sync.adap.tv', 'x.dlx.addthis.com', 'r.turn.com', 'sync.adaptv.advertising.com', 'load77.exelator.com', 'pix.impdesk.com', 'tr.blismedia.com', 'rbp.mxptint.net', 'sync.intentiq.com', 'nep.advangelists.com', 'beacon.lynx.cognitivlabs.com', 'match.deepintent.com', 'sync1.intentiq.com', 'gocm.c.appier.net', 'match.taboola.com', 'ads.playground.xyz', 'rtb.adentifi.com', 'content.quantcount.com', 'a1510.casalemedia.com', 'pixel.quantcount.com', 'exch.quantserve.com', 'tracking.emerse.com', 'ads.yieldmo.com', 'match.360yield.com', 'torque.admission.net', 'da.admission.net', 'www.breitbart.com', 'cdn.admission.net', 'gm.demdex.net', 'c.betrad.com', 'media.admission.net', 'scripts.webcontentassessor.com', 'media.breitbart.com', 'hb.emxdgt.com', 'breitbartproduction.disqus.com', 'certify-js.alexametrics.com', 'd7a5d2b33224328415305d77cacd472e.safeframe.googlesyndication.com', 'trends.revcontent.com', 'ak.sail-horizon.com', 'partner.googleadservices.com', 'resources.infolinks.com', 'api.sail-personalize.com', 'd1bvk193qme2fc.cloudfront.net', 'router.infolinks.com', 'cdn.revcontent.com', 'js.ad-score.com', 'rt3045.infolinks.com', 'images.revcontent.com', 'data.ad-score.com', 'media.revcontent.com', 'imasdk.googleapis.com', 'img.revcontent.com', 'rtb.openx.net', 'encrypted-tbn3.gstatic.com', 'encrypted-tbn1.gstatic.com', 'dclk-match.dotomi.com', 'ssbsync.smartadserver.com', 'c.eu1.dyntrk.com', 'sync.extend.tv', 'sync.go.sonobi.com', 'secure-assets.rubiconproject.com', 'de.tynt.com', 'onetag-sys.com', 'ap.lijit.com', 'assets.revcontent.com', 'ssc-cms.33across.com', 's.cpx.to', 'cti.w55c.net', 'id.knsso.com', 'rubiconcm.digitaleast.mobi', 'sync.srv.stackadapt.com', 'ads.stickyadstv.com', 'gu.dyntrk.com', 'cm.smadex.com', 'cms-xch-chicago.33across.com', 'dmp.adform.net', 'pixel-eu.rubiconproject.com', 'sync.bfmio.com']
# 950

# Number of unique domains that set a cookie - adBlock
# Brave
# Chrome
# Edge
# FireFox
# Opera

# Number of unique domains that at least one object is retrieved - abBlock
# Brave
# Chrome
# Edge
# FireFox
# Opera

# captchas (?) videos turnoff extensions
# yahoo - captchas on login
# reddit - front page click stories
# facebook - request couldnt be processed
# zoom - signup no work
# myshopify - wont login (enable js)
# twitch - just wont load at all haha
# twitter - goes to legacy because of no js
# 