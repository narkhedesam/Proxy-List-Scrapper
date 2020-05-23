# Proxy-List-Scrapper
<p align="center">
    <img width="460" height="300" src="https://raw.githubusercontent.com/narkhedesam/Proxy-List-Scrapper/master/_Proxy-List-Scrapper%20logo.jpg">
</p>

[![paypal](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/sameernarkhede/250)

<br/><br/>
Proxy List Scrapper from various websites. 
They gives the free proxies for temporary use.

## How to use
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

### Thanks for giving free proxies we all are thankful


 - https://www.sslproxies.org/
 - https://www.google-proxy.net/
 - https://free-proxy-list.net/anonymous-proxy.html
 - https://free-proxy-list.net/uk-proxy.html
 - https://www.us-proxy.org/
 - https://free-proxy-list.net/
 - http://spys.me/proxy.txt
<br/><br/>


## Screenshot is added


![Screenshot](https://raw.githubusercontent.com/narkhedesam/Proxy-List-Scrapper/master/Screenshot.png)


## Donation

If this project help you reduce time to develop, you can give me a cup of coffee :relaxed: 
<br/>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/sameernarkhede/250)

 