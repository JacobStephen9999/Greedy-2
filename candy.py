#Time Complexity : O(N) where N is number of elemeents
#Space Complexity :O(1)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if (ratings == None or len(ratings) == 0):
            return 0
        candies = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if (ratings[i] > ratings[i - 1]):
                candies[i] = candies[i - 1] + 1

        total = candies[len(ratings) - 1]
        for i in range(len(ratings) - 2, -1, -1):
            if (ratings[i] > ratings[i + 1]):
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total += candies[i]  
        return total 