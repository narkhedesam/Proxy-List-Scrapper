# Proxy-List-Scrapper 
#### [demo live example using javascript](https://narkhedesam.github.io/Proxy-List-Scrapper)
<p align="center">
    <img width="460" height="300" src="https://raw.githubusercontent.com/narkhedesam/Proxy-List-Scrapper/master/_Proxy-List-Scrapper%20logo.jpg">
</p>
<p align="center">
    <a href="https://paypal.me/sameernarkhede/250">
        <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="paypal" />
    </a>
    <img src="https://img.shields.io/github/license/narkhedesam/Proxy-List-Scrapper" alt="Proxy-List-Scrapper licence" />
    <img src="https://img.shields.io/github/forks/narkhedesam/Proxy-List-Scrapper" alt="Proxy-List-Scrapper forks" />
    <img src="https://img.shields.io/github/stars/narkhedesam/Proxy-List-Scrapper" alt="Proxy-List-Scrapper stars" />
    <img src="https://img.shields.io/github/issues/narkhedesam/Proxy-List-Scrapper" alt="Proxy-List-Scrapper issues" />
    <img src="https://img.shields.io/github/issues-pr/narkhedesam/Proxy-List-Scrapper" alt="Proxy-List-Scrapper pull-requests" />
</p>
<br/><br/>
Proxy List Scrapper from various websites. 
They gives the free proxies for temporary use.


## Web_Scrapper Module <a href="https://github.com/narkhedesam/Proxy-List-Scrapper/blob/master/Web_Scrapper/README.md">here</a>
Web Scrapper is proxy web scraper using proxy rotating api https://scrape.do <br/>
 you can check official documentation from <a href="https://docs.scrape.do/">here</a>
 
<h5>You can send request to any webpages with proxy gateway & web api provided by scrape.do</h5>
<br/><br/>
## How to use Proxy List Scrapper
You can clone this project from github. or use<br/>

    pip install Proxy-List-Scrapper
 
Make sure you have installed the requests and urllib3 in python<br/>

in import add<br/>
    
    from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

After that simply create an object of Scrapper class as "scrapper"<br/>

    scrapper = Scrapper(category=Category, print_err_trace=False)

Here Your need to specify category defined as below:<br/>

    'SSL': 'https://www.sslproxies.org/',
    'GOOGLE': 'https://www.google-proxy.net/',
    'ANANY': 'https://free-proxy-list.net/anonymous-proxy.html',
    'UK': 'https://free-proxy-list.net/uk-proxy.html',
    'US': 'https://www.us-proxy.org/',
    'NEW': 'https://free-proxy-list.net/',
    'SPYS.ME': 'http://spys.me/proxy.txt',
    'proxyscrape': 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
    'ALL': 'ALL'

These are all categories.<br/>
After you have to call a function named "getProxies"<br/>

    # Get ALL Proxies According to your Choice
    data = scrapper.getProxies()

the data will be returned by the above function the data is having the response data of function.<br/>
in data having proxies,len,category
 - @proxies is the list of Proxy Class which has actual proxy.<br/>
 - @len is the count of total proxies in @proxies.<br/>
 - @category is the category of proxies defined above. <br/> 
<br/>


## You can handle the response data as below


    # Print These Scrapped Proxies
    print("Scrapped Proxies:")
    for item in data.proxies:
        print('{}:{}'.format(item.ip, item.port))

    # Print the size of proxies scrapped
    print("Total Proxies")
    print(data.len)

    # Print the Category of proxy from which you scrapped
    print("Category of the Proxy")
    print(data.category)
  
## Author 
Sameer Narkhede <br/>
Profile : https://github.com/narkhedesam <br/>
Website : https://narkhedesam.github.io/ 

### Thanks for giving free proxies
 - https://www.sslproxies.org/
 - https://www.google-proxy.net/
 - https://free-proxy-list.net/anonymous-proxy.html
 - https://free-proxy-list.net/uk-proxy.html
 - https://www.us-proxy.org/
 - https://free-proxy-list.net/
 - http://spys.me/proxy.txt
 - https://proxyscrape.com/
<br/><br/>


## Screenshot is added


![Screenshot](https://raw.githubusercontent.com/narkhedesam/Proxy-List-Scrapper/master/Screenshot.png)


## Donation

If this project help you reduce time to develop, you can give me a cup of coffee :relaxed: 
<br/>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/sameernarkhede/250)

 
