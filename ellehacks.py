# def homepage: DONE 
# def sign_up_tutee:
# def sign_up_tutor:
# def sign_up_tutor:
# def profile: #(checks if user is a tutee or tutor)
# def find_tutee:
# def find_tutor:

subjects = []

def set_username_and_password():
    # username
    print("Please enter your first name.")
    fname = input("")
    print("Please enter your last name.")
    lname = input("")
    full_name = fname + lname
    
    # password (if time in end then make this more secure and have security questions and etc.
    print("Please choose a password.")
    password = input("")    

def set_grade_level():
    print("Please indicate your current level of education by typing 'P' for primary (grades 1 - 8),\n'S' for secondary (grades 9 - 12), or 'PS' for post secondary (university/college level education)")
    while True:
        education_level = input("").lower().strip()
        if education_level == 'p' or education_level == 's' or education_level == 'ps':         
            break
        else:
            print("Sorry, please enter either 'P', 'S', or 'PS")
            
    while True:
            print("Please indicate your current year of study.")
            grade_year = int(input(""))
            if education_level == 'p':
                if not 1 <= grade_year <= 8:
                    print("Sorry, your grade is not primary level. Please enter a primary level grade.") 
                else:
                    break
            if education_level == 's':
                if not 9 <= grade_year <= 12:
                    print("Sorry, your grade is not secondary level. Please enter a secondary level grade.") 
                else:
                    break 
            if education_level == 'ps':
                if not 1 <= grade_year <= 7:
                    print("Sorry, your grade is not post secondary level. Please enter a post secondary level grade.") 
                else:
                    break                

def sign_up_tutee():
    set_username_and_password()
    
    set_grade_level()
    
    # grade level
    print("Please indicate your current level of education by typing 'P' for primary (grades 1 - 8),\n'S' for secondary (grades 9 - 12), or 'PS' for post secondary (university/college level education)")
    while True:
        education_level = input("").lower().strip()
        if education_level == 'p' or education_level == 's' or education_level == 'PS':         
            break
        else:
            print("Sorry, please enter either 'P', 'S', or 'PS")
            
    while True:
            print("Please indicate your current year of study.")
            grade_year = int(input(""))
            if education_level == 'p':
                if not 1 <= grade_year <= 8:
                    print("Sorry, your grade is not primary level. Please enter a primary level grade.") 
                else:
                    break
            if education_level == 's':
                if not 9 <= grade_year <= 12:
                    print("Sorry, your grade is not secondary level. Please enter a secondary level grade.") 
                else:
                    break 
            if education_level == 'ps':
                if not 1 <= grade_year <= 7:
                    print("Sorry, your grade is not post secondary level. Please enter a post secondary level grade.") 
                else:
                    break            
    
    # location (city)
    print("Please enter your city (so that we can find tutors near yooouuuuuuuu crank that souja boi!)")
    location = input("")
    
    # preferred sex
    print("What is your preferred sex? Type 'F' for female, type 'M' for male, or, type 'D' for doesn't matter lol.")
    while True:
        response = input("").lower().strip()        
        if response == 'f' or response == 'm' or response == 'd':
            preferred_sex = response
            print("Your preferred sex is ", response)
            break
        else:
            print("Sorry, please enter either 'F', 'M', or 'D'")    
    
    # subjects
    print("Please specify the subject you would like to learn.")  
    subject = input("").lower().strip()
    subjects.append(subject)
    while True:
        print("If you would like to learn anything else, please enter that subject. Or, type '0' if you are finished specifying errthang.")
        subject = input("")
        if subject == '0':
            break
        subjects.append(subject)
    
    # price (INCOMPLETE, still have to validate et)
    print("Please specify your price range.")
    min = int(input("Min: $"))
    max = int(input("Max: $"))
    
    # weboption or chill?
    print("Would you like to add a webcam tutor session option? Type 'Y' for yes or 'N' for no.")    
    while True:
        response = input("").lower().strip()        
        if response == 'y':
            weboption = True
            break
        elif response == 'n':
            weboption = False
            break
        else:
            print("Sorry, please enter either 'Y' or 'N'") 
    
    
    
    
         
def homepage():
    print("Welcome sickerdogs and demons!\n")
    print("Type 0 to Sign Up")
    print("Type 1 to Log in\n")
    x = True
    while x:
        action = input("")
        
        if action == '0':
            print("------------------------------------")
            print("Welcome to our sick site! Are you a tutee or tutor?\n")
            print("Type 0 for tutee")
            print("Type 1 for tutor\n")
            while True: 
                action = input("")
                if action == '0':
                    x = False
                    print("youre signing up as a tutee.")
                    print("------------------------------------")                    
                    sign_up_tutee()                    
                    break
                elif action == '1':
                    x = False
                    print("youre signing up as a tutor.")   
                    print("------------------------------------")                    
                    #sign_up_tutor()                     
                    break
                print("Sorry, please enter either '0' or '1'")
        elif action == '1':
            #profile()
            print("youre logging in.")            
            break
        else:
            print("Sorry, please enter either '0' or '1'")

homepage()



    