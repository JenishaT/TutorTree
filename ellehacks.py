# def homepage: DONE 
# def sign_up_tutee:
# def sign_up_tutor:
# def sign_up_tutor:
# def profile: #(checks if user is a tutee or tutor)
# def find_tutee:
# def find_tutor:
# log out page that goes back to the homepage
# search function to put down tutors and rate em

from tutee import Tutee
tutees = [] 

def change_username():
    print("Please choose your new username.")
    username = input("")
    return username
    
def change_password():
    print("Please choose your new password.")
    password = input("")   
    return password
    
def set_username_and_password():
    print("Please enter your first name.")
    fname = input("")
    print("Please enter your last name.")
    lname = input("")
    full_name = fname + " " + lname
    
    print("Please enter your username")
    username = input("")
    
    print("Please choose a password.")
    password = input("")
    
    return full_name, username, password

    
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
                    print("Sorry, your grade is not primary level. Please enter a primary grade level (grades 1 - 8).") 
                else:
                    break
            if education_level == 's':
                if not 9 <= grade_year <= 12:
                    print("Sorry, your grade is not secondary level. Please enter a secondary grade level (grades 9 - 12).") 
                else:
                    break 
            if education_level == 'ps':
                if not 1 <= grade_year <= 7:
                    print("Sorry, your grade is not post secondary level. Please enter a post secondary grade level (years 1 - 7).") 
                else:
                    break    
    return education_level, grade_year

def set_location():
    print("Please enter your city (so that we can find tutors near yooouuuuuuuu crank that souja boi!)")
    location = input("")   
    return location

def set_preferred_sex():
    print("What is your preferred sex for a tutor? Type 'F' for female, type 'M' for male, or, type 'D' for doesn't matter lol.")
    while True:
        response = input("").lower().strip()        
        if response == 'f' or response == 'm' or response == 'd':
            preferred_sex = response
            print("Your preferred sex is", response)
            break
        else:
            print("Sorry, please enter either 'F', 'M', or 'D'")  
    return preferred_sex

def set_subjects():
    subjects = []    
    print("Please specify the subject you would like to learn.")  
    subject = input("").lower().strip()
    subjects.append(subject)
    while True:
        print("If you would like to learn/teach anything else, please enter that subject. Or, type '0' if you are finished specifying errthang.")
        subject = input("")
        if subject == '0':
            break
        subjects.append(subject)
    return subjects
        
def set_price_range():
    print("Please specify your price range.")
    min_price = input("Min: $")
    max_price = input("Max: $")    
    while not min_price.isdigit() and not max_price.isdigit():
        print("Please enter numbered values!")
        min_price = input("Min: $")
        max_price = input("Max: $")
    
    while float(max_price) < float(min_price) or float(min_price) < 0:
        print("You have entered nonsense! Please enter valid inputs for min and max price.\nMin must be greater than 0 and less than max price, dumbass lol (you need quick maths but dw we're here to help :).")
        min_price = float(input("Min: $"))
        max_price = float(input("Max: $"))
    
    return min_price, max_price
    
def set_weboption_or_chill():
    print("Would you like to add a webcam tutor session option? Type 'Y' for yes or 'N' for no.")    
    while True:
        response = input("").lower().strip()        
        if response == 'y':
            weboption = True
            print("You can now find tutors who offer webcam tutoring sessions!")
            break
        elif response == 'n':
            weboption = False
            print("You will not be able to find tutors who offer webcam tutoring sessions!")                        
            break
        else:
            print("Sorry, please enter either 'Y' or 'N'") 
    return weboption
  
def review_information_for_tutee(tutee):
    print("Welcome,", tutee.full_name, ". Would you like to review your profile information?")
    print("Type 'R' if you would like to review your profile, or type 'B' to begin looking for tutors.")
    x = True
    while x:
        response = input("").lower().strip()
        if response == 'r':
            print("Your profile information is as shown below:")
            print("Name:", tutee.full_name)
            print("Username:", tutee.username)
            print("Password:", tutee.password)
            print("Education level:", tutee.education_level)
            print("Year of study:", tutee.grade_year)
            print("Location:", tutee.location)
            print("Preferred sex of tutor:", tutee.preferred_sex)
            subjects_s = " "
            for subject in tutee.subjects:
                subjects_s += subject + ", "
            print("Subjects:", subjects_s)
            print("Weboption:", tutee.weboption)
            print("Min price:", tutee.min_price)
            print("Max price:", tutee.max_price)
            print("If you would like to change any of the information shown above, type 'Y', or otherwise, type 'N'.")
            while True:
                response = input("").lower().strip()
                if response == 'y':
                    print("you're changing ya info")
                    #change_information()
                    x = False
                    break
                elif response == 'n':
                    print("okurr so youve decided to not change your info nyeah")                    
                    #find_tutors()
                    x = False
                    break
                print("Sorry, please enter either 'Y' or 'N'.")
            break
        elif response == 'b':
            #find_tutors()
            break
        else:
            print("Sorry, please enter either 'R' or 'B'.")
    
def sign_up_tutee():
    full_name, username, password = set_username_and_password()
    education_level, grade_year = set_grade_level()
    location = set_location()
    preferred_sex = set_preferred_sex()
    subjects = set_subjects()
    min_price, max_price = set_price_range()
    weboption = set_weboption_or_chill()
    
    tutee = Tutee(username, full_name, password, education_level, grade_year, location, preferred_sex, subjects, min_price, max_price, weboption)
    tutees.append(tutee)
        
    print("Congratulations! You have successfully signed up as a tutee.")
    print("------------------------------------")
    review_information_for_tutee(tutee)
    
def sign_up_tutor():
    full_name, username, password = set_username_and_password()
    education_level, grade_year = set_grade_level()
    location = set_location()
    sex = set_sex()
    subjects = set_subjects()
    min_price, max_price = set_price_range()
    weboption = set_weboption_or_chill()
         
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



