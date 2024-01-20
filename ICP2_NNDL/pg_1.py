def full_name():
    try:
        f_name = str(input("Enter your first_name :"))
        l_name = str(input("Enter your last_name:"))
        if validateString(f_name) and validateString(l_name):
            full_name = f_name + " " + l_name
            print(full_name)
            return full_name
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))

def validateString(name):

    if name != '' and name is not None and name.isspace() != True and name.isnumeric() != True:
        return True
    else:
        return False        

def string_alternative(full_name):
    try:
        alt_name = full_name
        print(alt_name[::2])
    except Exception as error:
        print("Error occured {}".format(error))

if __name__ == "__main__":
    inp_name= full_name()
    string_alternative(inp_name)