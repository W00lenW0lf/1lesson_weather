import requests

PAYLOAD = {"n": "", "q": "", "T": "", "m": "", "lang": "ru"}
OFFICES = ['Шереметьево', 'Лондон', 'Череповец']


def main(payload, offices):
    for city in offices:
        response = requests.get(f'https://wttr.in/{city}', params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main(PAYLOAD, OFFICES)