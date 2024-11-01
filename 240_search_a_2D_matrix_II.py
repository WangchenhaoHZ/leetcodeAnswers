class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        index1head = 0
        index1tail = len(matrix) -1        
        if matrix[index1tail][len(matrix[0]) - 1] > target:
            index2 = len(matrix[0]) - 1
            while index1head < index1tail-1:
                mid = (index1head + index1tail) // 2
                if  matrix[mid][index2] == target: return True
                elif matrix[mid][index2] < target:
                    index1head = mid
                else:
                    index1tail = mid
        elif matrix[index1tail][len(matrix[0]) - 1] == target: return True
        else: return False
        if matrix[index1head][index2] > target: index1 = index1head
        elif matrix[index1head][index2] == target: return True
        else: index1 = index1tail
        index2tail = len(matrix[0]) - 1
        while (index1 < len(matrix)) and (matrix[index1][index2tail]>=target):
            index2head = 0
            while index2head < index2tail-1:
                mid = (index2head + index2tail) // 2
                if  matrix[index1][mid] == target: return True
                elif matrix[index1][mid] < target:
                    index2head = mid
                else:
                    index2tail = mid 
            if  matrix[index1][index2head] == target: return True
            index1 += 1
        return False


print(Solution().searchMatrix(matrix = [[5],[6]], target = 5))