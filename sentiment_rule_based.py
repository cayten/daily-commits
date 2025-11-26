POSITIVE_WORDS = {
    "good","great","awesome","happy","love","excellent","fantastic","nice","cool","super","amazing"
}
NEGATIVE_WORDS = {
    "bad","terrible","awful","sad","hate","worst","horrible","angry","disappointed","boring"
}

def analyze(text: str) -> dict:
    text_lower = text.lower()
    tokens = [t.strip(".,!?;:") for t in text_lower.split() if t.strip()]
    pos = sum(1 for t in tokens if t in POSITIVE_WORDS)
    neg = sum(1 for t in tokens if t in NEGATIVE_WORDS)
    score = pos - neg
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"
    return {"text": text, "positive": pos, "negative": neg, "score": score, "label": label}

if __name__ == "__main__":
    print("=== Rule-based Sentiment Analyzer ===")
    while True:
        s = input("Metin (çıkmak için boş bırak): ").strip()
        if not s:
            break
        res = analyze(s)
        print(f"Label: {res['label']} | score={res['score']} (pos={res['positive']}, neg={res['negative']})")
        print()
