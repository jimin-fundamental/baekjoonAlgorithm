def solution(n):
    def is_safe(loc, row, col):
        for r,c in enumerate(loc[:row]):
            if col == c or abs(r-row) == abs(c-col):
                return False
        return True
        
    
    def place_queen(loc, row):
        count = 0
        if row == n:
            return 1
        for col in range(n):
            if is_safe(loc,row,col):
                loc[row] = col
                count += place_queen(loc, row+1)
        return count
       
    loc = [-1]*n
    return place_queen(loc, 0)