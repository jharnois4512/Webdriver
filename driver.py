import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver import Edge
# from selenium.webdriver.edge.options import Options

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
        opts = Options()
        if(1 in input):
            opts.add_extension("adblock.crx")
        if(2 in input):
            opts.add_extension("adblockPlus.crx")
        if(3 in input):
            opts.add_extension("disconnect.crx")
        if(4 in input):
            opts.add_extension("duckduckgoEss.crx")
        if(5 in input):
            opts.add_extension("ghostery.crx")
        if(6 in input):
            opts.add_extension("privBadger.crx")
        if(7 in input):
            opts.add_extension("ublock.crx")  
        driver = webdriver.Chrome(options=opts)
        # driver.close()
        # driver.switch_to_window(driver.window_handles[0])
        for site in sites:
            driver.get(site)
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
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        for site in sites:
            driver.get(site)        
        driver.quit()

    elif("e" in input):
        opts = EdgeOptions()
        print(str(opts))
        opts.use_chromium = True
        opts.add_extension("adblock.crx")
        driver = Edge(opts)
        driver.quit()

    # elif("i" in input):
    #     driver.quit()

__main__(["e"])