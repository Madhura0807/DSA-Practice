class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # Create a row of 1s with length (i + 1)
            row = [1] * (i + 1)
            
            # Fill middle elements using values from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)

        return triangle