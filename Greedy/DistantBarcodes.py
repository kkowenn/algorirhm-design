'''
1054. Distant Barcodes
Medium

Topics
Companies

Hint
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.
 You may return any answer, and it is guaranteed an answer exists.



Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]


Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''
import collections
import itertools

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        k = 2
        cnts = collections.Counter(barcodes)
        bucket_cnt = max(cnts.values())
        result = [0] * len(barcodes)
        i = (len(barcodes) - 1) % k
        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):
            for _ in range(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = (i - 1) % k
        return result

class Solution2(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        cnts = collections.Counter(barcodes)
        sorted_cnts = [[v, k] for k, v in cnts.items()]
        sorted_cnts.sort(reverse=True)

        i = 0
        for v, k in sorted_cnts:
            for _ in range(v):
                barcodes[i] = k
                i += 2
                if i >= len(barcodes):
                    i = 1
        return barcodes

barcodes1 = [1,1,1,2,2,2]
barcodes2 = [1,1,1,1,2,2,3,3]

solution_instance = Solution()
result1 = solution_instance.rearrangeBarcodes(barcodes1)
result2 = solution_instance.rearrangeBarcodes(barcodes2)
print(result1, result2)

solution_instance2 = Solution2()
result1 = solution_instance2.rearrangeBarcodes(barcodes1)
result2 = solution_instance2.rearrangeBarcodes(barcodes2)
print(result1, result2)
