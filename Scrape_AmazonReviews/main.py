# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:39:01 2020

@author: lim
"""
import os
import sys


if __name__ == "__main__":
    while True:
        asin = input("Please input ASIN number:")
        if asin.lower() == "end":
            break
        
        if os.path.isfile("output.csv")== True:
            os.system("del output.csv")
        my_dir = os.path.dirname(sys.argv[0])
        cmd='%s %s' % (sys.executable, os.path.join(my_dir, 'Data_Analysis.py'))
            
        os.system("scrapy runspider spiders/AmazonReview.py -o output.csv -a asin={} & {}".format(asin, cmd))
