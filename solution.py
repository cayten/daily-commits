
from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    seen = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            i = seen[need]
            return (i, j) if i < j else (j, i)
        seen[x] = j
    return (-1, -1)

def main():
    import sys
    data = sys.stdin.read().strip().splitlines()
    target = int(data[0].strip())
    nums = list(map(int, data[1].split()))
    i, j = two_sum(nums, target)
    if i == -1:
        print(-1)
    else:
        print(i, j)

if __name__ == "__main__":
    main()
