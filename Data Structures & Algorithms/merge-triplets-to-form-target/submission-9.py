class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usable = []

        for triplet in triplets:
            add = False
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                add = True
            if add:
                usable.append(triplet)
                            
        max0 = 0
        max1 = 0
        max2 = 0
        for triplet in usable:
            max0 = max(max0, triplet[0])
            max1 = max(max1, triplet[1])
            max2 = max(max2, triplet[2])

        if max0 == target[0] and max1 == target[1] and max2 == target[2]:
            return True
        else:
            return False