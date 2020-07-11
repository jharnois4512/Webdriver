# README written for project WebDriver
# Written by Jeffrey Harnois

## Purpose:

The purpose of this project is to be able to set up an enviornment to allow for automatic webdriving with chrome or firefox through a Burp Suite proxy set up to record all traffic

## To run:

```
npm start
```

Running ```npm start``` will start up the Selenium web browser. Before you do this you will need to start a Burp Suite proxy. [Visit this site to download Burp Suite](https://portswigger.net/burp/communitydownload). The free version is all you will need to make this project work.

## Burp Configs

To set up Burp Suite to run as a proxy, you will first need to install the SSL Certs. [Follow this link for instructions](https://portswigger.net/support/installing-burp-suites-ca-certificate-in-your-browser). After you completed this, you then will need to set up the proxy. Make a new project and navigate over to the ```Proxy``` tab. You will find the button to generate CA Certs in the ```Options``` tab discussed below.

On the ```Intercept``` tab, if your interecptor is running, click it once. You will see it change to ```Intercept is off```. If it is already set to this, you may skip this step. 

Next, navigate over to the ```Options``` tab. Here you will find the Edit the ```Proxy Listners```. The ```Options``` tab is where you will also find the button mentioned for generating CA Certs. Add in a new interface of ```127.0.0.1:8080```. You can run the server on a different port if you wish, you will just have to modify the port in ```test.js```. 

Lastly, make sure that you check the ```running``` box to start the proxy.

When you are done with these steps, navigate to the ```HTTP history``` tab and run the program. 