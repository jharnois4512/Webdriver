const webdriver = require('selenium-webdriver')
const chrome = require('selenium-webdriver/chrome')
const fire = require('selenium-webdriver/firefox')
const edge = require('selenium-webdriver/edge')
const ie = require('selenium-webdriver/ie')
const proxy = require('selenium-webdriver/proxy')
const proxyAddr = "127.0.0.1:8888"
const fs = require('fs')

/* used for encoding crx files for Chrome extensions */
function encode(file) {
  var stream = fs.readFileSync(file);
  return new Buffer.from(stream).toString('base64');
}

function readIn(file){
  return new Buffer.from(fs.readFileSync(file)).toString().split("\r\n")
}

async function webDrive(input) {
  var driver
  // var act = driver.actions();
  // await act.sendKeys(webdriver.Key.CONTROL + "t").sendKeys("cnn").perform();
  try{
    if(input.includes("c")){
      var opts = new chrome.Options()
      if(input.includes(1)){
        opts.addExtensions(encode("adblock.crx"))
      }
      if(input.includes(2)){
        opts.addExtensions(encode("privBadger.crx"))
      }
      if(input.includes(3)){
        opts.addExtensions(encode("ublock.crx"))
      }
      if(input.includes(4)){
        opts.addExtensions(encode("ghostery.crx"))
      }
      if(input.includes(5)){
        opts.addExtensions(encode("adblockPlus.crx"))
      }
      if(input.includes(6)){
        opts.addExtensions(encode("disconnect.crx"))
      }
      if(input.includes(7)){
        opts.addExtensions(encode("duckduckgoEss.crx"))
      }
      driver = new webdriver.Builder()
                  .withCapabilities(webdriver.Capabilities.chrome())
                  .setChromeOptions(opts)
                  .setProxy(proxy.manual({https: proxyAddr}))
                  .build();
    }
    if(input.includes("f")){
      var fireCap = new webdriver.Capabilities()
      var fireOpts = new fire.Options()
      if(input.includes(1)){
        fireOpts.addExtensions("adblock.crx")
      }
      if(input.includes(2)){
        fireOpts.addExtensions("privBadger.crx")
      }
      if(input.includes(3)){
        fireOpts.addExtensions("ublock.crx")
      }
      if(input.includes(4)){
        fireOpts.addExtensions("ghostery.crx")
      }
      if(input.includes(5)){
        fireOpts.addExtensions("adblockPlus.crx")
      }
      if(input.includes(6)){
        fireOpts.addExtensions("disconnect.crx")
      }
      if(input.includes(7)){
        fireOpts.addExtensions("duckduckgoEss.crx")
      }
      fireCap.setAcceptInsecureCerts(true)
      driver = new webdriver.Builder()
                  .withCapabilities(fireCap)
                  .setFirefoxOptions(fireOpts)
                  .forBrowser("firefox")
                  .setProxy(proxy.manual({https: proxyAddr}))
                  .setFirefoxOptions(fireOpts)
                  .build()
    }
    if(input.includes("e")){
      var edgeOptions = new edge.Options()
      if(input.includes(1)){
        opts.addExtensions(encode("adblock.crx"))
      }
      if(input.includes(2)){
        opts.addExtensions(encode("privBadger.crx"))
      }
      if(input.includes(3)){
        opts.addExtensions(encode("ublock.crx"))
      }
      if(input.includes(4)){
        opts.addExtensions(encode("ghostery.crx"))
      }
      if(input.includes(5)){
        opts.addExtensions(encode("adblockPlus.crx"))
      }
      if(input.includes(6)){
        opts.addExtensions(encode("disconnect.crx"))
      }
      if(input.includes(7)){
        opts.addExtensions(encode("duckduckgoEss.crx"))
      }
      driver = new webdriver.Builder()
                  .forBrowser("MicrosoftEdge")
                  .setEdgeOptions(edgeOptions)
                  .setProxy(proxy.manual({https: proxyAddr}))
                  .build()
    }
    if(input.includes("i")){
      driver = new webdriver.Builder()
      .forBrowser("ie")
      .setProxy(proxy.manual({https: proxyAddr}))
      .build()
      ;(await driver).manage().setTimeouts({implicit: 90})
    }
    /* sites to start */
    var sites = readIn("topSites.txt")
    for(var i = 0; i < sites.length; i++){
      await driver.get(sites[i])
    }
    (await driver).close()
    ;(await driver).quit()
  }
  catch(e){
    console.log(e)
  }
}

webDrive(["c", 2])

