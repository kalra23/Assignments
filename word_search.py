'''Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row. '''

def word_in_matrix(matrix, word):
    n_rows = len(matrix)
    n_cols = len(matrix)
    

    for row in range(n_rows):
        for col in range(n_cols):
            # check left-to-right
            if col + len(word) <= n_cols:
                if matrix[row][col:col+len(word)] == list(word):
                    return True
            # check up-to-down
            if row + len(word) <= n_rows:
                if [matrix[r][col] for r in range(row,row+len(word))] == list(word):
                    return True
    return False

matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

print(word_in_matrix(matrix, 'FOAM')) 
print(word_in_matrix(matrix, 'MASS')) 
print(word_in_matrix(matrix, 'NO')) 
print(word_in_matrix(matrix, 'BOSS'))

