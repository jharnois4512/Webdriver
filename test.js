const webdriver = require('selenium-webdriver')
const chrome = require('selenium-webdriver/chrome')
const fire = require('selenium-webdriver/firefox')
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
    var opts = new chrome.Options()
    opts.addExtensions(encode("adblock.crx"), encode("ublock.crx"), encode("privBadger.crx"), encode("ghostery.crx"))
    var driver = new webdriver.Builder()
                .withCapabilities(webdriver.Capabilities.chrome())
                // .setChromeOptions(opts)
                .setProxy(proxy.manual({https: proxyAddr}))
                .build()
    /* Firefox driver */
    // var fireCap = new webdriver.Capabilities()
    // var fireOpts = new fire.Options()
    // fireOpts.addExtensions("adblock.xpi", "ublock.xpi", "privBadger.xpi", "ghostery.xpi")
    // fireCap.setAcceptInsecureCerts(true)
    // var driver = new webdriver.Builder()
    //             .withCapabilities(fireCap)
    //             .setFirefoxOptions(fireOpts)
    //             .forBrowser("firefox")
    //             .setProxy(proxy.manual({https: proxyAddr}))
    //             // .setFirefoxOptions(fireOpts)
    //             .build()

    /* Internet Explorer driver */
    // var driver = new webdriver.Builder()
    //             .forBrowser("internet explorer")
    //             .build()

    /* Opera Driver */
    
    /* sites to start */
    var sites = readIn("topSites.txt")
    for(var i = 0; i < sites.length; i++){
      await driver.get(sites[i])
    }
  }
  catch(e){
    console.log(e)
  }
}
webDrive()
