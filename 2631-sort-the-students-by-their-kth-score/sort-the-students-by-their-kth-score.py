class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Sort the matrix rows based on the element at index k in reverse (descending) order
        score.sort(key=lambda x: x[k], reverse=True)
        return score