import json

def run_quiz(path="questions.json"):
    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)
    score = 0
    for q in data["questions"]:
        print(q["prompt"])
        ans = input("Your answer: ").strip()
        if ans == str(q["answer"]).strip():
            print("✅ Correct")
            score += 1
        else:
            print(f"❌ Correct answer is {q['answer']}")
        print()
    print(f"Final score: {score}/{len(data['questions'])}")

if __name__=="__main__":
    run_quiz()
