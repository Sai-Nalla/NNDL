#Author : Sai Nalla
#start
def string_operation():
    try:
        inp_string = str(input("Enter your string here:"))
        if inp_string != '' and inp_string is not None and inp_string.isspace() != True and inp_string.isnumeric() != True:
            # Deleting at least 2 characters
            output = inp_string[:-2]
            # reversal of the string after

            output = output[::-1]

            print(output)
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))
#end of block1
if __name__ == "__main__":
    string_operation()

