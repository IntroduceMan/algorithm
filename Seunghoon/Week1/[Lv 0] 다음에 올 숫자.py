def solution(common):
    a = common[1]-common[0]
    
    if(common[1] + a == common[2]):
        return common[len(common)-1] + a
    
    else : 
        return common[len(common)-1] * (common[1] // common[0])

solution 
