import requests as  r
import bs4
import datetime
import time
import schedule

product_list = ['B0C5Y3JBC4','B0BSTX788T']
base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/dp/'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
base_response = r.get(url, headers=headers)
cookies = base_response.cookies

def track_prices():
    print(datetime.datetime.now())
    for prod in product_list:
        product_response = r.get(url+prod, headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(product_response.text, features='lxml')
        price_lines = soup.findAll(class_="a-price-whole")
        final_price =str(price_lines[0])
        final_price = final_price.replace('<span class="a-price-whole">', '')
        final_price = final_price.replace('<span class="a-price-decimal">.</span></span>', '')

        print(url+prod, final_price)

schedule.every(1).minutes.do(track_prices)

while True:
    schedule.run_pending()
    time.sleep(1)
