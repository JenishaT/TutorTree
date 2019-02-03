# def profile: #(checks if user is a tutee or tutor)
# def find_tutee:
# def find_tutor:
# log out page that goes back to the homepage
# search function to put down tutors and rate em

from tutee import Tutee
from tutor import Tutor
tutees = [] 
tutors = []

def logout():
    print("Thanks for working with us!")
    print("Logging Out........\n\n")
    homepage()
    
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
    print("Please indicate your current level of education. \nType 'P' for primary (grades 1 - 8),\n'S' for secondary (grades 9 - 12), \n'PS' for post secondary (university/college level education)")
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
                    print("Sorry, your grade is not primary level. \nPlease enter a primary grade level (grades 1 - 8).") 
                else:
                    break
            if education_level == 's':
                if not 9 <= grade_year <= 12:
                    print("Sorry, your grade is not secondary level. \nPlease enter a secondary grade level (grades 9 - 12).") 
                else:
                    break 
            if education_level == 'ps':
                if not 1 <= grade_year <= 7:
                    print("Sorry, your grade is not post secondary level. \nPlease enter a post secondary grade level (years 1 - 7).") 
                else:
                    break    
    return education_level, grade_year

def set_location():
    print("Please enter your city")
    location = input("")   
    return location

def set_sex():
    while True:
        response = input("").lower().strip()        
        if response == 'f' or response == 'm' or response == 'e':
            sex = response
            break
        else:
            print("Sorry, please enter either 'F', 'M', or 'E'")  
    return sex

def set_subjects():
    subjects = []    
    subject = input("").lower().strip()
    subjects.append(subject)
    while True:
        print("If you would like to add another subject, please enter that subject. \nType '0' if you are finished")
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
        print("Please enter valid inputs for min and max price.\nMin must be greater than 0 and less than max price.")
        min_price = float(input("Min: $"))
        max_price = float(input("Max: $"))
    
    return min_price, max_price
    
    
def set_weboption(): 
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
    return weboption

## My shit
def set_cost():
    print("Please specify your price per tutoring session")
    cost = input("$")
    while not cost.isdigit():
        print("Please enter number values!")
        cost = input("$")    
    return float(cost)

def get_tutor_data(searchname, tutors):
    data = ""
    for tutor in tutors:
        if tutor.username == searchname:
            data = "Name: " + tutor.full_name + "\nEducation: " + tutor.education_level+ "\nGrade: " + str(tutor.grade_year) + "\nSubjects: " + str(tutor.subjects)
            return data
        
def display_tutors(sorted_tutors):
    for name in sorted_tutors:
        print(get_tutor_data(name, tutors))
        print("------------------------------------")

def order_tutors(tutee, tutors):
    print("Here are you are your matches:")
    print("------------------------------------")
    matches = {}
    for tutor in tutors:
        matches[tutor.username] = 0
        if tutor.education_level == tutee.education_level and tutor.grade_year >= tutee.grade_year and tutor.location == tutee.location:
            if tutor.sex == tutee.preferred_sex:
                matches[tutor] += 1
            elif tutee.preferred_sex == 'E':
                matches[tutor.username] += 1
            for subject in tutee.subjects:
                if subject in tutor.subjects:
                    matches[tutor.username] += 1
            if tutor.weboption == tutee.weboption:
                matches[tutor.username] += 1
    sorted_tutors = sorted(matches, key=matches.get, reverse=True)
    display_tutors(sorted_tutors)
    print("Type 'R' to go return to the previous screen")
    while True:
        response = input("").lower().strip()        
        if response == 'r':
            welcome_tutee(tutee)
        else:
            print("Please enter 'R', to go back")      
    
def welcome_tutee(tutee):
    print("Welcome,", tutee.full_name, "Would you like to review your profile information?")
    print("Type 'R' if you would like to review your profile, or type 'B' to begin looking for tutors.\nType 'L' to logout")
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
            
            print("Type 'B' to begin looking for tutors.\n Type 'L' to logout")
            response = input("").lower().strip()
            if response == 'b':
                order_tutors(tutee, tutors)
                break
            elif response == 'l':
                logout()
            else:
                print("Sorry, please enter either 'B' or 'L'")            
            
            # functions to change specific parameters
            #print("If you would like to change any of the information shown above, type #'Y', or otherwise, type 'N'.")
            #while True:
            #    response = input("").lower().strip()
            #    if response == 'y':
            #        #change_information()
            #        x = False
            #        break
            #    elif response == 'n':                    
            #        order_tutors()
            #        x = False
            #       break
            #    print("Sorry, please enter either 'Y' or 'N'.")
            break
        elif response == 'b':
            order_tutors(tutee, tutors)
            break
        else:
            print("Sorry, please enter either 'R', 'B', 'L'")
            
