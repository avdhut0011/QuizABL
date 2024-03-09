
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.dept_name
    
class City(models.Model):
    city_name = models.CharField(max_length=40)

    def __str__(self):
        return self.city_name

class CustomUser(AbstractUser): 
    user_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    date_of_joining = models.DateField(blank=True,null=True)
    
    # password = models.


class QuizSession(models.Model):

    quiz_id = models.AutoField(primary_key=True,null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    creator = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    # admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)


    # def __str__(self):
    #     return self.quiz_id
       

class Question(models.Model):

    question_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(QuizSession,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    option5 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

#Trans
class UserAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(QuizSession,on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)
    submit_time = models.DateTimeField(null=True)


class Result(models.Model):
    quiz_id = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    )
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    submit_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"Quiz: {self.quiz_id}, User: {self.user_id}, Status: {self.status}"
