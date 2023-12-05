import re
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def scrape_data(url: str, proxy=None) -> dict:
    '''
    returns title and price of a product given the daraz link
    '''
    try:
        headers = {'User-Agent': UserAgent().random}
        markup = requests.get(
            url,
            timeout=20,
            proxies=None if proxy is None else {'https': proxy, 'http': proxy},
            headers=headers
        ).text
        soup = BeautifulSoup(markup, 'lxml')

        script = soup.find('script', type='text/javascript').string
        if script is None:
            return {'error': 'Not a daraz link'}

        data = re.search("\"{.*}\"", script)
        if data is None:
            return {'error': 'Error finding the data'}

        data_string = json.loads(data.group())
        data = json.loads(data_string)

        title = data.get("pdt_name")
        price_str = data.get("pdt_price")
        discount_str = data.get("pdt_discount")
        image_url = data.get("pdt_photo")

        price = int(re.search(r"\d.*\d", price_str).group().replace(',', ''))
        if discount_str:
            discount = int(re.search(r"\d\d*", discount_str).group())
        else:
            discount = 0

        real_price = price * (1 - discount / 100)

        return {
            'url': url,
            'title': title,
            'price': real_price,
            'image_url': image_url
        }
    except requests.exceptions.ProxyError as e:
        print(f"ProxyError: {e}")
        return {'error': 'ProxyError'}

def get_proxies() -> list:
    h = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(h, 'lxml')
    data = soup.find('textarea', class_='form-control').string
    proxies = re.findall(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*:[0-9]*', data)
    return proxies

# Rotate proxies function
def rotate_proxies(proxies):
    while True:
        yield proxies.pop(0)
        proxies.append(proxies[0])

# Example usage
daraz_url = 'https://www.daraz.com.np/products/multipurpose-egg-boilerfood-steamer-350w-assorted-colors-i100068007-s1020318008.html?spm=a2a0e.searchlistcategory.sku.3.35487b31PQhpiZ&search=1'
proxies = get_proxies()
proxy_rotator = rotate_proxies(proxies)

result = scrape_data(daraz_url, next(proxy_rotator))
print(result)

