import newspaper
import test

article = newspaper.Article("http://investorplace.com/2017/03/general-electric-company-ge-stock-should-nelson-peltz-just-quit/")
article.download()
article.parse()	
print article.authors
print article.publish_date
print article.text
print article.top_image
print test.sentiment(article.text)
# print article.movies
# article.nlp()
# print article.keywords
# print article.summary