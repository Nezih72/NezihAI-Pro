import requests
from config import COINS, VS_CURRENCY

def get_prices():

    ids = ",".join(COINS.keys())

    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={ids}"
        f"&vs_currencies={VS_CURRENCY}"
        "&include_24hr_change=true"
    )

    r = requests.get(url, timeout=10)
    data = r.json()

    sonuc = []

    for coin, sembol in COINS.items():

        fiyat = data[coin][VS_CURRENCY]

        degisim = data[coin][f"{VS_CURRENCY}_24h_change"]

        sonuc.append({
            "coin": sembol,
            "price": fiyat,
            "change": round(degisim,2)
        })

    return sonuc


if __name__ == "__main__":

    veriler = get_prices()

    for v in veriler:
        print(
            f"{v['coin']:5}  "
            f"{v['price']} TL   "
            f"{v['change']} %"
        )
