import requests

OFFICES = ['Шереметьево', 'Лондон', 'Череповец']


def main(OFFICES):
    for office in OFFICES:
        url = 'https://wttr.in/' + office + '?n?q?T?m?M&lang=ru'
        requests.get(url)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    main(OFFICES)
