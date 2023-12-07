# Function 1
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

maximum = max_num(1, 2, 3)
print(f"Max number is: {maximum}")

# Function 2
def mult_list(numbers):
    output = 1

    for number in numbers:
        output *= number
    
    return output

example_answer = mult_list([1, 2, 3, 4, 5])
print(f"The answer of the numbers in this list is: {example_answer}")

#function 3
def rev_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
    
string_example = "yo dude"

print(f"the reversed string is: {rev_string(string_example)}")

#function #4
def num_within(number, start, end):
        return start <= number <= end

num_within_example= num_within(3, 2, 4)
print(f"an example is of a num within: {num_within_example}")

#function 5
#n is number
def pascal(n):
    if n <= 0:
        return
    
    row = [1]

    for i in range(n):
        print(" " * (n - i), end="")
        for num in row:
            print(num, end=" ")
        print()

        # Calculate the next row
        next_row = [1]
        for j in range(len(row) - 1):
            next_num = row[j] + row[j + 1]
            next_row.append(next_num)
        next_row.append(1)
        row = next_row

pascal(5)


