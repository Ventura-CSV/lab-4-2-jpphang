def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    
    for i in range(5):
        user_input=int(input(f'enter numer{i+1}:'))
        
        total += user_input
        
    print(total)        

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
