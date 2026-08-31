class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_row = []
            check_col = []
            
            for j in range(9):

                if (board[i][j] != "." and board[i][j] in check_row):
                    return False
                else:
                    check_row.append(board[i][j])

                if (board[j][i] != "." and board[j][i] in check_col):
                    return False

                else:
                    check_col.append(board[j][i])


                if(i%3==0 and j%3==0):
                    check_block = []
                    for add_block_i in range(3):
                        for add_block_j in range(3):
                            
                            block_i = add_block_i+i
                            block_j = add_block_j+j

                            if(board[block_i][block_j] != "." and board[block_i][block_j] in check_block):
                                return False
                            else:
                                check_block.append(board[block_i][block_j])
        return True


    