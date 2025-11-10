import random, collections
WALL, PATH = '#', ' '
def generate(n=21, m=21):
    n = n if n%2==1 else n+1
    m = m if m%2==1 else m+1
    grid = [[WALL]*m for _ in range(n)]
    def carve(x,y):
        dirs = [(2,0),(-2,0),(0,2),(0,-2)]
        random.shuffle(dirs)
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 1<=nx<n-1 and 1<=ny<m-1 and grid[nx][ny]==WALL:
                grid[x+dx//2][y+dy//2]=PATH
                grid[nx][ny]=PATH
                carve(nx,ny)
    grid[1][1]=PATH
    carve(1,1)
    return grid
def solve(grid):
    n,m=len(grid),len(grid[0])
    start=(1,1); goal=(n-2,m-2)
    q=collections.deque([start]); parent={start:None}
    while q:
        x,y=q.popleft()
        if (x,y)==goal:
            cur=goal
            while cur:
                x,y=cur
                if grid[x][y]==' ': grid[x][y]='.'
                cur=parent[cur]
            return True
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==' ' and (nx,ny) not in parent:
                parent[(nx,ny)]=(x,y)
                q.append((nx,ny))
    return False
def show(grid):
    for row in grid:
        print(''.join(row))
def main():
    grid=generate(21,21)
    solve(grid)
    show(grid)
if __name__=='__main__':
    main()
