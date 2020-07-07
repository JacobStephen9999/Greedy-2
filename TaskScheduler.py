#Time Complexity : O(N) where N is number of elemeents
#Space Complexity :O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencyMap = {}
        maxFreq = 0
        maxFreqCount = 0
        N = len(tasks)
        for task in tasks:
            if task in frequencyMap:
                frequencyMap[task] += 1
            else:
                frequencyMap[task] = 1

            if frequencyMap[task] > maxFreq:
                maxFreq = frequencyMap[task]
                maxFreqCount = 1

            elif frequencyMap[task] == maxFreq:
                maxFreqCount += 1
     
        partitionsCount = maxFreq - 1
        emptySlots = partitionsCount * (n - (maxFreqCount - 1))
        pendingTasks = N - (maxFreq * maxFreqCount)
        idleSlots = max(0, emptySlots - pendingTasks)
        return N + idleSlots 