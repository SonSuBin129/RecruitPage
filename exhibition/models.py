from django.db import models


class Year(models.Model):
    year = models.CharField(max_length=50)

class Team(models.Model):
    year = models.ForeignKey(Year, on_delete = models.CASCADE)
    team = models.CharField (max_length=50)
    p_name = models.TextField()
    photo = models.ImageField(upload_to="")     #여기에 기능설명 및 프로젝트에 대한 설명들이 스크린 샷으로 들어갈 예정

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
    m_id =  models.IntegerField()  #나이 primary_Key 이슈로 id를 m_id로 변경
    major = models.CharField(max_length= 50)

class Info(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    madeby = models.ForeignKey(Member, on_delete= models.CASCADE)
    # planning_background = models.TextField()
    # problem_define = models.TextField()
    # service_info = models.TextField()
    # funtion  = models.ForeignKey(Function, on_delete = models.CASCADE)
    # main_technology = models.ForeignKey(Technology, on_delete = models.CASCADE)
    
#  주석처리된 부분은 향후 관리자페이지로 들어가 글을 작성하는 기능을 만들 경우 Info테이블에 넣을 것들이다(현재는 photo에 이 내용이 다 들어갈 예정) 

# class Technology(models.Model):
#     team =models.ForeignKey(Team, on_delete=models.CASCADE)
#     explain = models.TextField()

# class Function(models.Model):
#     team = models.ForeignKey(Team, on_delete= models.CASCADE)
#     explain = models.TextField()
