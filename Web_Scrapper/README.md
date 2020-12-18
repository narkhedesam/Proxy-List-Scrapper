# Web_Scrapper Module
<a href="https://paypal.me/sameernarkhede/250">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="paypal">
</a>
<br/><br/>Web Scrapper is proxy web scraper using proxy rotating api https://scrape.do <br/>
 you can check official documentation from <a href="https://docs.scrape.do/">here</a>
 
<h5>You can send request to any webpages with proxy gateway & web api provided by scrape.do</h5>
 
## usage of Scrape.do API handler 

initialize web scrapper object
    
    # create an web scrapper object
    web_scrapper = Web_Scrapper()
    
set the api token to web_scrapper    
    
    # set the scrape.do api key
    web_scrapper.set_scrape_do_config(api_token=API_TOKEN)
    
Get Scrape.do account statistics
    
    # Get Scrape.do account statistics
    resp = web_scrapper.scrape_do_acc_stat()
    print("Response Type " + type(resp))
    print(resp)
    
get response from scrape.do api
    
    resp = web_scrapper.scrape_do(url_to_scrape='https://docs.scrape.do/', method="GET", payload={}, headers={},
                                  render=False, super_proxies=False, geo_code=None)
    print(resp)
 
 
## Author 
<b>Sameer Narkhede</b> <br/>
<p align="left">
  <a href="https://github.com/narkhedesam" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="https://github.com/narkhedesam" height="20" width="20" />
  </a>
  <a href="https://narkhedesam.com/" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/googlechrome.svg" alt="https://narkhedesam.com/" height="20" width="20" />
  </a>
  <a href="https://www.linkedin.com/in/sameer-narkhede/" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="https://www.linkedin.com/in/sameer-narkhede/" height="20" width="20" />
  </a>
  <a href="https://www.facebook.com/narkhedesam" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="https://www.facebook.com/narkhedesam" height="20" width="20" />
  </a>
  <a href="https://www.instagram.com/sam_narkhede/" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="https://www.instagram.com/sam_narkhede/" height="20" width="20" />
  </a>
  <a href="https://t.me/narkhedesam" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/telegram.svg" alt="https://t.me/narkhedesam" height="20" width="20" />
  </a>

</p>

<h5>special thanks to <b>Batuhan Özyön</b> - https://github.com/bynf </h5>
 
 
## Screenshot
![Screenshot](https://raw.githubusercontent.com/narkhedesam/Proxy-List-Scrapper/master/Web_Scrapper/web_scrapper.png)

 
## Donation

If this project help you reduce time to develop, you can give me a cup of coffee :relaxed: 
<br/>
<a href="https://paypal.me/sameernarkhede/250">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="paypal">
</a>