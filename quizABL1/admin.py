from django.contrib import admin
from .models import Department, City, CustomUser, QuizSession, Question, UserAnswer,Result
from django.contrib.auth.admin import UserAdmin



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name',)

admin.site.register(Department, DepartmentAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)

admin.site.register(City, CityAdmin)

class admincustomuser(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields':(
                    'dept',
                    'city',
                    'date_of_birth',
                    # ' date_of_joining',
                )
            }
        )
    )
admin.site.register(CustomUser,admincustomuser)


class QuizSessionAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'creator','subject','start_time', 'end_time')
    search_fields = ('quiz_id',)

admin.site.register(QuizSession, QuizSessionAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id','quiz_id', 'question_text','correct_answer')
    search_fields = ('question_id', 'question_text')

admin.site.register(Question, QuestionAdmin)

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'quiz_id', 'user_id', 'question_id', 'user_answer','submit_time')
    search_fields = ('answer_id', 'quiz_id__quiz_id', 'user_id__username', 'question_id__question_id')

admin.site.register(UserAnswer, UserAnswerAdmin)


class ResultDisplay(admin.ModelAdmin):
    list_display = ('quiz_id', 'user_id', 'status','submit_time')  # Corrected attribute names
    search_fields = ('quiz_id__quiz_id', 'user_id__username', 'status')

admin.site.register(Result, ResultDisplay)

