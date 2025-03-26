class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        chocolate = [1]*n

        for i in range(1,len(ratings)):
            if ratings[i]> ratings[i-1]:
                chocolate[i] = chocolate[i-1]+1
            
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]> ratings[i+1]:
                chocolate[i] = max(chocolate[i],chocolate[i+1]+1)
        count = sum(chocolate)
        return count