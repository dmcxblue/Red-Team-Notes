#! /usr/bin/python3 env
# Favorite tools
# Scripted cause I have to download again everytime I start fresh
# It's annoying
# This tool doesnt automatically install them....Yet
# Won't work on that becasue I don't want it to force install any packages
# Version 0.5
# Added more tools and fixed some typos
# Added the Names cause I would get lost
# Added more installations steps so tools get a chance to be ready and installed
######################################
#
# Current Tools
#
# Sn1per, CrossLinked,EvilCLippy, donut, DomainPasswordSpray, RedELK, Rubeus, BloodHOund, Kerberoast
# MailSniper, Phantom Evasion, venom, Penetration Testing Tools (Red Team Folder), Empire, Macro_Pack
# Covenant, Unicorn, SpookFLare,NetLoader, OSRFRAMEWORK, Wesng, GhostPack
# spoofcheck, skiptracer, ScrapedIn, SimplyEmail (docker), typofinder, pwndb, spiderfoot, demiguise
# Office-DDE-Payloads, EvilURL, SCT-Obfuscator, UACBypass Collection, CredSniper, Infoga, koadic, Scriblur
# powerob, LethalHTA, vba-obfuscator, vba_obfuscator, impacket, SprayingToolKit, docker.io
# 
######################################

import subprocess
import time
import os

print ("Tool installer for Red Team")
print ("Or hacking in general")
print ("THIS WILL NOT INSTALL THE TOOLS IT WILL JUST DOWNLOAD THE REPOS")
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
	#os.system('apt install julia') # New programming language
	os.system('apt install docker')
	os.system('apt install docker.io')
	os.system('apt-get install dotnet-sdk-3.1') # This version is necessary for Covenant
	os.system('apt-get install apt-transport-https')
	os.system('pip3 install mitm6')
	# Tools 0.5 (Removed HiddenEye, Added Infoga, Rubeus,Phantom Evasion, MailSniper)
	# Added Various tools and fixed a few commands
	subprocess.call(['git', 'clone', 'https://github.com/1N3/Sn1per.git'])
	subprocess.call(['git', 'clone', 'https://github.com/m8r0wn/CrossLinked.git'])
	subprocess.call(['git', 'clone', 'https://github.com/outflanknl/EvilClippy.git'])
	subprocess.call(['git', 'clone', 'https://github.com/TheWover/donut.git'])
	subprocess.call(['git', 'clone', 'https://github.com/dafthack/DomainPasswordSpray.git'])
	subprocess.call(['git', 'clone', 'https://github.com/outflanknl/RedELK.git'])
	subprocess.call(['git', 'clone', 'https://github.com/GhostPack/Rubeus.git'])
	subprocess.call(['wget', 'https://github.com/BloodHoundAD/BloodHound/releases/download/3.0.4/BloodHound-linux-x64.zip'])
	subprocess.call(['git', 'clone', 'https://github.com/nidem/kerberoast.git'])
	subprocess.call(['git', 'clone', 'https://github.com/dafthack/MailSniper.git'])
	subprocess.call(['git', 'clone', 'https://github.com/oddcod3/Phantom-Evasion.git'])
	subprocess.call(['git', 'clone', 'https://github.com/r00t-3xp10it/venom.git'])
	subprocess.call(['svn', 'checkout', 'https://github.com/mgeeky/Penetration-Testing-Tools/trunk/red-teaming'])
	subprocess.call(['git', 'clone', 'https://github.com/BC-SECURITY/Empire.git'])
	subprocess.call(['git', 'clone', 'https://github.com/sevagas/macro_pack.git'])
	subprocess.call(['git', 'clone', '--recursive', 'https://github.com/cobbr/Covenant.git'])
	subprocess.call(['git', 'clone', 'https://github.com/trustedsec/unicorn.git'])
	subprocess.call(['git', 'clone', 'https://github.com/hlldz/SpookFlare.git'])
	subprocess.call(['git', 'clone', 'https://github.com/Flangvik/NetLoader.git'])
	subprocess.call(['apt', 'install', 'osrframework'])
	subprocess.call(['git', 'clone', 'https://github.com/bitsadmin/wesng.git'])
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
	subprocess.call(['git', 'clone', 'https://github.com/UndeadSec/EvilURL.git'])
	subprocess.call(['git', 'clone', 'https://github.com/Mr-Un1k0d3r/SCT-obfuscator.git'])
	subprocess.call(['git', 'clone', 'https://github.com/api0cradle/UltimateAppLockerByPassList.git'])
	subprocess.call(['git', 'clone', 'https://github.com/ustayready/CredSniper.git'])
	subprocess.call(['git', 'clone', 'https://github.com/m4ll0k/Infoga.git'])
	subprocess.call(['git', 'clone', 'https://github.com/zerosum0x0/koadic.git'])
	subprocess.call(['git', 'clone', 'https://github.com/nins3i/Scriblur.git'])
	subprocess.call(['git', 'clone', 'https://github.com/cwolff411/powerob.git'])
	subprocess.call(['git', 'clone', 'https://github.com/codewhitesec/LethalHTA.git'])
	subprocess.call(['git', 'clone', 'https://github.com/m8r0wn/CrossLinked.git'])
	subprocess.call(['git', 'clone', 'https://github.com/bonnetn/vba-obfuscator.git'])
	subprocess.call(['git', 'clone', 'https://github.com/ch4meleon/vba_obfuscator.git'])
	subprocess.call(['git', 'clone', 'https://github.com/SecureAuthCorp/impacket.git'])
	subprocess.call(['git', 'clone', 'https://github.com/byt3bl33d3r/SprayingToolkit.git'])
	subprocess.call(['git', 'clone', '--recurse-submodules', 'https://github.com/cobbr/Covenant'])
	# This will install Spider requirements
	# subprocess.call(['pip', 'install', '-r', '/opt/spiderfoot/requirements.txt')]
	# Continue with tools
	# Installing packages
elif ready == 'n':
	print ("OK")

