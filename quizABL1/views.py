from collections import Counter
from itertools import count
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone
from django.db.models import Max
from .models import Department,City,CustomUser,QuizSession,Question,UserAnswer,Result
from .forms import DeptForm ,CustomUserForm,CityForm ,SessionForm,LoginForm,QuizQuestionForm,QueForm
from django.contrib import messages


def Homepage(request):
    return render(request,'quizABL1\home.html')


def SignUp(request):
    form = CustomUserForm()

    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        CustomUser._meta.get_field('username')._unique = True
        if form.is_valid():
            form.save()
            messages.info(request, 'Signup Successfully!!!')
            return redirect('login')  # Replace 'success_url' with the URL you want to redirect to after successful form submission
        else:
            return render(request, 'quizABL1\signup.html', {'form': form, 'error': 'Invalid credentials'})
    return render(request, 'quizABL1\signup.html',{'form':form})




def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Login Successfully!!!')
                # Redirect to a success page or home page
                return redirect('home')
            else:
                # Handle invalid login credentials
                return render(request, 'quizABL1\login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = LoginForm()

    return render(request, 'quizABL1\login.html', {'form': form})




def LogOut(request):
    logout(request)
    messages.info(request, 'Logout Successfully!!!')
    return redirect('home')

# dept form
def my_view(request):
   
    if request.method == 'POST':
        # print(request.POST)
        form = DeptForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.info(request, 'Department added Successfully!!!')
            return redirect('home')  
    else:
        form = DeptForm()
    return render(request, 'quizABL1\dept.html', {'form': form})

# city form

def my_view1(request):
   
    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.info(request, 'City added Successfully!!!')
            return redirect('home')  
    else:
        form = CityForm()
    return render(request, 'quizABL1\city.html', {'form': form})


# Quizsession

def my_view3(request):
   
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Session added Successfully!!!')
            return redirect('session')  
           # return HttpResponse('you got success..!')
    else:
        form = SessionForm()
    return render(request, 'quizABL1\session.html', {'form': form})




def edit_session(request,quiz_id): 
    if request.method == 'POST':
        session = QuizSession.objects.get(quiz_id=quiz_id)
        form = SessionForm(request.POST,instance=session)
        if form.is_valid():
            form.save()
            messages.info(request, 'Session edited Successfully!!!')
            return redirect('sessionlist')
        else:
            messages.info(request, 'Something Wrong !!!')
            return redirect('home')
        
    else:
        session = QuizSession.objects.get(quiz_id=quiz_id)
        form = SessionForm(instance=session)
    return render(request, 'quizABL1\editsession.html', {'form': form})
            



# Questions

def my_view4(request):
   
    if request.method == 'POST':
        # print(request.POST)
        form = QueForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.info(request, 'Questions added Successfully!!!')
            return redirect('que')  
    else:
        form = QueForm()
    return render(request, 'quizABL1\que.html', {'form': form})



def user_list(request):
    context = {'userlist':CustomUser.objects.all() }
    return render(request, "quizABL1/userlist.html",context)


def session_list(request):
    context = {'sessionlist':QuizSession.objects.all() }
    return render(request, "quizABL1\sessionlist.html",context)

def dept_list(request):
    context = {'deptlist':Department.objects.all() }
    return render(request, "quizABL1\deptlist.html",context)

def city_list(request):
    context = {'citylist':City.objects.all() }
    return render(request, "quizABL1\citylist.html",context)

def question_list(request):
    context = {'questionlist':Question.objects.all() }
    return render(request, "quizABL1\questionlist.html",context)

# def user_delete(request, user_id):
   
#     user = CustomUser.objects.get(pk=user_id)
#     user.delete()
#     messages.info(request, 'User deleted successfully!')
#     return redirect('userlist')

# def user_delete(request, user_id):
#     try:
#         user = CustomUser.objects.get(pk=user_id)
#     except CustomUser.DoesNotExist:
#         messages.error(request, 'User does not exist.')
#         return redirect('userlist')

    user.delete()
    messages.info(request, 'User deleted successfully!')
    return redirect('userlist')

def session_delete(request, quiz_id):
    
    session = QuizSession.objects.get(pk=quiz_id)
    session.delete()
    messages.info(request, 'Session deleted successfully!')
    return redirect('sessionlist')

#edit_user

def edit_user(request,user_id): 
    if request.method == 'POST':
        user = CustomUser.objects.get(user_id=user_id)
        form = CustomUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'User edited Successfully!!!')
            return redirect('userlist')
        else:
            messages.info(request, 'Something Wrong !!!')
            return redirect('home')
        
    else:
        user = CustomUser.objects.get(user_id=user_id)
        form = CustomUserForm(instance=user)
    return render(request, 'quizABL1\edituser.html', {'form': form})


