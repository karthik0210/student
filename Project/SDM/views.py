from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddCourseForm, RegistrationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


# def send_email(request):
#     subject = 'Subject'
#     message = 'Message.'
#     from_email = 'f@example.com'
#     recipient_list = ['to@example.com']
    
#     send_email(subject, message, from_email, recipient_list)
    
#     return HttpResponse('Email sent successfully!')

# def send_verification_email(user):
#     subject = 'Verify your email address'
#     message = 'Please click the link below to verify your email address.'
#     from_email = 'abc@gmail.com'
#     to_email = user.email
#     send_email(subject, message, from_email, [to_email])

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            user = User.objects.create_user(username=student.email, password='defaultpassword')
            # Send registration email and WhatsApp message
            messages.success(request, "Registration successful! Please check your email and WhatsApp for your login details.")
        return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request, 'success.html')


@user_passes_test(lambda u: u.is_superuser)  # Ensures only admin users can access this view
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course added successfully!")
        return redirect('add-course-success')  # Redirect to a page where courses are listed
    else:
        form = AddCourseForm()
    
    return render(request, 'add_course.html', {'form': form})

def add_course_success(request):
    return render(request, 'add_course_success.html')