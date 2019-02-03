'Class for tutor objects'
class Tutor:
    username = ""
    full_name = ""
    password = ""
    education_level = ""
    grade_year = 0
    location = ""
    sex = ""
    subjects = []
    cost = 0
    weboption = False
    
    def __init__(self, username, full_name, password, education_level, grade_year, location, sex, subjects, cost, weboption):
        self.username = username
        self.full_name = full_name
        self.password = password
        self.education_level = education_level
        self.grade_year = grade_year
        self.location = location
        self.sex = sex
        self.subjects = subjects 
        self.cost = cost
        self.weboption = weboption    
    
    