#!/usr/bin/env python3
import os
import json
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def MACOS(mac):
	print('\n', end='')
	misc_scripts = []
	for (dirpath, dirname, filenames) in os.walk('scripts/macos/'):
		misc_scripts.extend(filenames)
	for item in misc_scripts:
		print(G + '[{}] '.format(misc_scripts.index(item)) + W + item)

	while True:
		try:
			misc_choice = input(G + '\nape[macos] > ' + W)		

			if misc_choice == 'clear':
				os.system('clear')
			elif misc_choice == 'back':
				return mac()
			elif misc_choice == 'help':
				return MACOS()
			elif misc_choice == '':
				pass
			elif misc_choice == 'exit' or misc_choice == 'quit':
				quit()
			elif int(misc_choice) <= len(misc_scripts) - 1:
				with open('conf/macos_scripts.json', 'r') as json_file:
					options = json.load(json_file)
					chosen = misc_scripts[int(misc_choice)]
			
					for k,v in options.items():
						if k in chosen:	
							desc = v['desc']
							url_state = v['url']			
							server_state = v['server']
							print('\n', end = '')
							print(G + '[+]' + C + ' Script : ' + W + chosen + '\n')
							print(G + '[+]' + C + ' Info : ' + W + desc + '\n')
							if url_state == 1:
    								MACOS.misc_url = input(G + '[+]' + C + ' URL (ENTER 0 IF YOU DO NAT HAVE ONE):' + W)
							    	if MACOS.misc_url == '0':
    										MACOS.misc_url = "https://www.bleepstatic.com/images/stock-photos/hacking/hacker-hacking.jpg"
							else:
								pass
							if server_state == 1:
								MACOS.misc_host = input(G + '[+]' + C + ' ENTER A STRING: ' + W)

							script_path = '/scripts/macos/' + chosen
							misc_output(script_path, chosen, url_state, server_state)
			else:
				print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
				pass
		except ValueError:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def misc_output(script_path, chosen, url_state, server_state):
	base_path = os.getcwd() + script_path
	outfile_path = os.getcwd() + '/output/{}'.format(chosen)

	if url_state == 1:
		with open(base_path, 'r') as file :
			filedata = file.read()

		filedata = filedata.replace('URL', MACOS.misc_url)

		with open('output/{}'.format(chosen), 'w') as file:
			file.write(filedata)
	else:
		os.system('cp {} {}'.format(base_path, outfile_path))
	
	if server_state == 1:
		with open(base_path, 'r') as file :
			filedata = file.read()

		filedata = filedata.replace('TEXT', MACOS.misc_host)

		with open('output/{}'.format(chosen), 'w') as file:
			file.write(filedata)

	print(G + '[+]' + C + ' Script Generated : ' + W + outfile_path)