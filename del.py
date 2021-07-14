import os
import timeit
from itertools import chain
from nltk.tokenize import RegexpTokenizer

def size_ct(subdir,fname):
    os.chdir(subdir)
    tokenizer = RegexpTokenizer(r'\w+')
    print(os.curdir,fname)
    with open(fname, 'r', encoding="utf8") as file:
        lines_in_file = file.read()
    
    nltk_tokens = tokenizer.tokenize(lines_in_file)

    for s in nltk_tokens:
        if s == 's':
            nltk_tokens.remove('s')
        elif not s.isalpha():
            nltk_tokens.remove(s)   

    for s in nltk_tokens:
        if not s.isalpha():
            nltk_tokens.remove(s)

    length = len(nltk_tokens)
    print(length)
    return nltk_tokens

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

if __name__ == '__main__':

    start = timeit.default_timer()
    cwd = os.getcwd()
    
    wordlist = []
    wordlist.extend(size_ct(cwd+'/remove','abc.txt'))
    freq_dict = wordListToFreqDict(wordlist)
    #sorted_freq_dict = sortFreqDict(freq_dict)
    print('Number of dictionary items: ',len(freq_dict))
    '''for i in range(0, len(sorted_freq_dict)):
        print(sorted_freq_dict[i])'''

    wordlist1 = []
    wordlist1.extend(size_ct(cwd+'/input','headword.txt'))
    headword = []
    for word in wordlist1:
        if(word in list(freq_dict.keys())):
            print(word)
        else:
            headword.append(word)
    
    os.chdir(cwd+'/input/')   
    with open("headword_updated.txt", "w", encoding='utf-8') as output:
        for word in headword:
            output.write(str(word))
            output.write(str('/n'))
    #print('karan' in list(freq_dict.keys()))
    stop = timeit.default_timer()
    print('\nTime taken: ', (stop - start)/60, ' minutes') 
    print('-----------------------------------------------------------------------------')
