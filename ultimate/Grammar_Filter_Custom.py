#Grammar_Filter_Custom.py

from operator import contains
import sys
import os
import random
import datetime


raw_title = "" 


def grammar_filter(raw_title):
    
    title = raw_title
    
    #later can loop through simple key-value-pair map with string to search for as key and replacement char as value
    if "  " in raw_title:
        print (raw_title)
        title = " ".join(raw_title.split())
        print(title)
        print("Replaced 2 spaces with 1 space")

    if "This World" in raw_title:
        title = raw_title.replace("This World", "In This World")
        print("Replaced This World with In This World")

    return(title)