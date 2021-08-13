INSTRUCTIONS FOR CS WORD LIST

Pre-processing:

Before running any script, ensure that you know the amount of different source files you have (Currently there are 12 for the Tier 3 CS project, located in input/input1). A source file means a different sub-area of a discipline (read report). All the source texts have to be collected and saved as sourceN.txt where N is the source number. 

Folders also have to be created for the results that will be obtained from running the scripts. 

The repo contains all the needed folders; to run the scripts use the "input" folder along with the sub sequential folders (these all have to be empty before running, except the input1 folder). Go to input and open the empty "freq_input.xlsx" spreadsheet and ensure you have the same number of sheets as you have sources.
Go to input/input3_alpha and and ensure you have the same number of folders as you have sources.

The "output" folder also has to be downloaded with an empty spreadsheet labelled "range" and the "remove" folder needs to be downloaded while containing the empty abc.txt file. The entire AWL folder needs to be downloaded as well.

Finally, download all script files.

Steps to run scripts:

NOTE: UPDATE DIRECTORY LOCATION RESPECTIVELY

1) Run step1.py : This will create a list of words in each source files and is saved in input2 (Breaks up paragraphs of text by separating each word on a new line).

2) Run step2.py : Organizes each word in a source file by alphabetical order, and a new file is created separately for each letter of the alphabet under every source (needed for faster processing). Saved under input3_alpha/sourceN, where N is the source number.

3) Run step3.py : This script will rename the words as headwords (see report) and remove OOV (see report) words. This is done by using the generated dictionary of headwords in the "alphabet.xslx" spreadsheet (Please note: this dictionary is missing a few words and does not include acronyms, meaning these missing words will be OOV and will not be present in the final word list. This can be solved in the future by implementing a way to sift through the OOV words and include the CS-related words in the headword file). The headwords file for each source is saved in input4_headword.

4) Run step4.py : This will generate the frequecy information and also the final set of headwords which are saved in input/headword.txt

5) Run NAWL_T1_vd.py : This will read through the "NAWL_1.xslx" and extract all words into /remove/abc.txt, using a list format (new line, capitalized).

6) Run pdf_to_text.py : This will read through all the academic Tier 2 word lists and extract all words into /remove/abc.txt, using a list format (new line, capitalized). 

7) Run del.py : This script will remove the Tier 1 and 2 words saved in abc.txt. This final CS wordlist will be saved under input/headword.txt_updated

8) Open freq_input.xlsx in /input and in each sheet, go to Data/Get External Data/From Text and select respective files from /input/input5_freq. Save the xlsx file and close it.

7) Run step5.py : This will combine the final wordlist along with frequencies/range. This will be saved in a new file, info.txt in /output folder. 

8) Open range.xlsx in /output, go to Data/Get External Data/From Text and select info.txt. This will arrange all the information of range and frequency in the xlsx file.