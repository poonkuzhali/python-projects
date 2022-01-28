from json import JSONDecodeError

import requests
from requests import RequestException, HTTPError


def main():
    print('-----------------------------------')
    print('      WEATHER CLIENT APP')
    print('-----------------------------------')
    location = input('Enter your location eg: New York: ')
    make_api_request(location)


def make_api_request(location):
    json = None
    response = None
    url = 'http://api.weatherstack.com/current'
    params = {'access_key': '20d119f3d7e3b59da5462688f2e83c8c', 'query': location, 'units': 'f'}
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        json = response.json()
        country = json['location']['country']
        temperature = json['current']['temperature']
        weather_description = json['current']['weather_descriptions']
        feels_like = json['current']['feelslike']
        print('Current temperature in {}, {} is {} F but feels like {} F. The weather is described as: {}.'
              .format(location, country, temperature, feels_like, ','.join(weather_description)))
    except HTTPError:
        print("Status code {}.Not a successful request."
              .format(response.status_code))
    except TimeoutError:
        print('Request timed out.')
    except JSONDecodeError:
        print('Error while decoding json. Check the request! Response received {}'.format(json))
    except RequestException:
        print(response.status_code)


if __name__ == '__main__':
    main()
