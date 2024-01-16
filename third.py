#Author : Sai Nalla

def string_op():
    try:
        inp_string = input("Enter your sentence here:")
        if inp_string != '' and inp_string is not None and inp_string.isspace() != True and inp_string.isnumeric() != True:
            inp_string = inp_string.replace('python','pythons')
            print(inp_string)
        else:
            print("please enter a valid sentence")
    except Exception as error:
        print("Error occured {}".format(error))

if __name__ == "__main__":
    string_op()
