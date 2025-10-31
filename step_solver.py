def explain_addition(a: int, b: int):
    """
    Explain column addition step by step.
    """
    a_str = str(a)[::-1]
    b_str = str(b)[::-1]
    carry = 0
    steps = []
    for i in range(max(len(a_str), len(b_str))):
        da = int(a_str[i]) if i < len(a_str) else 0
        db = int(b_str[i]) if i < len(b_str) else 0
        total = da + db + carry
        digit = total % 10
        carry = total // 10
        steps.append({
            "position": i,
            "a_digit": da,
            "b_digit": db,
            "sum_no_carry": da + db,
            "incoming_carry": carry if total>=10 else 0,
            "out_digit": digit,
            "new_carry": carry
        })
    if carry:
        steps.append({
            "position": len(steps),
            "a_digit": 0,
            "b_digit": 0,
            "sum_no_carry": 0,
            "incoming_carry": carry,
            "out_digit": carry,
            "new_carry": 0
        })
    return steps

def pretty_print(a,b,steps):
    print(f"Adding {a} + {b}")
    for s in steps:
        pos = s['position']
        print(f"- Column {pos}: {s['a_digit']} + {s['b_digit']} -> write {s['out_digit']}, carry {s['new_carry']}")

if __name__ == "__main__":
    a = int(input("First number: "))
    b = int(input("Second number: "))
    st = explain_addition(a,b)
    pretty_print(a,b,st)
