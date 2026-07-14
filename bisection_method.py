def square_root_bisection(number, tolerance=0.01, max_iteration=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    
    # for numbers between 0 and 1, the square root is actually greater than the number
    # e.g. 
    # root 0.25 -> 0.5 
    # root 0.04 -> 0.2
    if (number > 0 and number < 1 ):
        lower = number
        upper = 1

    # for numbers greater than or equal to 1, the square root is less than or equal to the number
    # e.g.
    # root 25 -> 5
    # root 9 -> 3
    elif number >= 1:
        lower = 0
        upper = number
    
    for i in range(max_iteration):
        mid = (lower + upper) / 2
        mid_square = mid**2
        
        # since square is greater than target, so root must be in lower half
        if mid_square > number:  
            upper = mid
        # since square is lower than target, so root must be in upper half         
        elif mid_square < number:
            lower = mid
        elif mid_square == number:
            print(f'The square root of {number} is approximately {mid}')
            return mid
        
        # check if below tolerance
        if upper-lower <= tolerance:
            mid = (lower+upper)/2
            print(f'The square root of {number} is approximately {mid}')
            return mid
        
    print(f'Failed to converge within {max_iteration} iterations')
    return None