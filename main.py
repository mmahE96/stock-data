from urllib3.util import url
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_NEWS = "0a71c46da2044ceba7c7ab06ec301d18"
API_KEY_STOCK = "NSKSUUWQKZV4PQPR"



response_stocks = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=NSKSUUWQKZV4PQPR")

response_stocks.raise_for_status()

stock_news = response_stocks.json()["Time Series (Daily)"]
print("Tesla stocks:")
working_stock = [value for (key, value) in stock_news.items()]
yesterday_stock_price = working_stock[0]
before_yesterday_stock_price_onclose = working_stock[1]["4. close"]
yesterday_stock_price_onclose = yesterday_stock_price["4. close"]


difference = abs(float(yesterday_stock_price_onclose) - float(before_yesterday_stock_price_onclose))
percentage_ofchange = (difference / float(yesterday_stock_price_onclose))*100

rounded_percentage_ofchange = round(percentage_ofchange, 2)
if percentage_ofchange>5:
    response_news = requests.get(url=NEWS_ENDPOINT + f"?q=tesla&apiKey={API_KEY_NEWS}")

    response_news.raise_for_status()

    articles = response_news.json()["articles"]
    three_articles = articles[:3]
    print("Tesla news:")




    new_array = [f"Heading: {article['title']}. \nContent:{article['description']}" for article in three_articles]
    print(new_array)

    string_percentage = str(rounded_percentage_ofchange) + "%"
    print(string_percentage)






