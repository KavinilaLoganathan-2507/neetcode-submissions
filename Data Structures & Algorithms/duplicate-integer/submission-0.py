class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #by using hash set 
        hashset = set()
        #for loop for to find duplicate 
        for n in nums :
            if n in hashset :
                return True 
            hashset.add(n)
        return False