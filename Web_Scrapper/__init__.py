"""
    Date: 29-08-2020
    Created by Sameer Narkhede
    Project : Proxy-List-Scrapper
    Module : Web_Scrapper
"""
import traceback

import requests


class ScrapperException(BaseException):
    pass


class Web_Scrapper:
    """
    Web Scrapper is proxy web scraper using proxy rotating api https://scrape.do
    """

    def __init__(self, print_err_trace=True):
        self.scrape_do_api_token = None
        self.print_trace = print_err_trace

    def set_scrape_do_config(self, api_token=None):
        """
        set scrape.do api token you can find this token from https://scrape.do/dashboard this needs login.
        :param api_token:
        :return:
        """

        self.scrape_do_api_token = api_token

    def scrape_do_acc_stat(self):
        """
        returns the statestics of account
        :return: Dictionary of statistics
        """
        response = requests.get("http://api.scrape.do/info?token=" + self.scrape_do_api_token)

        return response.json()

    def scrape_do(self, url_to_scrape, method="GET", payload=None, headers=None, render=False, super_proxies=False,
                  geo_code=None):
        """
        Best Rotating Proxy & Scraping API Alternative https://scrape.do/ api handler

        :param url_to_scrape: String the url user needs to scrape. Ex. 'https://httpbin.org/get'

        :param method: String method for the url request. Ex. ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
                        ``PATCH``, or ``DELETE``

        :param payload: (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the

        :param headers: (optional) Dictionary of HTTP Headers to send with the request

        :param render: (optional) Boolean - To use Javascript, all you need to do is setting render parameter to true
                        ** Beware that you need a business plan to use this feature!

        :param super_proxies:(optional) Boolean - To use Super Proxies, all you need to do is setting super parameter
                            to true
                        ** Beware that you need a business plan to use this feature!
        :param geo_code:

        :return: response of web scrapper

        """
        try:

            # check if there is token is configured
            if self.scrape_do_api_token:
                base_url = f"http://api.scrape.do"
                params = {'token': self.scrape_do_api_token}
                if headers is None:
                    headers = {}
                if payload is None:
                    payload = {}

                if headers is not None and headers is not {}:
                    params['customHeaders'] = 'true'

                params['url'] = url_to_scrape

                if render:
                    params['render'] = 'true' if render else 'false'

                if super_proxies:
                    params['super'] = 'true' if super_proxies else 'false'

                if geo_code:
                    geocodes = ['us', 'gb', 'ca', 'tr', 'cn', 'ru', 'se', 'de', 'fr', 'es', 'br']

                    if geo_code not in geocodes:
                        raise ScrapperException("Geo-Code is not valid. please provide geo-code in " + str(geocodes))

                    params['geo_code'] = geo_code

                methods = ["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
                if method not in methods:
                    raise ScrapperException("method is not valid. please provide method in " + str(methods))

                response = requests.request(method, base_url, params=params, headers=headers, data=payload)

                print("status_code:" + str(response.status_code))

                if response.status_code == 200:
                    return response.text.encode('utf8')

                elif response.status_code == 404:
                    raise ScrapperException("Target url not found :: Pass valid URL")

                elif response.status_code == 429:
                    raise ScrapperException("You are sending too many concurrent request :: Please upgrade your plan "
                                            "or contact with sale.")

                elif response.status_code == 401:
                    raise ScrapperException("You have not credit :: Please upgrade your plan or contact with sale.")

                elif response.status_code == 502:
                    raise ScrapperException("Gateway Error :: Please retry and check response. If you live constantly,"
                                            " contact support@scrape.do")

            else:
                raise ScrapperException("api-token is not configured")

        except ConnectionError:
            print('Connection Error in Web Scrapping')
            if self.print_trace:
                print(traceback.format_exc())
            return ""

        except ScrapperException as e:
            print(str(e))
            if self.print_trace:
                print(traceback.format_exc())
            return ""


if __name__ == '__main__':

    API_TOKEN = "XV7blMOWPkGto0q8oyQUuwChdpr4251kggxdpVjfe2Ug"

    # create an web scrapper object
    web_scrapper = Web_Scrapper()

    # set the scrape.do api key
    web_scrapper.set_scrape_do_config(api_token=API_TOKEN)

    # Get Scrape.do account statistics
    resp = web_scrapper.scrape_do_acc_stat()
    print("Response Type " + str(type(resp)))
    print(resp)

    resp = web_scrapper.scrape_do(url_to_scrape='https://docs.scrape.do/', method="GET", payload={}, headers={},
                                  render=False, super_proxies=False, geo_code=None)

    print(resp)
