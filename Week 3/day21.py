# Introduction

# https://en.wikipedia.org/wiki/Python_(programming_language)

import requests

# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# response = requests.get(url)

# if response.status_code == 200:
#     print(response.text[:500])
# else:
#     print(f"Failed to retreive data. Status Code: {response.status_code}")

from bs4 import BeautifulSoup

html_content = "<h1>Main Tittle</h1> <p>This is a sample paragraph</p> <a href='https://example.com'>Click Here</a>"
soup = BeautifulSoup(html_content, "html.parser")

print(soup.h1.text)
print(soup.p.text)
print(soup.a.text)
print(soup.a.link)