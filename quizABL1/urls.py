from django.contrib import admin
from django.urls import path,include
from quizABL1 import views
from quizABL1.views import my_view1
from quizABL1.views import my_view3
from quizABL1.views import my_view4
from .views import quiz_result,quiz_preview

from quizABL1.views import quiz_session_questions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept/', views.my_view, name='dept'),
    path('city/', views.my_view1, name='city'),
    path('session/', views.my_view3, name='session'),
    path('que/', views.my_view4, name='que'),
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.LoginView,name='login'),
    path('home/',views.Homepage,name='home'),
    path('logout/',views.LogOut,name='logout'),

    path('userlist/',views.user_list,name='userlist'),
    path('sessionlist/',views.session_list,name='sessionlist'),
    path('questionlist/',views.question_list,name='questionlist'),
    path('deptlist/',views.dept_list,name='deptlist'),
    path('citylist/',views.city_list,name='citylist'),


    # path('<int:quiz_id>/', views.my_view3, name='sessionupdate'),
    # path('delete/<int:user_id>/', views.user_delete, name='userdelete'),
    path('edituser/<int:user_id>/', views.edit_user, name='edituser'),

    path('delete/<int:quiz_id>/', views.session_delete, name='sessiondelete'),
    path('editq/<int:quiz_id>/', views.edit_session, name='edit_session'),

    path('deletec/<int:pk>/', views.city_delete, name='city_delete'),
    path('editc/<int:pk>/', views.edit_city, name='edit_city'),

    path('deleted/<int:pk>/', views.dept_delete, name='dept_delete'),
    path('editd/<int:pk>/', views.edit_dept, name='edit_dept'), 

    path('deleteque/<int:question_id>/', views.question_delete, name='question_delete'),
    path('editque/<int:question_id>/', views.edit_question, name='edit_question'),

    path('quiz_session_questions/<int:quiz_id>/', views.quiz_session_questions, name='quiz_session_questions'),

    #  path('quiz/<int:quiz_id>/<int:question_id>/', views.answer_question, name='answer_question'),
    path('quiz/<int:quiz_id>/', views.display_quiz, name='display_quiz'),
    # path('quiz/preview/', quiz_preview, name='quiz_preview'),
    # path('quiz_preview/', views.quiz_preview, name='quiz_preview'),
    path('quiz_result/<int:quiz_id>/', quiz_result, name='quiz_result'),
    # path('quiz/<int:quiz_id>/preview/', views.quiz_preview, name='quiz_preview'),
    # path('quiz-preview/<int:quiz_id>/', quiz_preview, name='quiz_preview'),
    path('quiz-preview/<int:quiz_id>/', quiz_preview, name='quiz_preview'),
    # path('quiz/<int:quiz_id>/preview/', views.quiz_preview, name='quiz_preview'),

    path('quiz/<int:quiz_id>/', views.display_quiz, name='display_quiz'),
    path('user_results/', views.user_results, name='user_results'),
    path('all_results/', views.all_results, name='all_results'),


    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy/', views.privacy, name='privacy'),
]