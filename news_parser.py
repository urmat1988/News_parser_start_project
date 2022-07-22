import json, requests

# URL for data parcing
url = 'http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-22'

# Data collecting
response = requests.get(url)
response.raise_for_status()
print(f"Status code: {response.status_code}")

# Load JSON data into a Python variable
response_dict = response.json() 

# Convert a Python value into JSON-formatted data
for news in response_dict['data']:
	readable_news = json.dumps(news, indent=4, ensure_ascii=False)
	print(readable_news)




