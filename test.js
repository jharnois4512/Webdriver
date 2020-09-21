const webdriver = require('selenium-webdriver')
const chrome = require('selenium-webdriver/chrome')
const fire = require('selenium-webdriver/firefox')
const edge = require('selenium-webdriver/edge')
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

async function webDrive() {
  /* Chrome driver */
  try{
    // var opts = new chrome.Options()
    // opts.addExtensions(encode("adblock.crx"), encode("ublock.crx"), encode("privBadger.crx"), encode("ghostery.crx"), encode("adblockPlus.crx"), encode("disconnect.crx"), encode("duckduckgoEss.crx"))
    // var driver = new webdriver.Builder()
    //             .withCapabilities(webdriver.Capabilities.chrome())
    //             .setChromeOptions(opts)
    //             .setProxy(proxy.manual({https: proxyAddr}))
    //             .build();
    // driver.findElement({css:"body"}).sendKeys('{CTRL}t')
    // await driver.sendKeys('{CTRL} + t')
    /* Firefox driver */
    // var fireCap = new webdriver.Capabilities()
    // var fireOpts = new fire.Options()
    // fireOpts.addExtensions("adblock.xpi", "ublock.xpi", "privBadger.xpi", "ghostery.xpi", "adblockPlus.xpi", "duckduckgoEss.xpi")
    // fireCap.setAcceptInsecureCerts(true)
    // var driver = new webdriver.Builder()
    //             .withCapabilities(fireCap)
    //             .setFirefoxOptions(fireOpts)
    //             .forBrowser("firefox")
    //             .setProxy(proxy.manual({https: proxyAddr}))
    //             // .setFirefoxOptions(fireOpts)
    //             .build()

    /* Edge driver */
    var edgeOptions = new edge.Options()
    edgeOptions.addExtensions(encode("adblock.crx"), encode("ublock.crx"), encode("privBadger.crx"), encode("ghostery.crx"), encode("adblockPlus.crx"), encode("disconnect.crx"), encode("duckduckgoEss.crx"))
    var driver = new webdriver.Builder()
                .forBrowser("MicrosoftEdge")
                .setEdgeOptions(edgeOptions)
                .setProxy(proxy.manual({https: proxyAddr}))
                .build()

    ;(await driver).get("https://www.google.com")
    /* Opera Driver */
    
    /* sites to start */
    // var sites = readIn("topSites.txt")
    // for(var i = 0; i < sites.length; i++){
    //   await driver.get(sites[i])
    // }
  }
  catch(e){
    console.log(e)
  }
}
webDrive()
