import random

def ask_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+','-'])
    if op == '+':
        correct = a + b
    else:
        correct = a - b
    answer = input(f"{a} {op} {b} = ")
    try:
        user_val = int(answer)
    except ValueError:
        print("Please enter a number.")
        return False
    if user_val == correct:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Nope. Right answer is {correct}.")
        return False

def main():
    print("=== CAYTEN Day1 Arithmetic Trainer ===")
    score = 0
    for i in range(5):
        if ask_question():
            score += 1
    print(f"Your score: {score}/5")

if __name__ == "__main__":
    main()