#edit_city

def edit_city(request,pk): 
    if request.method == 'POST':
        city = City.objects.get(pk=pk)
        form = CityForm(request.POST,instance=city)
        if form.is_valid():
            form.save()
            messages.info(request, 'City edited Successfully!!!')
            return redirect('citylist')
        else:
            messages.info(request, 'Something Wrong !!!')
            return redirect('home')
        
    else:
        city = City.objects.get(pk=pk)
        form = CityForm(instance=city)
    return render(request, 'quizABL1\editcity.html', {'form': form})

def city_delete(request,pk):
    city = City.objects.get(pk=pk)
    city.delete()
    messages.info(request, 'City deleted Successfully!!!')
    return redirect('citylist')

#Edit department 

def edit_dept(request,pk): 
    if request.method == 'POST':
        dept = Department.objects.get(pk=pk)
        form = DeptForm(request.POST,instance=dept)
        if form.is_valid():
            form.save()
            messages.info(request, 'Department edited Successfully!!!')
            return redirect('deptlist')
        else:
            messages.info(request, 'Something Wrong !!!')
            return redirect('home')
        
    else:
        dept = Department.objects.get(pk=pk)
        form = DeptForm(instance=dept)
    return render(request, 'quizABL1\editdept.html', {'form': form})

def dept_delete(request,pk):
    dept = Department.objects.get(pk=pk)
    dept.delete()
    messages.info(request, 'Department deleted Successfully!!!')
    return redirect('deptlist')



#Edit Question

def edit_question(request,question_id): 
    if request.method == 'POST':
        question = Question.objects.get(question_id=question_id)
        form = QueForm(request.POST,instance=question)
        if form.is_valid():
            form.save()
            messages.info(request, 'Question edited Successfully!!!')
            return redirect('questionlist')
        else:
            messages.info(request, 'Something Wrong !!!')
            return redirect('home')
        
    else:
        question = Question.objects.get(question_id=question_id)
        form = QueForm(instance=question)
    return render(request, 'quizABL1\editque.html', {'form': form})



def question_delete(request,question_id):
    question = Question.objects.get(pk = question_id) 
    question.delete()
    messages.info(request, 'Question deleted Successfully!!!')
    return redirect('questionlist')


def Homepage(request):
    # Retrieve quiz sessions from the database
    quiz_sessions = QuizSession.objects.all()
    return render(request, 'quizABL1/home.html', {'quiz_sessions': quiz_sessions})

def quiz_session_questions(request, quiz_id):
    quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_session)
    context = {'quiz_session': quiz_session, 'questions': questions}
    return render(request, 'quizABL1/quiz.html', context)


# def display_quiz(request, quiz_id):
#     quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
#     current_time = timezone.now()
#     if(quiz_session.start_time>current_time<=quiz_session.end_time):
#         start_time_str = quiz_session.start_time.strftime("%Y-%m-%d   %H:%M:%S")
#         messages.info(request, f'Quiz is not start yet!!!  Start Time: {start_time_str}')
#         return redirect('home')
#     elif not (quiz_session.start_time <= current_time <= quiz_session.end_time):
#         messages.info(request, 'Quiz session is expired!!!')
#         return redirect('home')
    
       
#     if request.method == 'POST':
#         action = request.POST.get('action')
        
#         if action != 'submit':
#             quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
#             questions = Question.objects.filter(quiz_id=quiz_session)
#             current_question_index = request.session['current_question_index']
#             current_question = questions[current_question_index]

#             form = QuizQuestionForm(request.POST, prefix='question', instance=current_question)
#             if form.is_valid():
#                 selected_option = form.cleaned_data['selected_option']
#                 session_key = f'selected_option_{current_question.question_id}'
#                 request.session[session_key] = selected_option

#             if action == 'next' and current_question_index + 1 < len(questions):
#                 current_question_index += 1
#             elif action == 'previous' and current_question_index - 1 >= 0:
#                 current_question_index -= 1

#             request.session['current_question_index'] = current_question_index

#             return redirect('display_quiz', quiz_id=quiz_id)

#         else:
#             quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
#             questions = Question.objects.filter(quiz_id=quiz_session)
#             user = request.user

#             # Initialize an empty list to store user answers
#             user_answers = []

#             # Get the current time as the submit time
#             submit_time = timezone.now()

#             for question in questions:
#                 session_key = f'selected_option_{question.question_id}'
#                 selected_option = request.session.get(session_key)

