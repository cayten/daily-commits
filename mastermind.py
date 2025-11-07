import random

def feedback(secret, guess):
    bulls = sum(s==g for s,g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in '0123456789') - bulls
    return bulls, cows

def main():
    secret = ''.join(random.sample('0123456789', 4))
    print('=== CAYTEN Mastermind ===')
    print('4 farklı rakamdan oluşan sayıyı tahmin et')
    tries = 0
    while True:
        guess = input('Tahmin (4 farklı rakam): ').strip()
        if len(guess)!=4 or not guess.isdigit() or len(set(guess))!=4:
            print('Geçersiz. 4 benzersiz rakam gir.')
            continue
        tries += 1
        b,c = feedback(secret, guess)
        print(f'Bulls: {b} | Cows: {c}')
        if b==4:
            print(f'Tebrikler! {tries} denemede bildin.')
            break

if __name__=='__main__':
    main()
