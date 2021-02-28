# This can probably be used later to obfuscate
# SImple POC does not Bypass NADA

print("""
__________    ________________
\______   \  /  _  \__    ___/
 |    |  _/ /  /_\  \|    |   
 |    |   \/    |    \    |   
 |______  /\____|__  /____|   
        \/         \/         
  ________                                   __                
 /  _____/  ____   ____   ________________ _/  |_  ___________ 
/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
""")

bat_n = input ("File Name >> ")

bat_payload = bat_n + ".bat"

bat = "@echo OFF\n"
bat +="C:\\Windows\\System32\\cmd.exe"

batf = open(bat_payload, 'w')
batf.write(bat)
batf.close()

print("File saved as: " + bat_payload)

