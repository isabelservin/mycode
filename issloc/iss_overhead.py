#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

def getLat():
    while True:
        try:
            lat = float(input('Enter latitude: '))
        except ValueError:
            print('ERROR! Enter a valid latitude')
            continue
        else:
            return lat

def getLon():
    while True:
        try:
            lon = float(input('Enter longitude: '))
        except ValueError:
            print('ERROR! Enter a valid longitude')
            continue
        else:
            return lon


def main():
    """your code goes below here"""
    

    #query params for lat & longitude
    query = {'lat': getLat(), 'lon': getLon()}
    
    #get request to api w/query params
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=query)
   
    # stuck? you can always write comments
    # Try describe the steps you would take manually

    print(response.json())

if __name__ == "__main__":
    main()

