class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myDic ={}
        for i in arr:
            if i in myDic:
                myDic[i] +=1
            else:
                myDic[i] = 1
                    
        l = []
        for k,v in myDic.items():
            l.append(v)
        
        s = set(l)
        if len(l) == len(s):
            return True
        else:
            return False
