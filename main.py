from scanner import get_prices

print("=" * 40)
print("       NEZİH AI PRO v1.0")
print("=" * 40)

try:
    prices = get_prices()

    for coin in prices:
        print(
            f"{coin['coin']:5} | "
            f"Fiyat: {coin['price']} TL | "
            f"24s: {coin['change']}%"
        )

except Exception as e:
    print("Hata oluştu:", e)
