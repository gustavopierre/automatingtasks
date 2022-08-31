import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print()
print(res.status_code == requests.codes.ok)
print()
print(len(res.text))
print()
print(res.text[:250])
