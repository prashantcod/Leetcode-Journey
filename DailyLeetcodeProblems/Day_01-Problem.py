#944. Delete Columns to Make Sorted
class Solution(object):
    def minDeletionSize(self, strs):
        delete_count = 0
        rows = len(strs)
        cols = len(strs[0])

        for col in range(cols):            # check each column
            for row in range(rows - 1):    # compare rows
                if strs[row][col] > strs[row + 1][col]:
                    delete_count += 1
                    break                  # stop checking this column

        return delete_count
        
strs = ["cba" , "daf" , "ghi"]
sol = Solution()
print(sol.minDeletionSize(strs))





