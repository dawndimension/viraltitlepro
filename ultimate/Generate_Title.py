#Generate_Title.py

import language_tool_python
import sys
import os
import random
import datetime
from random import randint
from tinydb import TinyDB, Query


db = TinyDB('db.json')
space = " "

#main entry point
#this function returns the generated title
def generate_title(subject, tags):
	suffix = generate_suffix()
	prefix = generate_prefix()
	#print (prefix +space+ subject +space+ suffix)
	return ((prefix +space+ subject +space+ suffix).title())

def generate_prefix():
	Prefix = Query()
	prefix_type_selector = ["the","basically the", "essentially the", "surely the", "truly the"]
	prefix_choice = random_index(prefix_type_selector)
	#print (prefix_type_selector[prefix_choice])

	if "the" in prefix_type_selector[prefix_choice]:
		array_length = db.count(Prefix.type == 'the_modifier')
		index = randint(0, array_length-1)		
		Prefix_addon_custom = db.search(Prefix.type == 'the_modifier')[index]["value"]
	
	return (prefix_type_selector[prefix_choice]) + space + Prefix_addon_custom


def generate_suffix():
	Suffix = Query()
	typeOfSuffix = "verb";
	suffix_type_selector = ["suffix_wants_noun", "suffix_wants_verb", "suffix_wants_custom"]
	suffix_choice = random_index(suffix_type_selector)
	#print (suffix_type_selector[suffix_choice])
	
	if suffix_type_selector[suffix_choice] == "suffix_wants_noun":
		typeOfSuffix = "noun";
		#suffix_wants_noun = ["in the"]
		suffix_wants_noun = db.get(Suffix.type == 'suffix_wants_noun')["value"]
		#suffix_addon_noun = ["world"]
		suffix_addon_noun = db.get(Suffix.type == 'suffix_addon_noun')["value"]
		return suffix_wants_noun + space + suffix_addon_noun
	
	if suffix_type_selector[suffix_choice] == "suffix_wants_verb":
		typeOfSuffix = "verb";
		#suffix_wants_verb = ["in the"]
		suffix_wants_verb = db.get(Suffix.type == 'suffix_wants_verb')["value"]
		#suffix_addon_verb = ["world"]
		suffix_addon_verb = db.get(Suffix.type == 'suffix_addon_verb')["value"]
		return suffix_wants_verb + space + suffix_addon_verb

	if suffix_type_selector[suffix_choice] == "suffix_wants_custom":
		typeOfSuffix = "custom";
		custom_type_selector = ["-", "|", "","","",""]
		custom_suffix_choice = random_index(custom_type_selector)
		#print (custom_type_selector[custom_suffix_choice])
				
		array_length = db.count(Suffix.type == 'suffix_addon_custom')
		index = randint(0, array_length-1)		
		suffix_addon_custom = db.search(Suffix.type == 'suffix_addon_custom')[index]["value"]
		return (custom_type_selector[custom_suffix_choice]) + space + suffix_addon_custom


#get a random index in an array
def random_index(array):
	array_length = len(array)
	random_index = randint(0, array_length-1)
	return random_index



#generate_title("Putt", "#shorts")