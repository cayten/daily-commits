
def solve(input_data: str) -> str:
    """Çözümünü buraya yaz. input_data metnini al ve çıktı metni döndür."""
    # Örnek: toplam hesapla
    nums = [int(x) for x in input_data.strip().split() if x.strip().lstrip('-').isdigit()]
    return str(sum(nums))

if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(solve(data))
