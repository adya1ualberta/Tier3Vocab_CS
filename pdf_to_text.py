import PyPDF2
import textract
import os

#Write a for-loop to open many files
#cwd = os.getcwd()

import pdfplumber

cwd = os.getcwd()
Grades = ['Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6', 'Grade7', 'Grade8', 'Grade9', 'Grade10', 'Grade11', 'Grade12', 'Grade13']
#Grades=['Grade11']
for Grade in Grades:
	text=''
	final_text=''
	filename = cwd +'/AWL/'+Grade+'.pdf'
	print(filename)
	with pdfplumber.open(filename) as pdf:
		pages = pdf.pages
		print(pages)
		for page in pages:
			#page  = pdf.pages[1]
			#text = page.chars[0]
			print(page)
			#print(type(page.extract_text())
			text=page.extract_text().replace(' ', '\n')
			#print(text)
			#for line in text.split(' '):
			#			final_text+=line
			#print(text)
			os.chdir(cwd+'/remove')
			with open("abc.txt", "a", encoding='utf-8') as output:
					output.write(str(text.upper()))
					output.write(str('\n'))
	

print("Done text extract")
