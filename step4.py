import os
import time
import progressbar
import timeit
import pandas as pd
from nltk.tokenize import RegexpTokenizer

def word_ct(subdir,fname):
	os.chdir(subdir)
	tokenizer = RegexpTokenizer(r'\w+')
	with open(fname, 'r', encoding='utf-8') as file:
		lines_in_file = file.read()
	
	nltk_tokens = tokenizer.tokenize(lines_in_file)

	for s in nltk_tokens:
		if s == 's':
			nltk_tokens.remove('s')
		elif not s.isalpha():
			#print(s)
			nltk_tokens.remove(s)	

	for s in nltk_tokens:
		if not s.isalpha():
			#print(s)
			nltk_tokens.remove(s)
	return list(nltk_tokens)

def sortFreqDict(freqdict):
	aux = [(freqdict[key], key) for key in freqdict]
	aux.sort()
	aux.reverse()
	return aux

def wordListToFreqDict(wordlist):
	wordfreq = [wordlist.count(p) for p in wordlist]
	return dict(zip(wordlist,wordfreq))

if __name__ == '__main__':
	print('Start.')
	start = timeit.default_timer()
	cwd = os.getcwd()
	headword =[]
	sources = ['source1', 'source2']
	count = 0
	for source in sources:
		wordlist = word_ct(cwd+'/input/input4_headword', 'headword_'+source+'.txt')
		print('loaded')
		freq_dict = wordListToFreqDict(wordlist)
		freq_dict_keys = freq_dict.keys()
		headword.extend(freq_dict_keys)
		print('dict made')
		os.chdir(cwd+'/input/input5_freq')
		with open("freq_"+source+".txt", "w", encoding='utf-8') as output:
			output.write(str('COUNT'+'/t'+'HEADWORD'))
			output.write(str('/n'))
			for key in freq_dict_keys:
				print(key,'/t',freq_dict.get(key))
				output.write(str(str(freq_dict.get(key))+'\t'+key))
				output.write(str('/n'))
		print('')
		
	headword_dict = wordListToFreqDict(headword)
	headword_dict_keys = freq_dict.keys()
	os.chdir(cwd+'/input')
	with open("headword.txt", "w", encoding='utf-8') as output:
		for word in headword_dict_keys:
			output.write(str(word))
			output.write(str('/n'))
	stop = timeit.default_timer()
	print('\nTime taken: ', (stop - start)/60, ' minute/s') 
	print('--------------------------------')
	print('Fin.')
