
import sys, json

def flatten(items):
    rows = []
    for obj in items:
        rows.append({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "age": (obj.get("meta") or {}).get("age")
        })
    return rows

def to_csv(rows):
    if not rows:
        return "id,name,age"
    out = ["id,name,age"]
    for r in rows:
        out.append(f"{r.get('id')},{r.get('name')},{r.get('age')}")
    return "\n".join(out)

def main():
    data = sys.stdin.read()
    items = json.loads(data)
    rows = flatten(items)
    print(to_csv(rows))

if __name__ == "__main__":
    main()
