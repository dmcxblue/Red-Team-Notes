#!/usr/bin/python3 env
# Takes a lot of screenshots

import optparse
import requests
import subprocess
import time

print('OSINT V 0.1')
print('')
print('A simple OSINT Tool that is probably slow, but I like it')

def people_search():
        parser = optparse.OptionParser()
        parser.add_option('-p','--search', dest='search', help='Search Type People, Number, Email, Username')
        parser.add_option('-n','--fname', dest='fname', help='First Name of Target')
        parser.add_option('-l','--lname', dest='lname', help='Last Name of taget')
        (options, arguments) = parser.parse_args()
        if not options.search:
                # Code for people error
                parser.error('[-] Please specify the type of Search, use --help for more info')
        elif not options.fname:
                # Code for name error
                parser.error('[-] Please specify a First Name to search, use --help for help')
        elif not options.lname:
                # COde error last name
                parser.error('[-] PLease provide a Last Name, use --help for  help')
        return options

def search_people(search, fname, lname):
        print('[+] Searching for {}'.format(search, fname))
        subprocess.call(['webscreenshot', '-f', 'pdf', 'https://thatsthem.com/name/' + fname + '-' + lname + '/CA'])

options = people_search()
search_people(options.search, options.fname, options.lname)
