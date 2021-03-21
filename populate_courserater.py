import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'CourseRater.settings')

import django
django.setup()
from CourseRate.models import University, Departments, Modules, UserProfile

def populate():

    unis = ['The University of Glasgow',
            'The University of Edinburgh',
            'The University of Oxford']

    departments_modules = { 'Computing Science':['Web Dev', 'Algorithms'],
                   'Economics':['Macroeconomics','Economics 101'],
                  'Media Stdudies':['Advertisting'] }





    for uni in unis:
        u = add_uni(uni)
        for dep in departments_modules:
            d = add_department(u, dep)
            for modu in departments_modules[dep]:
                m = add_module(d, modu)




def add_uni(name):
    u = University.objects.get_or_create(university_name=name)[0]
    u.save()
    return u


def add_department(uni, name):
    d = Departments.objects.get_or_create(university=uni, department_name=name)[0]
    d.department_name = name
    d.save()
    return d


def add_module(department, name):
    m = Modules.objects.get_or_create(department=department, module_name = name)[0]
    m.save()
    return m


#def add_user():

#def add_review():


if __name__ == '__main__':
    print('Starting CourseRater population script...')
    populate()
