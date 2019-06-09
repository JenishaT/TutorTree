'Class for tutee objects'
class Tutee:
    username = ""
    full_name = ""
    password = ""
    education_level = ""
    grade_year = 0
    location = ""
    preferred_sex = ""
    subjects = [] 
    min_price = 0
    max_price = 0
    weboption = False
    
    def __init__(self, username, full_name, password, education, grade_level, \
                 location, preferred_sex, subjects, min_price,max_price, \
                 weboption):
        self.username = username
        self.full_name = full_name
        self.password = password
        self.education_level = education
        self.grade_year = grade_level
        self.location = location
        self.preferred_sex = preferred_sex
        self.subjects = subjects 
        self.min_price = min_price
        self.max_price = max_price 
        self.weboption = weboption         
