from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAIN_DATA = [
    ("I love this product, it is awesome", "pos"),
    ("This is great and fantastic", "pos"),
    ("Absolutely amazing experience", "pos"),
    ("I am very happy with the service", "pos"),
    ("This is bad and disappointing", "neg"),
    ("I hate it, worst ever", "neg"),
    ("Terrible quality and horrible support", "neg"),
    ("Really boring and not good", "neg"),
]

def train_model():
    texts, labels = zip(*TRAIN_DATA)
    vec = TfidfVectorizer()
    X = vec.fit_transform(texts)
    clf = LogisticRegression()
    clf.fit(X, labels)
    return vec, clf

def predict(vec, clf, text: str):
    X = vec.transform([text])
    label = clf.predict(X)[0]
    prob = max(clf.predict_proba(X)[0])
    return label, prob

if __name__ == "__main__":
    print("=== ML Sentiment Demo (LogReg + TF-IDF) ===")
    vec, clf = train_model()
    while True:
        s = input("Text (empty to exit): ").strip()
        if not s:
            break
        label, prob = predict(vec, clf, s)
        print(f"Predicted: {label} (confidence={prob:.2f})")
        print()
