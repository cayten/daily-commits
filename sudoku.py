import sys
def read_grid(lines):
    grid=[]
    for ln in lines:
        ln=ln.strip().replace('.','0')
        if not ln: continue
        row=[int(c) for c in ln if c.isdigit()][:9]
        if len(row)==9:
            grid.append(row)
    assert len(grid)==9, 'Need 9 rows.'
    return grid
def valid(grid, r, c, val):
    if any(grid[r][i]==val for i in range(9)): return False
    if any(grid[i][c]==val for i in range(9)): return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if grid[i][j]==val: return False
    return True
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j
    return None
def solve(grid):
    pos=find_empty(grid)
    if not pos: return True
    r,c=pos
    for v in range(1,10):
        if valid(grid,r,c,v):
            grid[r][c]=v
            if solve(grid):
                return True
            grid[r][c]=0
    return False
def show(grid):
    for i,row in enumerate(grid):
        if i%3==0 and i: print('-'*21)
        line=[]
        for j,val in enumerate(row):
            if j%3==0 and j: line.append('|')
            line.append(str(val) if val!=0 else '.')
        print(' '.join(line))
def main():
    grid=read_grid(sys.stdin.readlines())
    print('Input:'); show(grid)
    if solve(grid):
        print('\nSolved:'); show(grid)
    else:
        print('Çözülemedi')
if __name__=='__main__':
    main()
