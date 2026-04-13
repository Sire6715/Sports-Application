from sport import Category, SportType
from athletics_dept import AthleticsDept

     
if __name__ == '__main__':
     dept = AthleticsDept()
     
     dept.generate_report([Category.VARSITY, SportType.BASEBALL])
     dept.generate_report([Category.VARSITY, SportType.FOOTBALL])
     
     dept.generate_report([Category.INTRAMURAL, SportType.BASEBALL])
     dept.generate_report([Category.INTRAMURAL, SportType.FOOTBALL])
     dept.generate_report([Category.INTRAMURAL, SportType.VOLLEYBALL])
     
