#!/usr/bin/python3
# A hacking Framework : Jarvis
# This will try to be as close as possible to other incredible C2 Frameworks and more
# hopefully this will help me in many assesments and interviews
# Version : 1.1
# Author : David (dmcxblue)

import os
import subprocess
import time
import optparse

print("""      #
      #   ##   #####  #    # #  ####
      #  #  #  #    # #    # # #
      # #    # #    # #    # #  ####
#     # ###### #####  #    # #      #
#     # #    # #   #   #  #  # #    #
 #####  #    # #    #   ##   #  ####
             Version 1.1
""")

print("Menu: ")
print("")
print("")
print("1-- Recon:")
print("2-- Scanning:")
print("3-- Vulnerability/Exploits:")

menu_choice_1 = input('> ')

def enum():
	print("Will enumerate with various tools this will take a while...")
	print("Please add the website to be scanned")
	website_enum = input("> ")
	
	subprocess.call(['curl', '-i', website_enum, '> curled_response.txt'])
	subprocess.call(['dnsenum', website_enum, '> dnsenum.txt'])
	subprocess.call(['fierce', '--dns', website_enum, '> fierce-enum.txt'])
	subprocess.call(['nikto', '-h', website_enum, '-o', 'nikto-enum.txt'])
	print('Enumerating any directories with a few common dictionaries')
	print('Would you like to add any extension?')
	extensions = input('Y / N > ')
	
	if extensions == 'Y':
		print('Please add extensions and separate with commas [,]')
		subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/big.txt', '-x', extensions, '-o', 'gobuster-scan-extensions-1.log'])
		subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/common.txt', '-x', extensions, '-o', 'gobuster-scan-extensions-2.log'])
	elif extensions == 'N':
		subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/big.txt', '-t', '50' '-o', 'gobuster-scan-1.log'])

def recon():
        print("Active or Passive: ")
        aop = input('> ')

        if aop == "Active":
                print("Scanning Aggrresively")
                print('IP Target: ')
                ip_arg_1 = input('> ')
                subprocess.call(['nmap','-A', ip_arg_1, '-Pn', '-oA', 'aggressive'])
        elif aop == "Passive":
                print("Scanning Passively")
                print('IP Target:')
                ip_arg_2 = input('> ')
                subprocess.call(['nmap', '-sS', ip_arg_2, '-Pn', '-oA', 'passive'])

def vuln_exploits():
	print("Will find the most reliable exploits for the enumerated item")
	print("Please input the deesirede term to be searched")
	target = input("Target Software> ")
	print("You may want to search your desired exploit [Local/Remote] and copy this onto your current directory")
	time.sleep(4)
	print("Calling searchsploit")
	time.sleep(3)
	subprocess.call(['searchsploit', target])
	print("Searching for anything relevant on your machine, this can be scripts or modules")
	print("")
	time.sleep(3)
	os.system('find / 2>/dev/null | grep {}'.format(target))

if menu_choice_1 == '1':
        enum()
elif menu_choice_1 == '2':
	recon()
elif menu_choice_1 == '3':
	vuln_exploits()
