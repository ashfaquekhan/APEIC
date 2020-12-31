#!/usr/bin/env python3

import os
import subprocess as subp
from modules.MISCELLANEOUS import MISCELLANEOUS
from modules.WEBHOOK import WEBHOOK
from modules.MACOS import MACOS

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white


def banner():
	os.system('clear')
	banner = r'''
$$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  $$$$$$$$\     $$$$$$\   $$$$$$\  $$\      $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|\__$$  __|$$  __$$\ $$  __$$\ $$  _____|   $$  __$$\ $$  __$$\ $$$\    $$$ |
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |         $$ |   $$ /  $$ |$$ |  $$ |$$ |         $$ /  \__|$$ /  $$ |$$$$\  $$$$ |
$$$$$$$  |$$ |  $$ |$$ |      $$$$$  /  $$$$$\       $$ |   $$$$$$$$ |$$$$$$$  |$$$$$\       $$ |      $$ |  $$ |$$\$$\$$ $$ |
$$  ____/ $$ |  $$ |$$ |      $$  $$<   $$  __|      $$ |   $$  __$$ |$$  ____/ $$  __|      $$ |      $$ |  $$ |$$ \$$$  $$ |
$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |         $$ |   $$ |  $$ |$$ |      $$ |         $$ |  $$\ $$ |  $$ |$$ |\$  /$$ |
$$ |       $$$$$$  |\$$$$$$  |$$ | \$$\ $$$$$$$$\    $$ |   $$ |  $$ |$$ |      $$$$$$$$\ $$\\$$$$$$  | $$$$$$  |$$ | \_/ $$ |
\__|       \______/  \______/ \__|  \__|\________|   \__|   \__|  \__|\__|      \________|\__|\______/  \______/ \__|     \__|
                                                                                                                                         
'''
	print(G + banner + W)
	print(G + '[+]' + C + ' DEV ON DUTY : ' + W + 'JalaluddinVECTOR')

def main():
	print('\n' + G + '[+]' + R + ' Choose Target : ' + W + '\n')
	print(G + '[1]' + C + ' Windows' + W)
	print(G + '[2]' + C + ' Mac_OS ' + W)
	while True:
		choice = input(G + '\nape > ' + W)

		if choice == '1':
			win()
		elif choice == '2':
    			MACOS(mac)
		elif choice == 'exit' or choice == 'quit':
			quit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass
def mac():
    	main()
def win():
	print('\n', end='')
	print(G + '[1]' + C + ' WEBHOOK' + W)
	print(G + '[2]' + C + ' MISCELLANEOUS' + W)
	
	while True:
		win_choice = input(G + '\nape[windows] > ' + W)
		
		if win_choice == '1':
			WEBHOOK(win)
		elif win_choice == '2':
			MISCELLANEOUS(win)
		elif win_choice == 'clear':
			os.system('clear')
		elif win_choice == 'back':
			return main()
		elif win_choice == 'help':
			return win()
		elif win_choice == '':
			pass
		elif win_choice == 'exit' or win_choice == 'quit':
			quit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def quit():
	distro = subp.Popen(['uname', '-r'], stdout = subp.PIPE)
	distro = distro.communicate()[0].decode()
	if 'ARCH' in distro:
		subp.call(['systemctl', 'stop', 'sshd.service'])
	else:
		subp.call(['systemctl', 'stop', 'ssh.service'])
	subp.call(['pkill', 'php'])
	exit()

try:
	banner()
	main()
except KeyboardInterrupt:
	print(R + '[-]' + C + ' Keyboard Interrupt.' + W + '\n')
	quit()
