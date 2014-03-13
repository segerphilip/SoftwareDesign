"""
Program: reading
Author: Philip Seger
Date: 2/24/14
"""
import re

#load the text into python
f = open("pg174.txt", "r")
full_text = f.read()
#find and delete the boilerplate beginning
end_of_boilerplate = full_text.index(" ***")
full_text[end_of_boilerplate+4:]
#find and delete the ending of the footer
end_of_novel = full_text.index("End of Project Gutenberg's")
full_text = full_text[:end_of_novel]

#def get_words_from_book(full_text):
#	all_words = re.findall("[\w'\-]+", full_text)
	
#def get_word_counts_list(full_text):
#	all_words = re.findall("[\w'\-]+", full_text)
#	for i in range(len(all_words)):

if __name__ == '__main__':
	word_occurence = []
	get_word_counts_list(full_text)