import webbrowser
import sys
import pyperclip


url = 'https://landdirect.ie'
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print(address)
address = 'https://www.google.com.br/maps/place/' + address
print(address)
print(sys.argv)

webbrowser.get(
    'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(address)
