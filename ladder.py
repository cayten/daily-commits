import sys, collections
def neighbors(word, wordset):
    for i in range(len(word)):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch!=word[i]:
                w = word[:i]+ch+word[i+1:]
                if w in wordset:
                    yield w
def bfs(start, end, wordset):
    q = collections.deque([start])
    parent = {start: None}
    while q:
        w = q.popleft()
        if w == end:
            path = []
            while w is not None:
                path.append(w)
                w = parent[w]
            return list(reversed(path))
        for nb in neighbors(w, wordset):
            if nb not in parent:
                parent[nb] = w
                q.append(nb)
    return None
def main():
    if len(sys.argv)<3:
        print('Usage: python ladder.py start end')
        return
    start, end = sys.argv[1].lower(), sys.argv[2].lower()
    with open('words.txt','r',encoding='utf-8') as f:
        words = {w.strip().lower() for w in f if len(w.strip())==len(start)}
    if start not in words or end not in words:
        print('Start/end sözlükte yok.')
        return
    path = bfs(start,end,words)
    if path:
        print(' → '.join(path))
    else:
        print('Yol bulunamadı.')
if __name__=='__main__':
    main()
