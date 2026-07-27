def generate_signal(rsi, macd, macd_signal):

    if rsi < 35 and macd > macd_signal:
        return "🟢 AL"

    elif rsi > 70 and macd < macd_signal:
        return "🔴 SAT"

    else:
        return "🟡 BEKLE"
