from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CourseRate.forms import UserForm, UserProfileForm, UniversityForm, DepartmentForm, ModuleForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from CourseRate.models import University, Departments, Modules


def home(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    response = render(request, 'CourseRater/home.html', context=context_dict)
    return response


def about(request):
    context_dict = {}
    response = render(request, 'CourseRater/about.html', context=context_dict)
    return response


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:

            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'CourseRater/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('CourseRate:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'CourseRater/login.html')


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('CourseRate:home'))


def add_university(request):
    form = UniversityForm()

    if request.method == 'POST':
        form = UniversityForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/CourseRate/')
        else:
            print(form.errors)

    return render(request, 'CourseRater/add_university.html', {'form': form})


def add_department(request, university_name_slug):
    try:
        university = University.objects.get(slug=university_name_slug)
    except:
        university = None
        return redirect('/CourseRater/')

    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():

            if university:
                department = form.save(commit=False)
                department.university = university
                department.save()
                return redirect(
                    reverse('CourseRate:show_university', kwargs={'university_name_slug': university_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'university': university}
    return render(request, 'CourseRater/add_department.html', context_dict)

def add_module(request, university_name_slug, department_name_slug):
    try:
        university = University.objects.get(slug=university_name_slug)
    except:
        university = None
        return redirect('/CourseRater/')

    try:
        department = Departments.objects.get(university=university, slug=department_name_slug)
    except:
        department = None
        return redirect(
            reverse('CourseRate:show_university', kwargs={'university_name_slug': university_name_slug}))

    form = ModuleForm()

    if request.method == 'POST':
        form = ModuleForm(request.POST)

        if form.is_valid():

            if university and department:
                module = form.save(commit=False)
                module.department = department
                module.save()
                return redirect(
                    reverse('CourseRate:show_department', kwargs={'university_name_slug': university_name_slug, 'department_name_slug': department_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'university': university, 'department': department}
    return render(request, 'CourseRater/add_module.html', context_dict)



def show_university(request, university_name_slug):
    context_dict = {}

    try:
        university = University.objects.get(slug=university_name_slug)

        departments = Departments.objects.filter(university=university)

        context_dict['departments'] = departments

        context_dict['university'] = university

    except University.DoesNotExist:

        context_dict['university'] = None

    return render(request, 'CourseRater/university.html', context=context_dict)


def show_department(request, university_name_slug, department_name_slug):
    context_dict = {}

    try:
        university = University.objects.get(slug=university_name_slug)
        context_dict['university'] = university

        try:
            department = Departments.objects.get(university=university, slug=department_name_slug)
            context_dict['department'] = department

            modules = Modules.objects.filter(department=department)
            context_dict['modules'] = modules

        except Departments.DoesNotExist:
            context_dict['department'] = None

    except University.DoesNotExist:

        context_dict['university'] = None
        return render(request, 'CourseRater/university.html', context=context_dict)

    return render(request, 'CourseRater/department.html', context=context_dict)


def show_module(request, university_name_slug, department_name_slug, module_name_slug):
    context_dict = {}

    try:
        university = University.objects.get(slug=university_name_slug)
        context_dict['university'] = university

        try:
            department = Departments.objects.get(university=university, slug=department_name_slug)
            context_dict['department'] = department

            try:
                module = Modules.objects.get(department=department, slug=module_name_slug)
                context_dict['module'] = module

            except Modules.DoesNotExist:
                context_dict['module'] = None

        except Departments.DoesNotExist:
            context_dict['department'] = None
            return redirect(
                reverse('CourseRate:show_department', kwargs={'department_name_slug': department_name_slug}))

    except:
        context_dict['university'] = None
        return redirect(
            reverse('CourseRate:show_university', kwargs={'university_name_slug': university_name_slug}))

    return render(request, 'CourseRater/module.html', context=context_dict)
