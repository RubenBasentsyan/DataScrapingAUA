import requests
import googlemaps


API_Key = "AIzaSyDcoGX7SNG-DwnRiCN52d8mtsaRBqDkT00"
regions = ['Երևան','Աշտարակ','Արտաշատ','Արմավիր','Գավառ','Հրազդան','Վանաձոր','Գյումրի','Կապան','Իջևան','Եղեգնաձոր']

pairs = [[regions[p1],regions[p2]] for p1 in range(len(regions)) for p2 in range(p1+1, len(regions))]

def get_distance(start, end, API_KEY):
    page = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={start}&destinations={end}&key={API_KEY}")
    response = page.json()
    print(f'The distance between {start} and {end} is {response["rows"][0]["elements"][0]["distance"]["text"]}')

for sublist in pairs:
    get_distance(sublist[0],sublist[1],API_Key)

