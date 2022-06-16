# Linear_Algebra
Package containing common linear algebra tools using general python language. Created while reviewing linear algebra, and as a practice exercise for learning Python. This package uses Python lists. For practical purposes, it's still recommended to use array type objects in conjunction with vetted common modules, such as Numpy.

## Table of Contents:
- [A Look Under the Hood](#a-look-under-the-hood)
- [Thoughts / Future Functions](#thoughts-/-future-functions)

## A Look Under the Hood
There is a single code file used for this project, consisting of multiple functions in a class.
- zeros(row, column): returns a matrix of zeros for the given amount of rows and columns.
- identiy(dimension): returns an identity matrix for the given dimension (i.e. an nxn matrix with 1's in the diagnonal, and the rest 0's).
  
  BUILDS OFF FUNCTIONS: zeros()
  
- vector_or_matrix(A): takes in a list object A. Returns a certain value for if it's a matrix, vector, or neither (error).
- matrix_size_check(A): takes in a list object A. Returns the length of the vector, or the dimensions of a matrix.

  BUILDS OFF FUNCTIONS: vector_or_matrix()
  
- matrices_size_check(A, B): takes in two list objects A, B. Returns if these vectors or matrices are the same size or not.

  BUILDS OFF FUNCTIONS: matrix_size_check()

- matrix_addition(A, B): takes in two list objects A, B. Returns a single list object containing element-wise addition between A and B.

  BUILDS OFF FUNCTIONS: matrices_size_check(), zeros()

- matrix_addition(A, B): takes in two list objects A, B. Returns a single list object containing element-wise subtraction between A and B.
  
  BUILDS OFF FUNCTIONS: matrices_size_check(), zeros()
  
- scalar_multiplication(c, A): takes in integer c and list object A. Returns a single list object (either vector or matrix) with every element multiplied by the constant c.
  
  BUILDS OFF FUNCTIONS: vector_or_matrix()
  
- multiplication_dimension_match(A, B): takes in two list objects A, B. Returns if different values based on whether the objects are vectors and / or matrices, and if the two objects are compatible for matrix multiplication (i.e. if the dimensions of the objects are: A = [r1 c1] & B = [r2 c2], if c1 = r2 then the objects are compatible for matrix multiplication).

  BUILDS OFF FUNCTIONS: vector_or_matrix(), matrix_size_check()

- matrix_multiplication(A, B): takes in list objects A, B. Returns a single list object (matrix or vector) after matrix multiplication is applied between A and B.
  
  BUILDS OFF FUNCTIONS: matrix_size_check(), multiplication_dimension_match()
  

[Table of Contents](#table-of-contents)

## Thoughts / Future Functions
This was an entertaining exercise, albeit surprisingly time consuming while employing error handling and building out supporting functions (vector_or_matrix(), multiplication_dimension_match(), etc.). It's fascinating that the module works with consecutive functions ultimately cumulating into some of the more basic functions of linear algebra, such as addition, subtraction, and multiplcation of matrices and vectors.

Additionally, there are thoughts to work up future linear algebra concepts such as:
- Elimation Matrx
- Magnitude of Vector
- Unit Vector
- Span, Independence Tests, Subspace Tests, Basis
- Transpose Fromula

Although a great exercise, as stated in the opening, it might be a better use of time to stick with the renowned modules that use actual array objects.

[Table of Contents](#table-of-contents)
