from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.select('span.titleline > a')

article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.get_text())
    article_links.append(article.get('href'))

article_upvotes = [int(score.get_text().split(' ')[0]) for score in soup.select('span .score')]
m = max(article_upvotes)
idx = article_upvotes.index(m)
print(f'{article_texts[idx]} : {m} votes - {article_links[idx]}')











# with open('website.html', 'r', encoding='utf8') as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading.name)

# ul = soup.find(name='ul')
# print(ul.get_text())

# headings = soup.select(selector='.heading')
# text = [t.get_text() for t in headings]
# print(text)
