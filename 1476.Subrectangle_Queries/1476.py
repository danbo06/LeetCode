https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in  range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]



    def __init__(self, rectangle: List[List[int]]):
        # self.rectangleとrectangleが同じメモリを共有しないように__init__でrectangleをdeepcopyする
        self.rectangle = copy.deepcopy(rectangle)
        self.histories = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.histories.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for his in reversed(self.histories):
            if his[0] <= row <= his[2] and his[1] <= col <= his[3]:
                return his[4]
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)