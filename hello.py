# hello.py
"""
Basit bir dosya: GitHub yeşili için günlük commit.
Çalıştır: python hello.py
"""

def greet(name: str = "Canan"):
    """Kısa ve tatlı bir selam fonksiyonu."""
    return f"Hello, {name}! 🌱"

if __name__ == "__main__":
    print(greet())
