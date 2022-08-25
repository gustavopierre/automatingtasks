# Open google in python - Windows
import webbrowser


url = 'https://landdirect.ie'
webbrowser.get(
    'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

webbrowser.open_new_tab(url)
