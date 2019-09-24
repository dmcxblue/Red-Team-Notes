#/usr/bin/python3

import subprocess
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest='interface', help='Interface toc hange mac')
	parser.add_option('-m', '--mac', dest='new_mac', help='New mac to change')
	(options, arguments) = parser.parse_args()
	if not options.interface:
		# Code to handle error
		parser.error('[-] Please specify the interface, use --help for info')
	elif not options.new_mac:
		# Code to Handle error
		parser.error('[-] Please specify the new mac address, use --help for help')
	return options

def change_mac(interface, new_mac):
	print('[+]Changing MAC {} to {}'.format(interface,new_mac))
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
	subprocess.call(['ifconfig', interface, 'up'])

options = get_arguments()
change_mac(options.interface, options.new_mac)
