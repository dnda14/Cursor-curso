# create a list of squares of first 10 numbers
def squares_of_first_10_numbers():
    squares = [i**2 for i in range(1, 11)]
    return squares

print(squares_of_first_10_numbers())

# create a list of squares of first 10 numbers using a for loop
def squares_of_first_10_numbers_using_for_loop():
    squares = []
    for i in range(1, 11):
        squares.append(i**2)
    return squares

# create a list of cubes (powered to 3) of first 10 numbers
def cubes_of_first_10_numbers():
    cubes = [i**3 for i in range(1, 11)]
    return cubes

print(cubes_of_first_10_numbers())