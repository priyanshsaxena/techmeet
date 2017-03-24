import data_processing

x = open("xyz")
article = x.readlines()
article = " ".join(article)
company_name = "aapl"
up_down = -1  # 1/-1

relevancy = data_processing.relevancy_of_article(company_name,article, up_down)
print (relevancy)