def caesar(text, shift=3, decode=False):
    if decode: shift = -shift
    out=[]
    for ch in text:
        if ch.isalpha():
            base='A' if ch.isupper() else 'a'
            out.append(chr((ord(ch)-ord(base)+shift)%26+ord(base)))
        else:
            out.append(ch)
    return ''.join(out)
def vigenere(text, key, decode=False):
    out=[]; k=[(ord(c.lower())-97)%26 for c in key if c.isalpha()]
    j=0
    for ch in text:
        if ch.isalpha():
            base='A' if ch.isupper() else 'a'
            s = k[j%len(k)]*( -1 if decode else 1)
            out.append(chr((ord(ch)-ord(base)+s)%26+ord(base)))
            j+=1
        else:
            out.append(ch)
    return ''.join(out)
def demo():
    msg='Meet me at the park at eleven.'
    print('Caesar enc:', caesar(msg, 5))
    print('Vigenere enc:', vigenere(msg, 'lemon'))
if __name__=='__main__':
    demo()
