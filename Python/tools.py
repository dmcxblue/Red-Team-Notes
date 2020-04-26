#! /usr/bin/python3 env
# Favorite tools
# Scripted cause I have to download again everytime I start fresh
# It's annoying
# This tool doesnt automatically install them....Yet
# Won't work on that becasue I don't want it to force install any packages
# Version 0.3
# Added more tools and fixed some typos
# Added more installations steps so tools get a chance to be ready and installed

import subprocess
import time
import os

print ("Tool installer for Red Team")
print ('')
print ("Or hacking in general")
print ("THIS WILL NOT INSTALL THE JUST DOWNLOAD THE REPOS")
print ("Please run as root files get saved on your '/opt' PATH")
print ('')
print ("Ready ?")

# Extra packages so some of the tools work

package1 ='https://packages.microsoft.com/config/ubuntu/19.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb'

ready = input('> ')

if ready == 'y':
	os.chdir('/opt')
	# First we will update and download a few necessary packages
	os.system('apt update')
	os.system('apt upgrade')
	os.system('apt dist-upgrade')
	os.system(' apt install python3-pip')
	os.system('wget -q ' + package1)
	os.system('dpkg -i packages-microsoft-prod.deb')
	# I can add more dependecies and install them so they are already avaialble
	# For example DOTNET for Covenant
	# More tools 0.2
	os.system('apt install exiftool')
	os.system('apt install gobuster')
	os.system('apt install julia') # New programming language
	os.system('apt install docker')
	os.system('apt-get install dotnet-sdk-2.2') # This version is necessary for Covenant
	os.system('apt-get install apt-transport-https')
	subprocess.call(['git', 'clone', 'https://github.com/1N3/Sn1per.git'])
	subprocess.call(['git', 'clone', 'https://github.com/m8r0wn/CrossLinked.git'])
	subprocess.call(['git', 'clone', 'https://github.com/outflanknl/EvilClippy.git'])
	subprocess.call(['git', 'clone', 'https://github.com/TheWover/donut.git'])
	subprocess.call(['git', 'clone', 'https://github.com/dafthack/DomainPasswordSpray.git'])
	subprocess.call(['git', 'clone', 'https://github.com/outflanknl/RedELK.git'])
	# Tools 0.1
	subprocess.call(['git', 'clone', 'https://github.com/BC-SECURITY/Empire.git'])
	subprocess.call(['git', 'clone', 'https://github.com/sevagas/macro_pack.git'])
	subprocess.call(['git', 'clone', '--recursive', 'https://github.com/cobbr/Covenant.git'])
	subprocess.call(['git', 'clone', 'https://github.com/trustedsec/unicorn.git'])
	subprocess.call(['git', 'clone', 'https://github.com/hlldz/SpookFlare.git'])
	subprocess.call(['git', 'clone', 'https://github.com/DarkSecDevelopers/HiddenEye.git'])
	subprocess.call(['apt', 'install', 'osrframework'])
	subprocess.call(['git', 'clone', 'https://github.com/r3motecontrol/Ghostpack-CompiledBinaries.git'])
	subprocess.call(['git', 'clone', 'https://github.com/BishopFox/spoofcheck.git'])
	subprocess.call(['git', 'clone', 'https://github.com/xillwillx/skiptracer.git'])
	subprocess.call(['git', 'clone', 'https://github.com/dchrastil/ScrapedIn.git'])
	subprocess.call(['git', 'clone', 'https://github.com/SimplySecurity/SimplyEmail.git'])
	subprocess.call(['git', 'clone', 'https://github.com/nccgroup/typofinder.git'])
	subprocess.call(['git', 'clone', 'https://github.com/davidtavarez/pwndb.git'])
	subprocess.call(['git', 'clone', 'https://github.com/smicallef/spiderfoot.git'])
	subprocess.call(['git', 'clone', 'https://github.com/nccgroup/demiguise.git'])
	subprocess.call(['git', 'clone', 'https://github.com/0xdeadbeefJERKY/Office-DDE-Payloads.git'])
	subprocess.call(['git', 'clone', 'https://github.com/Mr-Un1k0d3r/SCT-obfuscator.git'])
	subprocess.call(['git', 'clone', 'https://github.com/api0cradle/UltimateAppLockerByPassList.git'])
	subprocess.call(['git', 'clone', 'https://github.com/ustayready/CredSniper.git'])
	subprocess.call(['git', 'clone', 'https://github.com/zerosum0x0/koadic.git'])
	subprocess.call(['git', 'clone', 'https://github.com/codewhitesec/LethalHTA.git'])
	subprocess.call(['git', 'clone', 'https://github.com/SecureAuthCorp/impacket.git'])
	subprocess.call(['git', 'clone', 'https://github.com/byt3bl33d3r/SprayingToolkit.git'])
	# This will install Spider requirements
	# subprocess.call(['pip', 'install', '-r', '/opt/spiderfoot/requirements.txt')]
	# Continue with tools
	# Installing packages
elif ready == 'n':
	print ("OK")

