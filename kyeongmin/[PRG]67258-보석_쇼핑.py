#일부 오류가 있는 소스코드. 87점

def solution(gems):

    gem_list = set(gems)
    n = len(gems) # n = 8
    i, j = 0, 0
    temp = []

    gem_dict = dict()
    for gem in gem_list :
        gem_dict[gem] = 0

    def check(gem_dict) :
        if 0 in gem_dict.values() :
            return False
        else :
            return True 


    while j < n : 
        if check(gem_dict) == False : 
            gem_dict[gems[j]] += 1
            j += 1

        else :
            temp.append([j-i,i+1,j])
            gem_dict[gems[i]] -= 1
            i += 1
    temp.append([j-i,i+1,j])
    
    temp.sort(key=lambda x : (x[0],x[1],x[2]))
    return(temp[0][1:3])