#                 if selected_option:
#                     # Get the text value of the selected option
#                     selected_option_text = getattr(question, selected_option)
#                     user_answer_instance = UserAnswer(
#                         quiz_id=quiz_session,
#                         user_id=user,
#                         question_id=question,
#                         user_answer=selected_option_text,
#                         submit_time=submit_time  # Assign the submit time here
#                     )
#                     user_answers.append(user_answer_instance)

#             # Bulk create user answers
#             UserAnswer.objects.bulk_create(user_answers)

#             # Clear session data
#             for question in questions:
#                 session_key = f'selected_option_{question.question_id}'
#                 if session_key in request.session:
#                     del request.session[session_key]
#             request.session.modified = True
        
#             request.session.pop('current_question_index', None)
#             request.session.pop('current_quiz_session_id', None)
#             messages.info(request, 'Exam Submitted Successfully!!!')
#             return redirect('quiz_result', quiz_id=quiz_id)

#     else:
#         quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
#         questions = Question.objects.filter(quiz_id=quiz_session)

#         if 'current_quiz_session_id' not in request.session or request.session['current_quiz_session_id'] != quiz_id:
#             request.session['current_question_index'] = 0
#             request.session['current_quiz_session_id'] = quiz_id

#         current_question_index = request.session['current_question_index']
#         current_question = questions[current_question_index]
#         is_last_question = current_question_index + 1 >= len(questions)

#         options = [(f'option{i}', getattr(current_question, f'option{i}')) for i in range(1, 6)]
#         session_key = f'selected_option_{current_question.question_id}'
#         selected_option = request.session.get(session_key)
#         form = QuizQuestionForm(prefix='question', instance=current_question, initial={'selected_option': selected_option})
#         form.fields['selected_option'].choices = options

#         question_number = current_question_index + 1

        
    

#         return render(request, 'quizABL1/quiz.html', {'quiz_session': quiz_session, 'form': form, 'current_question': current_question, 'question_number': question_number, 'is_last_question': is_last_question})




def display_quiz(request, quiz_id):
    quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
    current_time = timezone.now()

    if quiz_session.start_time > current_time <= quiz_session.end_time:
        start_time_str = quiz_session.start_time.strftime("%Y-%m-%d   %H:%M:%S")
        messages.info(request, f'Quiz is not start yet!!!  Start Time: {start_time_str}')
        return redirect('home')
    elif not (quiz_session.start_time <= current_time <= quiz_session.end_time):
        messages.info(request, 'Quiz session is expired!!!')
        return redirect('home')

    if request.method == 'POST':
        action = request.POST.get('action')

        quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
        questions = Question.objects.filter(quiz_id=quiz_session)
        current_question_index = request.session.get('current_question_index', 0)
        current_question = questions[current_question_index]

        form = QuizQuestionForm(request.POST, prefix='question', instance=current_question)
        if form.is_valid():
            selected_option = form.cleaned_data['selected_option']
            session_key = f'selected_option_{current_question.question_id}'
            request.session[session_key] = selected_option

        if action == 'next' and current_question_index + 1 < len(questions):
            current_question_index += 1
        elif action == 'previous' and current_question_index - 1 >= 0:
            current_question_index -= 1
        elif action == 'submit' and current_question_index == len(questions) - 1:
            # Handle quiz submission if the user is on the last question and clicks "Submit"
            return submit_quiz(request, quiz_id)

        request.session['current_question_index'] = current_question_index

        return redirect('display_quiz', quiz_id=quiz_id)

    else:
        quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
        questions = Question.objects.filter(quiz_id=quiz_session)

        current_question_index = request.session.get('current_question_index', 0)
        current_question = questions[current_question_index]
        is_last_question = current_question_index + 1 >= len(questions)

        options = [(f'option{i}', getattr(current_question, f'option{i}')) for i in range(1, 6)]
        session_key = f'selected_option_{current_question.question_id}'
        selected_option = request.session.get(session_key)
        form = QuizQuestionForm(prefix='question', instance=current_question, initial={'selected_option': selected_option})
        form.fields['selected_option'].choices = options

        question_number = current_question_index + 1

        return render(request, 'quizABL1/quiz.html', {'quiz_session': quiz_session, 'form': form, 'current_question': current_question, 'question_number': question_number, 'is_last_question': is_last_question})

