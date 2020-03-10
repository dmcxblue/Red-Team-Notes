#! /usr/bin/python3 env
# Favorite tools
# Scripted cause I have to download again everytime I start fresh
# It's annoying
# This tool doesnt automatically installt hem....Yet
# Won't work on that becasue I don't want it to force install any packages
# Version 0.1

import subprocess
import time
import os

print ("Tool installer for Red Team")
print ('')
print ("Or hacking in general")
print ("THIS WILL NOT INSTALL THE JUST DOWNLOAD THE REPO'S")
print ("Please run as root files get saved on your '/opt' PATH")
print ('')
print ("Ready ?")

# Extra packages so some of the tools work

package1 ='https://packages.microsoft.com/config/ubuntu/19.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb'

ready = input('> ')

if ready == 'Y' or 'y':
	os.chdir('/opt')
	# First we will update
	os.system('apt update')
	os.system('apt upgrade')
	os.system('apt dist-upgrade')
	subprocess.call(['git', 'clone', 'https://github.com/BC-SECURITY/Empire.git'])
	subprocess.call(['git', 'clone', 'https://github.com/sevagas/macro_pack.git'])
	subprocess.call(['git', 'clone', '--recursive', 'https://github.com/cobbr/Covenant.git'])
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
	os.system('wget -q ' package1)
elif ready == 'N':
	print ("OK")

