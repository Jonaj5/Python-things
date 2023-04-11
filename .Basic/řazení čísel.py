s=list(map(int,input(" > ").split()))
d=len(s)-1


while d>=0:
    if s[d] < s[d - 3] and d-3>=0:
        s[d], s[d - 3] = s[d - 3], s[d]
    
    if s[d] < s[d - 2] and d-2>=0:
        s[d], s[d - 2] = s[d - 2], s[d]
        
    if s[d] < s[d - 1]:
        s[d], s[d - 1] = s[d - 1], s[d]
    d-=1


print(s)
