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
	sheets = ['Sheet1','Sheet2']
	headword = []
	cwd = os.getcwd()
	wordlist = word_ct(cwd+'/input','headword_updated.txt')
	#print(wordlist[0])
	os.chdir(cwd+'/output')
	with open("info.txt", "w", encoding='utf-8') as output:
		output.write(str('HEADWORD/tF1/tF2/tRANGE/tFREQ'))
		output.write(str('/n'))
		for word in wordlist:
			output.write(str(word+'/t'))
			#print(word ,end=' ')
			range1 = 0
			freq1 = 0
			word_check = False;
			for sheet in sheets:
				word_check = False;
				os.chdir(cwd+'/input')
				df = pd.read_excel('freq_input.xlsx', sheet_name=sheet)
		
				for i in df.index:
					#print('index area ',i, ' ',df['FAMILY'][i])
					if(str(df['HEADWORD'][i])==word):
						output.write(str(str(df['COUNT'][i])+'/t'))
						#print(df['COUNT'][i], end=' ')
						word_check = True;
						range1 += 1
						freq1 += df['COUNT'][i]
						break;
				if(word_check):
					continue;
				else:
					output.write(str('0/t'))
					#print('0', end=' ')
					headword.append(word)
			output.write(str(str(range1)+'/t'+str(freq1)))
			output.write(str('/n'))
			#print(range1,' ',freq1)


	print('--------------------------------')
	stop = timeit.default_timer()
	print('\nTime taken: ', (stop - start)/60, ' minute/s') 
	print('--------------------------------')
	print('Fin.')
