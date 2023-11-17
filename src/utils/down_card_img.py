import requests

# Check clash royale api documentation to see more options

def download_image(url, filename):
    """Download an image from the given url and save it to 'filename'"""
    response2 = requests.get(url)

    if response2.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response2.content)


api_key = '#########' # Replace '######' with your actual Clash Royale API key
api_url = 'https://api.clashroyale.com/v1/cards' # url to get cards info

headers = {
    'Authorization': f'Bearer {api_key}',
}


response = requests.get(api_url, headers=headers) # Make the API request without the 'limit' parameter to get everything

if response.status_code == 200:
    data = response.json() # Json data
    cards = data.get('items', [])
    
    for card in cards:
        card_name = card['name'] # Get card name
        url2 = card['iconUrls']['medium'] # Get normal card image url
        download_image(url2, f"cards/{card_name}.png") # Download normal card image
        try:
            url3 = card['iconUrls']['evolutionMedium'] # Get evolution card image url
            download_image(url3, f"cards/{card_name} Evolution.png") # Download evolution card image
        except Exception as e:
            print(e)

else:
    print(f"Error: {response.status_code} - {response.text}")


