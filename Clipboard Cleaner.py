import pyperclip
import re

#a = recurring IP addresses which don't need to be investigated (yandexbot, googlebot, ldsbot, automated access)
a = []
x = pyperclip.paste()
z = ""
final = ""

#Extract src from WAF_task_related page
for i in x.splitlines():
    y = i.strip().split()
    if y[0] not in a:
        z += y[0] + "\r\n"

pyperclip.copy(z)