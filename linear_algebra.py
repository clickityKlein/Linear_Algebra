# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:14:02 2022

@author: carlj
"""

class LinearAlgebra():
    
    # zero matrix
    def zeros(row, column):
        return [[0] * column for step in range(row)]

    # identiy matrix
    def identiy(dimension):
        new = LinearAlgebra.zeros(dimension, dimension)
        for count, row in enumerate(new):
            row[count] = 1
        return step
    
    # this will return if the input is a vector (1), matrix(2), or neither (0)
    def vector_or_matrix(A):
        matrix_type = 2
        try:
            len(A)
        except TypeError:
            matrix_type = 0
        finally:
            if matrix_type == 0:
                matrix_type = 0
            else:
                try:
                    len(A[0])
                except TypeError:
                    matrix_type = 1
                finally:
                    return matrix_type        
    
    # this will return the len of a vector, or the dimensions of a matrix
    def matrix_size_check(A):
        check = LinearAlgebra.vector_or_matrix(A)
        if check == 2:
            for row in range(0, len(A)):
                if len(A[0]) != len(A[row]):
                    print(f'Error: Rows in matrix {A} do not contain the same number of elements')
                    return 0
                else:
                    return (len(A), len(A[0]))
        elif check == 1:
            return len(A)
        else:
            print(f'Error: Input {A} is neither a vector nor a matrix')
            return 0
    
    # this will check to see if two matrices or vector are the same size
    def matrices_size_check(A, B):
        size_A = LinearAlgebra.matrix_size_check(A)
        size_B = LinearAlgebra.matrix_size_check(B)
        if size_A == 0 or size_B == 0:
            print('Error: Inputs are formatted incorrectly')
            return 0
        elif size_A != size_B:
            print('Error: Inputs are not the same dimensions')
            return 0
        else:
            return 1
        
    # matrix arithmetic
    # matrix addition
    def matrix_addition(A, B):
        check = LinearAlgebra.matrices_size_check(A, B)
        new = LinearAlgebra.zeros(len(A), len(A[0]))
        if check == 1:
            for row in range(0, len(A)):
                for element in range(0, len(A[0])):
                    new[row][element] = A[row][element] + B[row][element]
            return new
        else:
            print('InputError: Check formatting or dimensions')
    
    # matrix subtraction
    def matrix_subtraction(A, B):
        check = LinearAlgebra.matrices_size_check(A, B)
        new = LinearAlgebra.zeros(len(A), len(A[0]))
        if check == 1:
            for row in range(0, len(A)):
                for element in range(0, len(A[0])):
                    new[row][element] = A[row][element] - B[row][element]
            return new
        else:
            print('InputError: Check formatting or dimensions')
            
    # matrix algebra
    # matrix multiplication - scalar
    # matrix A multiplied by scalar c
    def scalar_multiplication(c, A):
        check = LinearAlgebra.vector_or_matrix(A)
        # 1: vector, 2: matrix, 3: other
        if check == 1:
            return [c * element for element in A]
        elif check == 2:
            new = []
            for row in range(0, len(A)):
                new.append([c * element for element in A[row]])
            return new
        else:
            print('InputError: Check formatting or dimensions')
  
    # matrix multiplication - dot product set up
    # first, check for [r1 c1] [r2 c2], c1 and r2 must be same dimensions, where
    # multipliation will result in a [r1 c2] matrix 
    # it's assumed in this module that vectors are input as row vectors
    def multiplication_dimension_match(A, B):
        type_A = LinearAlgebra.vector_or_matrix(A)
        type_B = LinearAlgebra.vector_or_matrix(B)
        # types will return if the input is a vector (1), matrix(2), or neither (0)
        size_A = LinearAlgebra.matrix_size_check(A)
        size_B = LinearAlgebra.matrix_size_check(B)
        # sizes will return vector: single value, matrix: (rows, cols)
        if size_A == 0 or size_B == 0:
            print('Error: Inputs are formatted incorrectly')
            return 0
        # vector vs. matrix computations
        
        # A is a vector, B is a vector, then return 1
        if type_A == 1 and type_B == 1 and size_A == size_B:
            return 1
        elif type_A == 1 and type_B == 1 and size_A != size_B:
            print('Error: Dimensions are incompatible')
            return 0
            
        # A is a vector, B is a matrix, then return 2
        if type_A == 1 and type_B == 2 and size_A == size_B[0]:
            return 2
        elif type_A == 1 and type_B == 1 and size_A != size_B[0]:
            print('Error: Dimensions are incompatible')
            return 0
            
        # A is a matrix, B is a vector, then return 3
        if type_A == 2 and type_B == 1 and size_A[1] == size_B:
            return 3
        elif type_A == 2 and type_B == 1 and size_A[1] != size_B:
            print('Error: Dimensions are incompatible')
            return 0
            
        # A is a matrix, B is a matrix, then return 4
        if type_A == 2 and type_B == 2 and size_A[1] == size_B[0]:
            return 4
        elif type_A == 2 and type_B == 1 and size_A[1] != size_B[0]:
            print('Error: Dimensions are incompatible')
            return 0
         
    # matrix multiplication - dot product
    def matrix_multiplication(A, B):
        size_A = LinearAlgebra.matrix_size_check(A)
        size_B = LinearAlgebra.matrix_size_check(B)
        check = LinearAlgebra.multiplication_dimension_match(A, B)
        if check == 0:
            print('Error: Dimensions are incompatible')
        # 1: A vector, B vector
        elif check == 1:
            scalar = 0
            for a in range(0, len(A)):
                scalar += A[a] * B[a]
            return scalar
        # 2: A vector, B matrix
        elif check == 2:
            results = []
            for j in range(0, size_A):
                for k in range(0, size_B[1]):
                    results.append([A[j] * B[j][k], k])
            final = LinearAlgebra.zeros(1, size_B[1])
            for result in results:
                for column_num in range(0, size_B[1]):
                    if result[1] == column_num:
                        final[0][column_num] += result[0]
            return final
        # 3: A matrix, B vector
        elif check == 3:
            results = []
            for j in range(0, size_A[1]):
                for k in range(0, size_B):
                    results.append([A[j][k] * B[k], j])
            final = LinearAlgebra.zeros(size_B, 1)
            for result in results:
                for row_num in range(0, size_B):
                    if result[1] == row_num:
                        final[row_num][0] += result[0]
            return final
        # 4: A matrix, B matrix
        elif check == 4:
            pass
        
    
    # future work ups:
        
    # 1) Elimination Matrix E
        # EA = I
        # will likely be used to solve a system of equations, so maybe find a way
        # to extend to Ax = b...
        
    # 2) Magnitude of Vector
        # sqrt(sum(elements^2))
    
    # 3) Unit Vector (builds off 2)
        # vector / magnitude of vector
        
    # *) Potentially include:
        # Span
        # Tests for Independence
        # Tests for Subspaces
        # Ultimately all builds into Basis...
        
    # 4) Dot Product
    
    # 5) Cross Product
    
    # 6) Transpose Formula
    
    # 7) Break Matrix into the 4 Subspaces:
        # Null Space: N(A)
            # find x s.t. Ax = 0 (if N(A) contains only 0, C(A) are linearly independent)
        # Left Null Space: N(A^T)
        # Column Space: C(A)
        # Row Space: C(A^T)