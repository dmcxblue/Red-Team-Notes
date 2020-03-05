#!/usr/bin/python3
# A hacking Framework : Jarvis
# This will try to be as close as possible to other incredible C2 Frameworks and more
# hopefully this will help me in many assesments and interviews
# Version : 1.2
# Author : David Garcia (dmcxblue)

import os
import subprocess
import time
import optparse

print ("""     #
      #   ##   #####  #    # #  ####
      #  #  #  #    # #    # # #
      # #    # #    # #    # #  ####
#     # ###### #####  #    # #      #
#     # #    # #   #   #  #  # #    #
 #####  #    # #    #   ##   #  ####
             Version 1.2 OSINT
""")

print ("Menu: ")
print ("")
print ("")
print ("1-- Recon:")
print ("2-- Scanning:")
print ("3-- Vulnerability/Exploits:")
print ("4-- OSINT:")

menu_choice_1 = input('JARVIS > ')

def enum():
        print ("Will enumerate with various tools this will take a while...")
        print ("Please add the website to be scanned [Example: google.com]")
        website_enum = input("JARVIS > ")
        subprocess.call(['curl', '-i', website_enum, '> curled_response.txt'])
        subprocess.call(['dnsenum', website_enum, '> dnsenum.txt'])
        subprocess.call(['nikto', '-h', website_enum, '-o', 'nikto-enum.txt'])
        print ("Searching for subdomains")
        print ("Might take a while")
        subprocess.call(['fierce', '--dns', website_enum, '> fierce-enum.txt'])
        subprocess.call(['gobuster', 'dns', '-d', website_enum, '-w', '/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt', '>> gobuster-dns.txt'])
        subprocess.call(['sublist3r', '-d', website_enum, '>> sublist3r.txt'])
        print ('Enumerating any directories with a few common dictionaries')
        print ('Would you like to add any extension?')
        extensions = input('Y / N > ')

        if extensions == 'Y':
                print ('Please add extensions and separate with commas [,]')
                subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/big.txt', '-x', extensions, '-o', 'gobuster-scan-extensions-1.log'])
                subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/common.txt', '-x', extensions, '-o', 'gobuster-scan-extensions-2.log'])
        elif extensions == 'N':
                subprocess.call(['gobuster', 'dir', '-u', website_enum, '-w', '/opt/seclists/Discovery/Web-Content/big.txt', '-t', '50' '-o', 'gobuster-scan-1.log'])

def recon():
        print ("Active or Passive: ")
        aop = input('JARVIS > ')

        if aop == "Active":
                print ("Scanning Aggrresively")
                print ('IP Target: ')
                ip_arg_1 = input('JARVIS > ')
                subprocess.call(['nmap','-A', ip_arg_1, '-Pn', '-oA', 'aggressive'])
        elif aop == "Passive":
                print ("Scanning Passively")
                print ('IP Target:')
                ip_arg_2 = input('JARVIS > ')
                subprocess.call(['nmap', '-sS', ip_arg_2, '-Pn', '-oA', 'passive'])

def vuln_exploits():
        print ("Will find the most reliable exploits for the enumerated item")
        print ("Please input the deesirede term to be searched")
        target = input("Target Software> ")
        print ("You may want to search your desired exploit [Local/Remote] and copy this onto your current directory")
        time.sleep(4)
        print ("Calling searchsploit")
        time.sleep(3)
        subprocess.call(['searchsploit', target])
        print ("Searching for anything relevant on your machine, this can be scripts or modules")
        print ("")
        time.sleep(3)
        os.system('find / 2>/dev/null | grep {}'.format(target))

def osint():
        print ("Great I'll will ask for information in regards to what I am searching for")
        print ("")
        print ("User, Email, Person, Phone")
        print ("")
        osint_choice = input('OSINT> ')

        if osint_choice == 'User' or 'user':
                print ("Please Enter the Username")
                username = input ('OSINT > ')
                print ("[+] Searching for {} Username".format(username))
                subprocess.call(['usufy', '-n', username])
                print ("OSRFRAMEWORK RESULTS")
        exit ()
        if osint_choice == 'Email' or 'email':
                print ("Please Enter an Email")
                email = input ('OSINT > ')
                print("[+] Searching Email {}".format(email))
                subprocess.call(['mailfy', '-m', email])
                print ("Using theHarvester to search for more emails on the domain")
                print ("[Example: google.com]")
                email_th = input ("Domain > ")
                subprocess.call (['theHarvester', '-d', email_th, '-l', '100', '-b', 'google,linkedin', '> theHarvester-results.txt'])
        exit()
if osint_choice == 'Person' or 'person':
                print ("Please Enter a Name")
                print ("You can query Usernames as well")
                name = input ('OSINT > ')
                print ('[+] Searching for {}'.format(name))
                subprocess.call(['searchfy', '-q', name])
                print ("Done")
        else:
                print ("Please try again")
        return osint

if menu_choice_1 == '1':
        enum()
if menu_choice_1 == '2':
        recon()
if menu_choice_1 == '3':
        vuln_exploits()
if menu_choice_1 == '4':
        osint()
else:
        print ("Bye")
        exit()
