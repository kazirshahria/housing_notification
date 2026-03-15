import requests
import json

url = "https://a806-housingconnectapi.nyc.gov/HPDPublicAPI/api/Lottery/SearchLotteries"

payload = json.dumps({
  "UnitTypes": [],
  "NearbyPlaces": [],
  "NearbySubways": [],
  "Amenities": [],
  "Applied": None,
  "HPDUserId": "3667567",
  "Boroughs": [],
  "Neighborhoods": [],
  "HouseholdSize": None,
  "Income": "",
  "HouseholdType": 1,
  "OwnerTypes": [],
  "PreferanceTypes": [],
  "LotteryTypes": [],
  "Min": None,
  "Max": None,
  "RentalSubsidy": None
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://housingconnect.nyc.gov',
  'priority': 'u=1, i',
  'referer': 'https://housingconnect.nyc.gov/',
  'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

sales = None
rentals = None

if response.status_code == 200:
    data = response.json()
    
    sales = data.get('sales')
    rentals = data.get('rentals')
    
    print(f'Sales: {len(sales)}')
    print(f'Rentals: {len(rentals)}')