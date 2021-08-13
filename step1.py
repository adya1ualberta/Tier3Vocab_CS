from nltk.tokenize import RegexpTokenizer
import os
import timeit

def word_ct(subdir, fname):
	os.chdir(subdir)
	print(os.curdir,fname)
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

	nltk_tokens = [x.upper() for x in nltk_tokens]

	return nltk_tokens


if __name__ == '__main__':
	start = timeit.default_timer()
	cwd = os.getcwd()
	sources = ['source1', 'source2', 'source3', 'source4', 'source5', 'source6', 'source7', 'source8', 'source9', 'source10', 'source11', 'source12']
	for source in sources:
		wordlist = word_ct(cwd+'/input/input1', source+'.txt')
		os.chdir(cwd+'/input/input2')
		with open("nl_"+source+".txt", "w", encoding='utf-8') as output:
			for word in wordlist:
				output.write(str(word))
				output.write(str('\n'))

	stop = timeit.default_timer()
	print("Done")
	print('-----------------------------------------------------------------------------')
