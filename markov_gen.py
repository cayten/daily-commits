import random

def build_model(tokens, order=2):
    model = {}
    for i in range(len(tokens) - order):
        key = tuple(tokens[i:i+order])
        nxt = tokens[i+order]
        model.setdefault(key, []).append(nxt)
    return model

def generate(model, order=2, length=20):
    if not model:
        return ""
    start = random.choice(list(model.keys()))
    out = list(start)
    for _ in range(length - order):
        key = tuple(out[-order:])
        options = model.get(key)
        if not options:
            break
        out.append(random.choice(options))
    return " ".join(out)

if __name__ == "__main__":
    with open("corpus.txt", "r", encoding="utf-8") as f:
        text = f.read().strip().replace("\n", " ")
    tokens = [t for t in text.split() if t]
    model = build_model(tokens, order=2)
    print("=== Markov Text Generator ===")
    for _ in range(3):
        print("-", generate(model, order=2, length=15))
