'''
2d matrix as input
maximum size of a rectange formed ny 1s  as output
'''
def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j]+=1
            area = self.helper(heights)
            res = max(res, area)
        return res
    
def helper(self, heights):
    #stack  O(n)
    stack = [-1]
    heights.append(0)
    res = 0
    for i in range(len(heights)):
        while heights[i]<heights[stack[-1]]:
            height = heights[stack.pop()]
            left = stack[-1]
            area = height*(i-left-1)
            res = max(res, area)
        stack.append(i)
    return res

#driver
#get input and call the function
