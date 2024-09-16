class Course:
    '''Parent class for all Courses ran by Hyperion Dev
    Usage:
        object.contact_details()\n
        object.get_head_office()
    '''
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        '''Returns print statement with self.contact_website'''
        print("Please contact us by visiting", self.contact_website)

    def get_head_office(self):
        print("The head office is: Cape Town")


class OOPCourse(Course):
    '''Object Orientated Programming Course sub class ran by Hyperion Dev\n
    Usage:
        object.trainer_details()\n
        object.show_course_id()
    '''
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        '''Returns print statement including self.description and self.trainer'''
        print(f"This is a course about {self.description}, ran by {self.trainer}")

    def show_course_id(self):
        '''Returns print statement with Course ID number'''
        print("Course ID number: #12345")


# Create OOP subclass object
course_1 = OOPCourse()

# Call parent class method contact_details()
course_1.contact_details()

# Call subclass method trainer_details()
course_1.trainer_details()
# Call subclass method show_course_id()
course_1.show_course_id()
