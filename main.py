import requests
import time
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
time.sleep(30)

# print(r)
print(r.content)