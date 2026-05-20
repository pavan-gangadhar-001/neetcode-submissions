class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        defaultdict = {}
        for num in nums:
            defaultdict[num] = 1 + defaultdict.get(num,0)
        sorted_dict = dict(sorted(defaultdict.items(), key=lambda item: item[1]))
        l = list(sorted_dict.keys())
        return l[-k:]







