import os
import time
import progressbar
import timeit
import pandas as pd
from nltk.tokenize import RegexpTokenizer


print('Start.')
#start = timeit.default_timer()

cwd = os.getcwd()

sheets = ['Sheet1']
for sheet in sheets:
        text = ''
        #wordlist = (cwd+'/AWL/', 'NAWL_1')
        #print(wordlist)
        filename='/Users/adyadutt/downloads/AWL/NAWL_1.xlsx'
        output=open("/Users/adyadutt/downloads/remove/abc.txt", "a", encoding='utf-8')
        df = pd.read_excel(filename, sheet_name=sheet,skiprows=[0],index_col=0)
        df.fillna(' ', inplace = True)
        df.replace(' ', '\n')
        #print(df.index)
        columns=list(df)
        print(columns)
        for i in columns:
                #os.chdir(cwd+'/remove')
                for j in df.index:
                                #print(df)
                                ln=str(df[i][j]).upper()
                                #print(ln)
                        #df.replace('\t', '\n')
                                output.write(ln)
                                output.write(str('\n'))
        print("First file done")

#sheets1 = ['Total Coverage']
#for sheet1 in sheets1:
filename='/Users/adyadutt/downloads/AWL/NGSL+Spoken+1.01.xlsx'
print(filename)
df1 = pd.read_excel(filename, sheet_name='Total Coverage')#,names=['Lemma']
df1.fillna(' ', inplace = True)
#df1.columns=['Lemma']
df2=df1.iloc[:,0]
#df2=df1.columns[0]

output_1=open("/Users/adyadutt/downloads/remove/abc.txt", "a", encoding='utf-8')
print(df2.index)
for k in df2.index:
        ln1=str(df2[k]).upper()
        #print(ln1)
        
        output_1.write(ln1)
        output_1.write(str('\n'))
output_1.close()
        
        

print("Second file Done")
