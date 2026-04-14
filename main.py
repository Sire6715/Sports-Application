from sports.sport import Category, SportType
from sports.athletics_dept import VarsityDept, IntramuralDept
from players.team import Team_1, Team_2, Team_3
from players.report import TeamReport

     
if __name__ == '__main__':
     varsity = VarsityDept()
     
     varsity.generate_report(SportType.BASEBALL)
     varsity.generate_report(SportType.FOOTBALL)
     
     intramural = IntramuralDept()
     
     intramural.generate_report(SportType.BASEBALL)
     intramural.generate_report(SportType.FOOTBALL)
     intramural.generate_report(SportType.VOLLEYBALL)
     
     report = TeamReport()
     
     team_1 = Team_1()
     report.print(team_1)
     
     team_2 = Team_2()
     report.print(team_2)   # use the instance

     team_3 = Team_3()
     report.print(team_3)   # use the instance
     
     
     
