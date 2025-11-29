import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_faq(path="faq_data.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_index(faq):
    questions = [item["q"] for item in faq]
    vec = TfidfVectorizer()
    X = vec.fit_transform(questions)
    return vec, X

def find_best_answer(user_q, faq, vec, X, threshold=0.2):
    q_vec = vec.transform([user_q])
    sims = cosine_similarity(q_vec, X)[0]
    best_idx = sims.argmax()
    best_score = sims[best_idx]
    if best_score < threshold:
        return None, best_score
    return faq[best_idx], best_score

if __name__ == "__main__":
    faq = load_faq()
    vec, X = build_index(faq)
    print("=== FAQ Retrieval Bot ===")
    print("Ask something (empty to exit).")
    while True:
        q = input("You: ").strip()
        if not q:
            break
        best, score = find_best_answer(q, faq, vec, X)
        if best is None:
            print("Bot: Sorry, I am not sure about that.
")
        else:
            print(f"Bot (score={score:.2f}): {best['a']}\n")
