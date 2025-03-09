def triangle(size, style="normal"):
    """This function must print a triangle using the # character on the screen.

    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """
    for i in range(1, size + 1):
        print('#' * i)
    

    


def rectangle(width, height):
    for i in range(height): #iterates over every row
        if i == 0 or i == height - 1: #if the first row or last row, print the top and bottom border width times
            print( '#' * width)
        else:
            print('#'+ ' ' * (width - 2) + '#' ) # '' * (width - 2) creates the hollow part in the rectangle
            #first print '#' followed by hollow followed by the hollow space follwoed by '#'
            #if statement in for loop repeats until all conditions are met
   
    """This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)

    >>> rectangle(1, 1)
    #

    >>> rectangle(3, 1)
    ###

    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """
   
        
        


if __name__ == "__main__":
    triangle(0)
    triangle(10)
    print()
    rectangle(10, 3)
    rectangle(-1, -1)
