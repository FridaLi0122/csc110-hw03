"""
Name: Frida Li
Peers: 
References: 
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """Read five grades from the user and store them in the grades list."""
    
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:
        # check if the input is not a digit print error
        # convert to int
        # check if the int is not in the interval [0 to 10] print error
        # add the int to grades at index idx
        
        # Read the next grade as a string
        x_string = input("Give me the next grade in [0 to 10]:")
        
        # Make sure the input contains only digits
        if not x_string.isdigit():
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        
        x_int = int(x_string)
        
        # Make sure the grade is between 0 and 10
        if not 0 <= x_int <= 10:
            print("Error in read_five_ints: input integer outside of range")
            exit()
            
        else:
            grades[idx] = x_int
            
            
            
        

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """Let the user choose mean, median, or mode and return the result."""
    
    y_string = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    
    
    # Calculate the statistic selected by the user
    if y_string == "a":
        print("picked: Mean")
        avg1 = statistics.mean(grades)
        return avg1
    
    elif y_string == "b":
        print("picked: Median")
        avg2 = statistics.median(grades)
        return avg2
    
    elif y_string == "c":
        print("picked: Mode")
        avg3 = statistics.mode(grades)
        return avg3
    
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        
        exit()
        
    
        

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """Let the user choose how to display the calculated result."""
    
    z_string = input("Pick '1' for print average, or '2' for plot average: ")
    
    # Display the result using the selected format
    if z_string == "1":
        print_list_and_average(average)
        
    elif z_string == "2":
        plot_grades(average)
        
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()
        


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
