from sport import Category, SportType
from athletics_dept import VarsityDept, IntramuralDept      

     
if __name__ == '__main__':
     varsity = VarsityDept()
     
     varsity.generate_report(SportType.BASEBALL)
     varsity.generate_report(SportType.FOOTBALL)
     
     intramural = IntramuralDept()
     
     intramural.generate_report(SportType.BASEBALL)
     intramural.generate_report(SportType.FOOTBALL)
     intramural.generate_report(SportType.VOLLEYBALL)
     
     
     
