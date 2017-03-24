import numpy as np

fh_syn=open("companies.txt","r")
list_company_names = fh_syn.read().split('\n')
fh_syn.close()

for i in list_company_names:
	print i.lower()