def submit_quiz(request, quiz_id):
    # Handle quiz submission
    # This function will be called when the user submits the last question
    quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_session)
    user = request.user

    # Initialize an empty list to store user answers
    user_answers = []

    # Get the current time as the submit time
    submit_time = timezone.now()

    for question in questions:
        session_key = f'selected_option_{question.question_id}'
        selected_option = request.session.get(session_key)

        if selected_option:
            # Get the text value of the selected option
            selected_option_text = getattr(question, selected_option)
            user_answer_instance = UserAnswer(
                quiz_id=quiz_session,
                user_id=user,
                question_id=question,
                user_answer=selected_option_text,
                submit_time=submit_time  # Assign the submit time here
            )
            user_answers.append(user_answer_instance)

    # Bulk create user answers
    UserAnswer.objects.bulk_create(user_answers)

    # Clear session data
    for question in questions:
        session_key = f'selected_option_{question.question_id}'
        if session_key in request.session:
            del request.session[session_key]
    request.session.modified = True

    request.session.pop('current_question_index', None)
    request.session.pop('current_quiz_session_id', None)
    messages.info(request, 'Exam Submitted Successfully!!!')
    return redirect('quiz_result', quiz_id=quiz_id)


def quiz_result(request, quiz_id):
    # Retrieve the quiz session
    quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
    
    # Retrieve all questions for this quiz session
    questions = Question.objects.filter(quiz_id=quiz_session)
    
    # Get the user's answers for these questions
    max_time = UserAnswer.objects.filter(quiz_id=quiz_session, user_id=request.user).aggregate(max_submit_time=Max('submit_time'))
    user_answers = UserAnswer.objects.filter(quiz_id=quiz_session, user_id=request.user)
    
    # Create a dictionary to store question IDs and their corresponding user answers
    user_answers_dict = {answer.question_id_id: answer.user_answer for answer in user_answers}
    
    # Ensure all questions have an entry in the user_answers_dict

    for question in questions:
        if question.question_id not in user_answers_dict:
            user_answers_dict[question.question_id] = "None"
    
    # Calculate the score and prepare results
    correct_count = 0
    results = []

    for question in questions:
        
        user_answer = user_answers_dict[question.question_id]
        correct_answer = question.correct_answer

        # Check if the user's answer exists
        is_correct = user_answer == correct_answer

        # Append the result for this question to the results list
        results.append({
            'question_text': question.question_text,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
            
        })

        # Increment correct count if the user's answer is correct
        if is_correct:
            correct_count += 1

    # Calculate the score percentage
    total_questions = len(questions)
    score_percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0

    # Save the result to the Result model
    result_value = score_percentage / 100  # Storing the score as a value between 0 and 1
    pass_threshold = 0.5  # You can adjust the pass threshold as needed
    is_pass = score_percentage >= (pass_threshold * 100)

    # Save max_time as submit_time
    submit_time = max_time['max_submit_time']

    # Create and save the Result instance
    Result.objects.create(
        quiz_id=quiz_session,
        user_id=request.user,
        status="Pass" if is_pass else "Fail",
        submit_time=submit_time
    )

    # Render the quiz result template with the calculated score and results
    return render(request, 'quizABL1/quiz_result.html', {
        'quiz_session': quiz_session,
        'total_questions': total_questions,
        'correct_count': correct_count,
        'incorrect_count': total_questions - correct_count,
        'score_percentage': score_percentage,
        'results': results,
        'submit_time': submit_time 
    })




def quiz_preview(request, quiz_id):
    quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_session)
    selected_options = {}

    for question in questions:
        session_key = f'selected_option_{question.question_id}'
        selected_option = request.session.get(session_key)
        selected_options[question] = selected_option

    return render(request, 'quizABL1/quiz_preview.html', {'quiz_session': quiz_session, 'selected_options': selected_options})


# from django.http import JsonResponse

# def quiz_preview(request, quiz_id):
#     quiz_session = get_object_or_404(QuizSession, quiz_id=quiz_id)
#     questions = Question.objects.filter(quiz_id=quiz_session)
#     print("que")
#     print(questions)
    
#     selected_options = {}

#     for question in questions:
#         session_key = f'selected_option_{question.question_id}'
#         selected_option = request.session.get(session_key)
#         selected_options[question.question_text] = selected_option

#     return JsonResponse({'quiz_session': quiz_session.subject, 'selected_options': selected_options})

 
@login_required
def user_results(request):
    results = Result.objects.filter(user_id=request.user)
    return render(request, 'quizABL1/user_results.html', {
        # 'results_with_info': results_with_info,
        'results':results})


@login_required
def all_results(request):
    # Restrict access to staff members (superusers)
    if not request.user.is_staff:
        return redirect('home')  # Redirect to homepage or appropriate URL
    results = Result.objects.filter(user_id=request.user)
    return render(request, 'quizABL1/user_results.html', {
        'results':results})
    

def about_us(request):
    return render(request, 'quizABL1/about_us.html')

def privacy(request):
    return render(request, 'quizABL1/privacy.html')

def contacts(request):
    return render(request, 'quizABL1/contacts.html')