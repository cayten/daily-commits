from copy import deepcopy

def bubble_sort(arr):
    a = deepcopy(arr)
    steps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a, steps

def insertion_sort(arr):
    a = deepcopy(arr)
    steps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            steps += 1
            a[j+1] = a[j]
            j -= 1
        steps += 1
        a[j+1] = key
    return a, steps

def quick_sort(arr):
    a = deepcopy(arr)
    steps = {"count": 0}
    def _q(l, r):
        if l >= r:
            return
        pivot = a[(l+r)//2]
        i, j = l, r
        while i <= j:
            while a[i] < pivot:
                steps["count"] += 1
                i += 1
            while a[j] > pivot:
                steps["count"] += 1
                j -= 1
            if i <= j:
                steps["count"] += 1
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if l < j: _q(l, j)
        if i < r: _q(i, r)
    _q(0, len(a)-1)
    return a, steps["count"]

def main():
    raw = input("Sıralanacak sayıları gir (ör: 5 3 9 1): ").strip()
    arr = [int(x) for x in raw.split()] if raw else [5,3,9,1,7,2]
    print(f"Girdi: {arr}")
    for name, fn in [("Bubble", bubble_sort), ("Insertion", insertion_sort), ("Quick", quick_sort)]:
        sorted_arr, steps = fn(arr)
        print(f"{name:9}: {sorted_arr} | steps={steps}")

if __name__ == "__main__":
    main()
