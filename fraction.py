import math

def simplify(n,d):
    g = math.gcd(n,d)
    return n//g, d//g

if __name__ == "__main__":
    raw = input("Enter fraction (a/b): ").strip()
    a,b = raw.split("/")
    a=int(a); b=int(b)
    sn, sd = simplify(a,b)
    print(f"Simplified: {sn}/{sd}")
