import requests

test_link = "https://en.wikipedia.org/wiki/Main_Page"
my_req = requests.get(url=test_link)
print(my_req.content)
my_req.
