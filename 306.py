
class Solution:
    def dfs(self, num, starting_index, prev_two):
        if starting_index == len(num):
            return False

        if len(prev_two) != 2:
            for index in range(starting_index, len(num) - 1):
                prev_two.append(int(num[starting_index:index+1]))
                if self.dfs(num, index + 1, prev_two):
                    return True
                prev_two.pop()
                if num[starting_index:index + 1] == "0":
                    break

        else:
            sum_needed = sum(prev_two)
            end_index = starting_index + len(str(sum_needed)) - 1
            if num[starting_index : end_index + 1] == str(sum_needed):
                if end_index == len(num) - 1:
                    return True
                if self.dfs(num, end_index + 1, [prev_two[1], sum_needed]):
                    return True
                
        return False
    
    def isAdditiveNumber(self, num: str) -> bool:
        return self.dfs(num, 0, [])