from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAIN = [
    ("Hello, how are you?", "en"),
    ("This is a small English sentence.", "en"),
    ("I love learning new languages.", "en"),
    ("Merhaba, nasılsın?", "tr"),
    ("Bu küçük bir Türkçe cümledir.", "tr"),
    ("Yeni diller öğrenmeyi seviyorum.", "tr"),
    ("Hola, ¿cómo estás?", "es"),
    ("Esta es una pequeña frase en español.", "es"),
    ("Me encanta aprender nuevos idiomas.", "es"),
]

def train_model():
    texts, labels = zip(*TRAIN)
    vec = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
    X = vec.fit_transform(texts)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, labels)
    return vec, clf

if __name__ == "__main__":
    print("=== Toy Language Detector (en/tr/es) ===")
    vec, clf = train_model()
    while True:
        s = input("Metin (boşsa çıkış): ").strip()
        if not s:
            break
        X = vec.transform([s])
        label = clf.predict(X)[0]
        probs = clf.predict_proba(X)[0]
        conf = max(probs)
        print(f"Predicted: {label} (confidence={conf:.2f})")
        print()
