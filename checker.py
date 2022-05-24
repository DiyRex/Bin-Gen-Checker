import requests
from bs4 import BeautifulSoup

def check(bin):
    path = "https://bincheck.org/{0}"
    url = path.format(bin)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.findAll('td')
    try:
        brand = results[1].text.strip()
    except:
        brand = "N/A"
    try:
        type = results[2].text.strip()
    except:
        type = "N/A"
    try:
        catergory = results[3].text.strip()
    except:
        catergory = "N/A"
    try:
        bank = results[4].text.strip()
    except:
        bank = "N/A"
    try:
        bank_url = results[5].text.strip()
    except:
        bank_url = "N/A"
    try:
        country = results[6].text.strip()
    except:
        country = "N/A"
    try:
        country_short = results[7].text.strip()
    except:
        country_short = "N/A"



    json_str = {"Bin": bin,"Type":type, "Brand":brand, "Catergory":catergory, "Bank":bank, "Bank_URL":bank_url, "Country":country, "Country_Short":country_short}

    return json_str
