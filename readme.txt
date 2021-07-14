Instructions:
Before running any script, ensure that you know the amount of different source files you have. A source file means a different sub-area (read report) and all the texts have to be collected and saved as sourceN.txt where N is the source number.
Go to input and open freq_input.xlsx and ensure you have the same number of sheets as you have sources.
Go to input/input3_alpha and and ensure you have the same number of folders as you have sources.

Steps:
1) Run step1.py : This will create a list of words in each source files and is saved in input2.
2) Run step2.py : This will create alphabetically separations of each source file word (needed for faster processing) and is saved in input3_alpha/sourceN where N is the source number.
3) Run step3.py : This will rename the words as headwords and remove OOV. The headwords file for each source is saved in input4_headword.
4) Run step4.py : This will generate the frequecy information and also the final set of headwords which are saved in input/headword.txt
5) Remove words from Tier 1 and Tier 2 from the headword.txt. This can be done by saving all other wordlists in /remove/abc.txt and running the del.py 
6) Open freq_input.xlsx in /input and in each sheet, go to Data/Get External Data/From Text and select respective file from /input/input5_freq. Save the xlsx file and close it.
7) Run step5.py : This will create the final info.txt in /output folder. 
8) Open range.xlsx in /output, go to Data/Get External Data/From Text and select info.txt. This will arrange all the information of range and frequency in the xlsx file.