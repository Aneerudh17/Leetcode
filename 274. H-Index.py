class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i,value in enumerate(citations):
            if value >= i+1:
                h_index = i+1
            else:
                break
        return h_index