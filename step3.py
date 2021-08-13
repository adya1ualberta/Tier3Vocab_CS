import os
import time
import progressbar
import timeit
import pandas as pd
from nltk.tokenize import RegexpTokenizer

def word_ct(subdir,fname):
	os.chdir(subdir)
	tokenizer = RegexpTokenizer(r'\w+')
	with open(fname, 'r',encoding='utf-8') as file:
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
	sheets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	sources = ['source1', 'source2', 'source3', 'source4', 'source5', 'source6', 'source7', 'source8', 'source9', 'source10', 'source11', 'source12']
	cwd = os.getcwd()
	for source in sources:
		headword = []
		for sheet in sheets:
			wordlist = word_ct(cwd+'/input/input3_alpha/'+source, sheet.lower()+'.txt')
			os.chdir(cwd+'/input/input3_alpha/')
			df = pd.read_excel('alphabet.xlsx', sheet_name=sheet)
			for word in wordlist:
				word_check = False;
				
				for i in df.index:
                                
					if(str(df['FAMILY'][i])==word):
						headword.append(str(df['HEADWORD'][i]))
						#print(df['HEADWORD'][i])
						word_check = True;
						break;
				if(word_check):
					continue
				else:
					#headword.append(word)
					print(word,' oov')

		os.chdir(cwd+'/input/input4_headword')
		with open("headword_"+source+".txt", "w", encoding='utf-8') as output:
			for word in headword:
				output.write(str(word))
				output.write(str('\n'))
		print('')

			
	print('--------------------------------')
	#wordlist = word_ct(cwd+'/input/input2', 'nl_source.txt')
	#print(len(wordlist))
	'''alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
				os.chdir(cwd+'/input/input4_headword')
				for alpha in alphabet:
					with open(alpha+".txt", "w", encoding='utf-8') as output:
						for word in headword:
							if(word[0]==alpha.upper()):
								output.write(str(word))
								output.write(str('\n'))
			'''
	stop = timeit.default_timer()
	print('\nTime taken: ', (stop - start)/60, ' minute/s') 
	print('--------------------------------')
	print('Fin.')

