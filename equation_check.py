def check_equation(a,b,c,x):
    left = a*x + b
    right = c
    return left == right, left, right

if __name__ == "__main__":
    print("Solve ax + b = c")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = float(input("Proposed x: "))
    ok, L, R = check_equation(a,b,c,x)
    if ok:
        print(f"✅ {x} works because {L} = {R}")
    else:
        print(f"❌ {x} does NOT work because {L} != {R}")
