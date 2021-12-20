import requests


def unshorten():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'}
    api_url = "https://unshorten.me/json/"
    print("Enter shorten link: ", end = '')
    slink = input()
    url = api_url + slink
    r = requests.get(url=url, headers=header).json()
    print (f"Unshorten url: {r['resolved_url']}")


if __name__ == '__main__':
    unshorten()
