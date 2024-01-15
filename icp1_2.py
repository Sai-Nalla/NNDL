#Author: Sai Nalla
#start
def math_operations():
    try:
        try:
            input_b = int(input("Enter your first number:"))#enter the 1st integer value
            input_c = int(input("Enter your second number :"))#enter the 2nd integer value
        except ValueError:
            print ("Please enter only number not strings")
            return None
        if type(input_b) == int and type(input_c) == int:
            addition = input_b + input_c  #addition operator
            subtraction = input_b - input_c #subtraction operator
            multiplication = input_b * input_c #multiplication operator
            if input_c != 0:
                division = input_b/input_c #division operator
            else:
                division = None
                print("division by zero is not possible")
            print("Addition of 2 numbers : ",addition)
            print("Substraction  of 2 numbers : ", subtraction)
            print("Multiplication  of 2 numbers : ", multiplication)
            print("Division  of 2 numners : " ,division)
        else:
            print("please enter a valid number")
    except Exception as error:
        print("Error occured {}".format(error))
#end

if __name__ == "__main__":
    math_operations()