def binary_search(arr, target):
    lo, hi = 0, len(arr)-1
    steps = []
    while lo <= hi:
        mid = (lo + hi) // 2
        steps.append((lo, mid, hi, arr[mid]))
        if arr[mid] == target:
            return mid, steps
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps

def main():
    print("=== Binary Search Explorer ===")
    arr = list(range(0, 101, 5))
    print("Array:", arr)
    target = int(input("Aranan değer: "))
    idx, steps = binary_search(arr, target)
    for i, (lo, mid, hi, mid_val) in enumerate(steps, start=1):
        print(f"Step {i}: lo={lo}, mid={mid}, hi={hi}, arr[mid]={mid_val}")
    if idx != -1:
        print(f"Sonuç: {target} bulundu, index={idx}")
    else:
        print("Sonuç: bulunamadı.")

if __name__ == "__main__":
    main()
