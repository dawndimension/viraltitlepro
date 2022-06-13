#Generate_Title.py

import sys
import os
import random
import datetime
from random import randint
from tinydb import TinyDB, Query
from Grammar_Checker import *
from Grammar_Filter_Custom import*

db = TinyDB('db.json')
space = " "
subject = "video"

#main entry point
#this function returns the generated title
def generate_multiple_titles(subject, tags, title_count):
	titles = []
	for x in range(0, title_count):
		print(x)
		titles.append(generate_title(subject, tags))
	print(titles)
	return titles

def generate_title(subject, tags):
	if subject == "" or subject == None:
		subject = "video"
	suffix = generate_suffix()
	prefix = generate_prefix()
	#print (prefix +space+ subject +space+ suffix)
	#.title() is built in python to make the text title-case
	raw_title = ((prefix +space+ subject +space+ suffix).title())
	#title = grammar_replace(raw_title)
	title = grammar_filter(raw_title)
	return title

def generate_prefix():
	Prefix = Query()
	prefix_type_selector = ["the","the"]
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
		custom_type_selector = ["-", "|", "...","","",""]
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


#test script with this uncommented
#print(generate_title("Putt", "#shorts"))
