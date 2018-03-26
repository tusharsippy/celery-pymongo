#
# This python class is used to get page dump using python requests library
import json
import random
import socket
import ssl
import requests


class Scraper:
    def __init__(self):
        self.user_agent = None
        self.headers = None

    def get_user_agent(self):
        """
        Set random user agent string
        """
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        ]
        self.user_agent = random.choice(user_agents)
        return True

    def get_headers(self):
        """
        Set request headers used for scraping.
        """
        headers = {
            'Accept-Charset': 'utf-8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
            'user-agent': self.user_agent,
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
        }
        self.headers = headers

    def get_page(self, url, custom_headers=None, post_data=None):
        """
        Scrape url and return page dumo with status code
        custom_headers for passing custom headers used for specific websites
        post_data is used to set data to post on a url
        """
        response_details = {
            'page': None,
            'code': 0
        }
        if custom_headers:
            # merging custom headers with existing headers
            self.headers = {**self.headers, **custom_headers}
        try:
            if post_data:
                # if post data exists then send post request to input url
                req = requests.post(url, headers=self.headers, data=post_data)
            else:
                req = requests.get(url, headers=self.headers)
        except Exception as e:
            return response_details

        response_details['page'] = req.content
        response_details['code'] = req.status_code
        return response_details
