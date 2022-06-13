#Grammar_Checker.py

import language_tool_python
import sys
import os
import random
import datetime
from random import randint
from tinydb import TinyDB, Query
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

#LanguageTool offers spell and grammar checking. Just paste your text here and click the 'Check Text' button. 
# Click the colored phrases for details on potential errors. or use this text too 
# see an few of of the problems that LanguageTool can detecd. What do you thinks of grammar checkers? 
# Please not that they are not perfect. Style issues get a blue marker: It's 5 P.M. in the afternoon. 
# The weather was nice on Thursday, 27 June 2017

raw_title = "" 


def grammar_replace(raw_title):

    # get the matches
    matches = tool.check(raw_title)
    
    print(matches)

    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    
    for rules in matches:
        if len(rules.replacements)>0:
            start_positions.append(rules.offset)
            end_positions.append(rules.errorLength+rules.offset)
            my_mistakes.append(raw_title[rules.offset:rules.errorLength+rules.offset])
            my_corrections.append(rules.replacements[0])
        
    
        
    my_new_raw_title = list(raw_title)
    
    
    for m in range(len(start_positions)):
        for i in range(len(raw_title)):
            my_new_raw_title[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_raw_title[i]=""
        
    my_new_raw_title = "".join(my_new_raw_title)
    print(my_new_raw_title)