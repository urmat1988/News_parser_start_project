# Python 3.8.10
# Parses news from web and saves it in json file 
import json, requests

# URL for data parcing
url = 'http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-25'

# Data collecting
response = requests.get(url)
response.raise_for_status()
print(f"Status code: {response.status_code}")

# Load JSON data into a Python variable
response_dict = response.json() 

# Convert a Python value to json file
filename = 'news_parcer_25072022.json'
with open(filename,'w') as file:
	for news in response_dict['data']:
		json.dump(news, file, indent=4, ensure_ascii=False)
	




