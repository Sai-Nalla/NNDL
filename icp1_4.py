#Author : Sai Nalla
#start
def grading_classScore():
    try:
        try:
            class_score = int(input("Enter your score here:"))
        except ValueError:
            print ("Please enter number in numeric format not strings")
            return None
        if class_score != '' and class_score is not None:
            if class_score > 100 or class_score < 0:
                print("Score not in range please enter a valid score")
            else:
                if class_score >= 90 and class_score <= 100: #Range of Grade A score
                    print("A")
                elif class_score >= 80 and class_score <= 89: #Range of Grade B score
                    print("B")
                elif class_score >= 70 and class_score <= 79: #Range of Grade C score
                    print("c")
                elif class_score >= 60 and class_score <= 69: #Range of Grade D score
                    print("D")
                else:
                    print("F") #Grade F score
            
        else:
            print("please enter a valid number")
    except Exception as error:
        print("Error occured {}".format(error)) 
#end
if __name__ == "__main__":
    grading_classScore()