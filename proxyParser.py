import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def proxy_writer(proxy_list):
    try:
        with open('proxy.txt', 'w') as f:
            for proxy in proxy_list:
                f.write(proxy + '\n')
        print("All proxies were written")
    except Exception:
        print("Proxies were not written to file")


def get_proxy(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        proxies = soup.find('textarea', attrs={'class': 'form-control'})

        """first 3 elements and the last are string and empty string"""

        return proxies.text.split('\n')[3:-1]
    except Exception:
        print("Proxy didn't parsed")


def main():
    url = 'https://free-proxy-list.net/'
    html = get_html(url)
    proxies = get_proxy(html)
    proxy_writer(proxies)


if __name__ == '__main__':
    main()
