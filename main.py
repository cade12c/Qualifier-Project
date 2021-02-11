import requests
from bs4 import BeautifulSoup
#import lxml

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'
}

puppies = requests.get("https://www.reddit.com/r/puppies/")

#response = requests.get(puppies, headers=headers)

soup = BeautifulSoup(puppies.content, "html.parser")

title = soup.find_all(class_ = "_eYtD2XCVieq6emjKBH3m")

comment = soup.find_all(class_ = "FHCV02u6Cp2zYL0fhQPsO")

upvote = soup.find_all(class_ = "_1E9mcoVn4MYnuBQSVDt1gC")

for info in title:
  print(info.get_text().strip())
  
for info in comment:
  print(info.get_text().strip())

for info in upvote:
  print(info.get_text().strip())







