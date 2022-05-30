from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.http import HttpResponse
from .models import User, Teacher, Course, ClassNumber, Subject, CurrentCourse


def get_base_context():

    return {
        'courses': Course.objects.all(),
    }


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = get_base_context()
        context['form'] = UserCreationForm()
        return render(request, self.template_name, context)

    def post(self, request):
        context = get_base_context()
        form = UserCreationForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, self.template_name, context)


@login_required
def show_stream(request):
    context = get_base_context()
    return render(request, 'stream.html', context)


def show_main(request):
    context = get_base_context()
    return render(request, 'mainpage.html', context)


@login_required
def show_courses(request):
    context = get_base_context()
    return render(request, 'courses.html', context)


@login_required
def show_course(request, course_id):
    if not CurrentCourse.objects.filter(c_course_id=course_id).exists():
        current_course = CurrentCourse(c_course_id=course_id,
                                       c_name=Course.objects.get(id=course_id).name,
                                       c_classNumber=Course.objects.get(id=course_id).classNumber.number)
        current_course.save()
    context = get_base_context()
    context['course'] = Course.objects.get(id=course_id)
    return render(request, 'course.html', context)


@login_required
def show_profile(request):
    context = get_base_context()
    context['name'] = request.user.username
    context['email'] = request.user.email
    context['current_courses'] = CurrentCourse.objects.all()
    return render(request, 'profile.html', context)
