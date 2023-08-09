class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
      # Keys are the unique number, and Values is frequency
        indice = [[] for i in range(len(nums) + 1)]
      # this array is going to be used for bucket sort

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for key, v in count.items():
            indice[v] += [key]
        
        res = []
        for i in range(len(indice) - 1, 0, -1):
            for j in indice[i]:
                if len(res) < k:
                    res.append(j)
                
        return res

        
