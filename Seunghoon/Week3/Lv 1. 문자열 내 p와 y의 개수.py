def solution(s):
    p = 0
    y = 0
    s = str(s).lower()
    for i in range(len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i] == 'y':
            y += 1
            
    if p == y:
        return True
    
    else: return False
    