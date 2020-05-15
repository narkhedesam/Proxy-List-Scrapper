# Proxy-List-Scrapper
Proxy List Scrapper from various websites. 
They gives the free proxies for temporary use.

## How to use
Just Download the code and place in your project.<br/>
 
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

    # Get ALl Proxies According to your Choice
    data = scrapper.getProxies()

the data will be returned by the above function the data is having the response data of function.<br/>
in data having proxies,len,category
 - @proxies is the list of Proxy Class which has actual proxy.<br/>
 - @len is the count of total proxies in @proxies.<br/>
 - @category is the category of proxies defined above. <br/> 
<br/>
#### You can handle the response data as below


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
  

#### Thanks for giving free proxies we all are thankful
 - https://www.sslproxies.org/
 - https://www.google-proxy.net/
 - https://free-proxy-list.net/anonymous-proxy.html
 - https://free-proxy-list.net/uk-proxy.html
 - https://www.us-proxy.org/
 - https://free-proxy-list.net/
 <br/><br/>
 - http://spys.me/proxy.txt