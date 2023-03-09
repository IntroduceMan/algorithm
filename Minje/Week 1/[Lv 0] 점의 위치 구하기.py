def solution(dot):
    bi = [0]
    if(dot[0]>bi[0] and dot[1]>bi[0]):
        return 1
    elif(dot[0]<bi[0] and dot[1]>bi[0]):
        return 2
    elif(dot[0]<bi[0] and dot[1]<bi[0]):
        return 3
    else:
        return 4