def welcome_tutor(tutor):
    print("Welcome,", tutor.full_name, "Would you like to review your profile information?")
    print("Type 'R' if you would like to review your profile,\nType 'L' to logout")
    x = True
    while x:
        response = input("").lower().strip()
        if response == 'r':
            print("Your profile information is as shown below:")
            print("Name:", tutor.full_name)
            print("Username:", tutor.username)
            print("Password:", tutor.password)
            print("Education level:", tutor.education_level)
            print("Year of study:", tutor.grade_year)
            print("Location:", tutor.location)
            print("Sex:", tutor.sex)
            subjects_s = " "
            for subject in tutor.subjects:
                subjects_s += subject + ", "
            print("Subjects:", subjects_s)
            print("Weboption:", tutor.weboption)
            print("Price per session:", tutor.cost)
            
            print("Type 'L' to logout")
            response = input("").lower().strip()
            if response == 'l':
                logout()
            
            
            #function to change parameters
            #print("If you would like to change any of the information shown above, type #'Y', or otherwise, type 'N'.")
            #while True:
            #    response = input("").lower().strip()
            #    if response == 'y':
            #        #change_information()
            #        x = False
            #        break
            #    elif response == 'n':                    
            #        #find_tutee()
            #        x = False
            #       break
            #    print("Sorry, please enter either 'Y' or 'N'.")
            #break
        elif response == 'l':
            logout()
            break
        else:
            print("Sorry, please enter either 'R' or 'L'.")            
    
def sign_up_tutee():
    full_name, username, password = set_username_and_password()
    education_level, grade_year = set_grade_level()
    location = set_location()
    print("What is your preferred sex for a tutor? \nType 'F' for female, Type 'M' for male, \nType 'E' for either")
    preferred_sex = set_sex()
    print("Please specify the subject you would like to learn.")
    subjects = set_subjects()
    min_price, max_price = set_price_range()
    print("Would you like to add a webcam tutor session option? \nType 'Y' for yes or 'N' for no.") 
    weboption = set_weboption()
    
    tutee = Tutee(username, full_name, password, education_level, grade_year, location, preferred_sex, subjects, min_price, max_price, weboption)
    tutees.append(tutee)
        
    print("Congratulations! You have successfully signed up as a tutee.")
    print("------------------------------------")
    welcome_tutee(tutee)
   
def sign_up_tutor():
    full_name, username, password = set_username_and_password()
    education_level, grade_year = set_grade_level()
    location = set_location()
    print("Enter your sex. Type 'F' for female, type 'M' for male")
    sex = set_sex()
    print("Please specify the subject you would like to teach.")
    subjects = set_subjects()
    cost = set_cost()
    print("Would you like to provide a webcam tutor session option? \nType 'Y' for yes or 'N' for no.") 
    weboption = set_weboption()
    
    tutor = Tutor(username, full_name, password, education_level, grade_year, location, sex, subjects, cost, weboption)
    tutors.append(tutor)
    
    print("Congratulations! You have successfully signed up as a tutor.")
    print("------------------------------------")
    welcome_tutor(tutor)  

def login(tutees, tutors):
    username = input("Please enter your username:")
    password = input("Please type your password:")
    found = False
    
    for tutee in tutees:
        if username == tutee.username and password == tutee.password:
            found = True
            print("Welcome back,", username)
            welcome_tutee(tutee)
            
    for tutor in tutors:
        if username == tutor.username and password == tutor.password:
            print("Welcome back,", username)
            found = True
            welcome_tutor(tutor)        
            
    if found == False:
        print("An account with the username,",  username, "does not exist")
        print("Please Try Again\n\n")
        homepage()
            
    for tutor in tutors:
        if username == tutors.username and password == tutors.password:
            print("Welcome back,", username)
            #welcome_tutor(tutor)    
    
def homepage():
    print("Welcome to TutorTree")
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
                    print("Signing up as a tutee.")
                    print("------------------------------------")                    
                    sign_up_tutee()                    
                    break
                elif action == '1':
                    x = False
                    print("Signing up as a tutor.")   
                    print("------------------------------------")                    
                    sign_up_tutor()                     
                    break
                print("Sorry, please enter either '0' or '1'")
        elif action == '1':
            #profile()
            print("You're Logging in.") 
            login(tutees, tutors)
            break
        else:
            print("Sorry, please enter either '0' or '1'")

homepage()

