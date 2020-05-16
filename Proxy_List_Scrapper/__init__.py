"""
    Date: 15-05-2020
    Created by Sameer Narkhede
    Project : Proxy-List-Scrapper
"""

import sys
import traceback
from re import findall

import requests
from requests.exceptions import ConnectionError


class ScrapperException(BaseException):
    pass


class Proxies(object):
    """
       Proxies is the response data type of getProxies function
    """
    def __init__(self, proxies, category):
        """
        Initialize the proxies class
        :param proxies: is the list of proxies.
        :param category: is the category for proxies.
        """
        self.proxies = proxies
        self.len = len(proxies)
        self.category = category


class Proxy(object):
    """
        Proxy is the class for proxy.
    """
    def __init__(self, ip, port):
        """
        Initialization of the proxy class
        :param ip: ip address of proxy
        :param port: port of proxy
        """
        self.ip = ip
        self.port = port


class Scrapper:
    """
    Scrapper class is use to scrape the proxies from various websites.
    """
    def __init__(self, category='ssl', print_err_trace=True):
        """
        Initialization of scrapper class
        :param category: Category of proxy to scrape.
        :param print_err_trace: (True or False) are you required the stack trace for error's if they occured in the program
        """
        # init with Empty Proxy List
        self.proxies = []
        self.category = category
        self.Categories = {'SSL': 'https://www.sslproxies.org/',
                           'GOOGLE': 'https://www.google-proxy.net/',
                           'ANANY': 'https://free-proxy-list.net/anonymous-proxy.html',
                           'UK': 'https://free-proxy-list.net/uk-proxy.html',
                           'US': 'https://www.us-proxy.org/',
                           'NEW': 'https://free-proxy-list.net/',
                           'SPYS.ME': 'http://spys.me/proxy.txt',
                           'ALL': 'ALL'
                           }
        self.print_trace = print_err_trace

    def getProxies(self):
        """
        getProxies() gives the proxies scrapped from websites.
        :return: the object of proxies class
        """
        if self.Categories[self.category] == 'ALL':
            for Cat in self.Categories:
                # Skip iteration for ALL category
                if Cat == 'ALL':
                    continue

                self.category = Cat
                self.proxies += self._get()
            self.category = 'ALL'
            self.filter_proxies_remove_duplicates()
        else:
            self.proxies = self._get()

        self.proxies = [Proxy(proxy.split(':')[0], proxy.split(':')[1]) for proxy in self.proxies]
        return Proxies(proxies=self.proxies, category=self.category)

    def _get(self):
        """
        _get() is the actual scrapper to scrape proxies by REGEX.
        :return: returns the list of proxies according to the category of proxies
        """
        try:
            r = requests.get(url=self.Categories[self.category])
            if self.category == 'SPYS.ME':
                self.proxies = findall(pattern=r'\d+\.\d+\.\d+\.\d+:\d+', string=r.text)
            else:
                matches = findall(pattern=r'\d+\.\d+\.\d+\.\d+</td><td>\d+', string=r.text)
                self.proxies = [m.replace('</td><td>', ':') for m in matches]
            return self.proxies
        except ConnectionError:
            print('Connection Error in getting SSL Proxies')
            if self.print_trace:
                print(traceback.format_exc())
            return []

    def filter_proxies_remove_duplicates(self):
        """
        filter_proxies_remove_duplicates() is the filter for the proxy list. To get the unique proxies it just get
        the LIST of proxies from self object convert it to SET and then convert to LIST.

        :return: Update the UNIQUE LIST of proxies.
        """
        self.proxies = list(set(self.proxies))


__author__ = "Sameer Narkhede"
__copyright__ = "Copyright (C) 2020 Sameer Narkhede"
__license__ = "MIT LICENCE"
__version__ = "0.1.0"

if __name__ == "__main__":
    # By default set ALL for the parameter to get ALL Proxies
    Category = 'ALL'

    try:
        # get an parameter from command line
        Category = sys.argv[1]

    except IndexError:
        print('You didn\'t Specify parameter for script')

    # Initialize the Scrapper
    scrapper = Scrapper(category=Category, print_err_trace=False)

    # Get ALl Proxies According to your Choice
    data = scrapper.getProxies()

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
