import requests

offices = ['svo', 'london', 'cherepovets']
def main(offices):
    for office in offices:
        url = 'https://wttr.in/' + office
        requests.get(url)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    main(offices)
