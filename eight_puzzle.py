import sys, heapq
GOAL=(1,2,3,4,5,6,7,8,0)
def manhattan(state):
    d=0
    for i,v in enumerate(state):
        if v==0: continue
        gi=v-1
        x,y=i//3,i%3
        gx,gy=gi//3,gi%3
        d+=abs(x-gx)+abs(y-gy)
    return d
def neighbors(state):
    i=state.index(0); x,y=i//3,i%3
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            j=nx*3+ny
            arr=list(state)
            arr[i],arr[j]=arr[j],arr[i]
            yield tuple(arr)
def astar(start):
    pq=[]; heapq.heappush(pq,(manhattan(start),0,start,None))
    seen={start:(0,None)}
    while pq:
        f,g,s,parent=heapq.heappop(pq)
        if s==GOAL:
            path=[]; cur=s
            while cur is not None:
                path.append(cur); cur=seen[cur][1]
            return list(reversed(path))
        for nb in neighbors(list(s)):
            ng=g+1
            if nb not in seen or ng<seen[nb][0]:
                seen[nb]=(ng,s)
                heapq.heappush(pq,(ng+manhattan(nb),ng,nb,s))
    return None
def main():
    if len(sys.argv)<2:
        print('Usage: python eight_puzzle.py "1 2 3 4 0 6 7 5 8"')
        return
    start=tuple(int(x) for x in sys.argv[1].split())
    path=astar(start)
    if not path:
        print('Çözüm yok veya çok zor.')
        return
    for p in path:
        print(f"{p[0]} {p[1]} {p[2]}\n{p[3]} {p[4]} {p[5]}\n{p[6]} {p[7]} {p[8]}\n")
    print(f'Adım sayısı: {len(path)-1}')
if __name__=='__main__':
    main()
