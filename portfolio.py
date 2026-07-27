class Portfolio:

    def __init__(self):

        self.balance = 0

        self.positions = []

    def add_position(self, coin, amount, buy_price):

        self.positions.append({
            "coin": coin,
            "amount": amount,
            "buy_price": buy_price
        })

    def show(self):

        for p in self.positions:

            print(
                f"{p['coin']} | "
                f"{p['amount']} adet | "
                f"Alış: {p['buy_price']}"
            )
