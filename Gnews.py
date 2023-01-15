#!/usr/bin/env python3
# Google News
# gnews.py
# Author Hemanth.HM
# Site : www.h3manth.com
# Licensed under GNU GPL Version 3
'''
try:
    import pip
except ImportError:
	print("Pip Not Installed. Install With sudo apt-get install python-pip");
	exit();

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

import pip

required_pkgs = ['feedparser', 'tinyurl', 'colorama' ]
installed_pkgs = [pkg.key for pkg in pip.get_installed_distributions()]

for package in required_pkgs:
    if package not in installed_pkgs:
        with suppress_stdout():
            pip.main(['install', package])

'''
import feedparser
import pyshorteners
#import tinyurl
import colorama
from colorama import Fore, Back, Style


class Googlenews:
	""" This class helps to fetch top news from specific catagories of Goog News"""
	def get_input(self):
		""" Prompts user to select his choice of news """
		bold = "\033[1m"
		reset = "\033[0;0m"
		try:
			""" print  News feed list : \n1.   Top \n2.   World \n3.   Australia \n4.   Canada \n5.   India \n6.   Ireland \n7.   New \n8.   South \n9.   US \n10.  UK \n11.  Business \n12.  Sci/Tech \n13.  Health \n14.  Sports \n15.  Entertainment """
			""" news_type = int(raw_input(bold+"Which you you like to read : "+reset)) """
			news_type = 1
			return news_type
		except ValueError:
			print('Invalid input, please select a number for the list')

	def get_feed(self):
		""" Returns the feed type based on the users input """
		url="http://news.google.com/news?ned=%s&topic=%s&output=rss"
		links=[{"ned":"us", "type":"h"},
			   {"ned":"us", "type":"w"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"nz"},
			   {"ned":"us", "type":"sa"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"n"},
			   {"ned":"us", "type":"b"},
			   {"ned":"us", "type":"t"},
			   {"ned":"us", "type":"m"},
			   {"ned":"us", "type":"s"},
			   {"ned":"us", "type":"e"},
			  ]
		feed = links[self.get_input()]
		return url%(feed["ned"],feed["type"])


	def gnews(self):
		""" Returns the top ten news of the selected section """
		feed_url = self.get_feed()
		feed_data = feedparser.parse(feed_url)
		print("")
		type_tiny = pyshorteners.Shortener()
		for data in feed_data["items"]:
			tiny_url = type_tiny.tinyurl.short(data["link"])
			#tiny_url = tinyurl.create_one(data["link"])
			print('\033[33m' + data["title"] + " : " + Style.RESET_ALL + tiny_url)
			print("")

def main():
	""" The main block where all the action happens """
	news = Googlenews()
	news.gnews()

if __name__ == "__main__":
	main()
