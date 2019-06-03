    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dict_ = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+j not in dict_:
                    dict_[i+j] = list()
                    dict_[i+j].append(matrix[i][j])
                else:
                    dict_[i+j].append(matrix[i][j])
        result = list()
        for i, j in dict_.items():
            if i % 2 == 0:
                result += j[::-1]
            else:
                result += j
        return result