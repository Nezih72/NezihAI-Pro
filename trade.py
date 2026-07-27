class TradePlan:

    def __init__(self, entry, stop, tp1, tp2):

        self.entry = entry
        self.stop = stop
        self.tp1 = tp1
        self.tp2 = tp2

    def show(self):

        print("📊 İşlem Planı")
        print(f"Giriş : {self.entry}")
        print(f"Stop  : {self.stop}")
        print(f"TP1   : {self.tp1}")
        print(f"TP2   : {self.tp2}")
