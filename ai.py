def ai_score(rsi, macd, macd_signal):

    score = 50

    # RSI
    if rsi < 30:
        score += 20
    elif rsi < 40:
        score += 10
    elif rsi > 70:
        score -= 20

    # MACD
    if macd > macd_signal:
        score += 15
    else:
        score -= 15

    # Sınırlar
    score = max(0, min(score, 100))

    return score


def recommendation(score):

    if score >= 80:
        return "🟢 GÜÇLÜ AL"

    elif score >= 60:
        return "🟢 AL"

    elif score >= 40:
        return "🟡 BEKLE"

    elif score >= 20:
        return "🔴 SAT"

    else:
        return "🚨 GÜÇLÜ SAT"
