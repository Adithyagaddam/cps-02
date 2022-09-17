class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        listToStr = ''.join([str(elem) for i,elem in enumerate(digits)])
        s=int(listToStr)
        k=s+1
        res = [int(x) for x in str(k)]
        return res
