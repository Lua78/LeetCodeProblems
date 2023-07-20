def rotate(matrix)
    matrix.replace(matrix.reverse.transpose)
  end

puts rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])