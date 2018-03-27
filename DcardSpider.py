### reference: https://levirve.github.io/blog/2016/dcard-spider-python-package/
### reference: https://github.com/leVirve/dcard-spider

from dcard import Dcard
import json
#problem:有在total list裡面，卻沒分到任一topic
### Hint: 部選用熱門文章，因為多為舊劇，更多為以前熱門劇延燒討論至今
dcard = Dcard()

#  取得看板最新 50 篇 
metadata_forums = dcard.forums('tvepisode').get_metas(num=20, sort='new')  # default=30, new

ids = [meta['id'] for meta in metadata_forums]
articles = dcard.posts(ids).get()    # or # articles = dcard.posts(metadata_forums).get()

# print(articles)

# 存取 articles 中的內容
# 1. articles.results -> get a `generator()`
# `article` is a Python dict() object
index = 1
for article in articles.results:
	print(index, article['title'])
	index = index + 1
	if len(article['topics']) != 0:
		print('類別: ',article['topics'][0])
	else:
		print('類別: ',article['topics'])
	# for comment in article['comments']:
	# 	print(comment['content'])
	print('--------------------------------') 

#  Dumps all articles data into file directly
# with open('output.json', 'w', encoding='utf-8') as f:
#     json.dump(articles.result(), f, ensure_ascii=False)