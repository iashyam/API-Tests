import requests
from bs4 import BeautifulSoup
import re

#all the urls here are wrt this base url
base_url = 'https://www.googleapis.com/blogger/v3'

#retriving the blog id
with open('blog_id.txt', 'r') as f:
    blogid = f.read()

#retriving the auth_key
with open('api_key', 'r') as f:
    api_key = f.read()

base_url += '/blogs/' + blogid

# print(response.status_code)
# print(response.json())

#getting the posts
url = base_url +  f"/posts?key={api_key}&maxResults=500"


items = []

while url:
      response = requests.get(url)
      data = response.json()
      items.extend(data['items'])
      url = data.get('nextPageToken')


count = 0
# print(items[0].keys())
print(len(items))
for item in items:

      try:

            if 'Poem' in item['labels']:
                  html_content = str(item['content']).split('</a>')
                  lines = html_content[1].replace('</div><div>', '\n')
                  lines = lines.replace('<div>', '\n')    
                  lines = lines.replace('</div>', '\n')    
                  lines = lines.replace('<br>', '\n')
                  lines = lines.replace('<br />', '\n')
                  lines = lines.replace('&nbsp', '')
                  lines = lines.replace('<div style="text-align: left;">', "")
                  lines = lines.replace(';', '')
                  while lines.count('\n\n\n')!= 0:
                        lines = lines.replace('\n\n\n', '\n\n')
                  
                  lines.strip()
                  
                  title = str(item['title'])
                  with open(title+'.txt', 'w') as f:
                        f.write(title)
                        f.write(lines)

                  soup = BeautifulSoup(html_content[0], 'html.parser')
                  img = soup.find_all('img')
                  with open(item['title']+'link', 'w') as f:
                        f.write(img[0]['src'])

                  
                  count += 1
      except IndexError:
            with open('wihtout images', 'a') as i:
                  i.write(item['title'])
                  i.write('\n')


print(count)