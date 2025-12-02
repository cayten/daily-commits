from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EXAMPLES = [
    ("hello", "greeting"),
    ("hi there", "greeting"),
    ("good morning", "greeting"),
    ("what is the weather today", "weather"),
    ("is it going to rain", "weather"),
    ("will it be sunny tomorrow", "weather"),
    ("i need some help", "help"),
    ("can you assist me", "help"),
    ("i don't understand this feature", "help"),
]

KEYWORDS = {
    "greeting": {"hello", "hi", "hey"},
    "weather": {"weather", "rain", "sunny"},
    "help": {"help", "assist", "support"},
}

def train():
    texts, labels = zip(*EXAMPLES)
    vec = TfidfVectorizer()
    X = vec.fit_transform(texts)
    return vec, X, labels

def keyword_hint(text: str):
    words = set(text.lower().split())
    for intent, keys in KEYWORDS.items():
        if words & keys:
            return intent
    return None

def classify(text: str, vec, X, labels, threshold=0.25):
    kw = keyword_hint(text)
    v = vec.transform([text])
    sims = cosine_similarity(v, X)[0]
    best_idx = sims.argmax()
    best_score = sims[best_idx]
    intent = labels[best_idx]
    if best_score < threshold and kw is None:
        return "other", best_score, kw
    return intent, best_score, kw

if __name__ == "__main__":
    print("=== Tiny Intent Classifier ===")
    vec, X, labels = train()
    while True:
        s = input("User: ").strip()
        if not s:
            break
        intent, score, kw = classify(s, vec, X, labels)
        print(f"Intent: {intent} (score={score:.2f}, keyword_hint={kw})\n")
