### reference: https://levirve.github.io/blog/2016/dcard-spider-python-package/
### reference: https://github.com/leVirve/dcard-spider

from dcard import Dcard
import json
#problem:有在total list裡面，卻沒分到任一topic
### Hint: 部選用熱門文章，因為多為舊劇，更多為以前熱門劇延燒討論至今
dcard = Dcard()

#  取得看板最新 50 篇 
metadata_forums = dcard.forums('tvepisode').get_metas(num=500, sort='new')  # default=30, new

ids = [meta['id'] for meta in metadata_forums]
articles = dcard.posts(ids).get()    # or # articles = dcard.posts(metadata_forums).get()

# print(articles)

# 存取 articles 中的內容
# 1. articles.results -> get a `generator()`
# `article` is a Python dict() object

search_query = input("搜尋:")

pushCount = 0
lookFowardToCount = 0

index = 1
for article in articles.results:
	
	if search_query not in article['title']:
		continue
	else:
		if '韓劇' in article['topics']:
			print(index, article['title'])
			print(article['createdAt'])

			for comment in article['comments']: 
				if 'content' in comment:
					# print(comment['content'],'\n')
					if '推' in comment['content']:
						pushCount = pushCount + 1
					if '期待' in comment['content']:
						lookFowardToCount = lookFowardToCount + 1

			index = index + 1

		elif '韓劇' in article['title']:
			print(index, article['title'])
			print(article['createdAt'])

			for comment in article['comments']:
				if 'content' in comment:
					# print(comment['content'],'\n')
					if '推' in comment['content']:
						pushCount = pushCount + 1
					if '期待' in comment['content']:
						lookFowardToCount = lookFowardToCount + 1

			index = index + 1

		print('推:',pushCount, '& 期待:', lookFowardToCount)

	# print('--------------------------------') 

#  Dumps all articles data into file directly
# with open('output1.json', 'w', encoding='utf-8') as f:
#     json.dump(articles.result(), f, ensure_ascii=False)