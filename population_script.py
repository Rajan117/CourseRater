import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'CourseRater.settings')

import django
django.setup()
from CourseRate.models import University, Departments, Modules, UserProfile, Review
from django.contrib.auth.models import User
import random
import datetime


def populate():

    unis = ['University of Glasgow',
            'University of Edinburgh',
            'University of Oxford']

    departments_modules = { 'Computing Science':['Web Application Development', 'Algorithms and Data Structures'],
                   'Economics':['Macroeconomics','Economics 101'],
                  'Media Studies':['Advertisting'] }



    for i in range(0,5):
        x = add_user_profile()
        
        

    for uni in unis:
        u = add_uni(uni)
        for dep in departments_modules:
            d = add_department(u, dep)
            for modu in departments_modules[dep]:
                m = add_module(d, modu)
                for i in range(1, random.randint(2,5)):
                    x = add_user_profile()
                    r = add_review(x,m)




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

def add_user_profile():

    user = User.objects.create_user('User'+str(random.randint(10000,9000000)), email=None, password="Test123")
    up = UserProfile.objects.get_or_create(user=user)[0]
    up.save()

    return up

def add_review(x, m):

    sample_text = ["""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam ex. Donec auctor efficitur lobortis.
                    Proin vitae porttitor massa. Proin ut ante quam. Nulla finibus velit ac purus blandit dignissim. Nullam pretium nec tortor nec ornare.
                    Donec semper nibh.""",
                   """Vivamus consectetur ligula leo, a consectetur dui sodales eu. Sed in porttitor mauris. Aenean et sollicitudin est. Nam congue nec libero quis congue.
                    Maecenas et pretium erat, non varius diam. Sed molestie feugiat nunc a finibus. Interdum et malesuada fames.""",
                   """Praesent dolor massa, ultricies in condimentum ac, eleifend luctus velit. Vivamus mollis, felis vitae accumsan porta, turpis magna iaculis nunc, vitae aliquet
                        est leo a nunc. In scelerisque pellentesque ex at luctus. Phasellus tortor nunc, venenatis quis sem auctor, fringilla."""]

    review = Review.objects.get_or_create(module=m,user=x.user,user_profile=x,rev_timestamp=datetime.datetime.now(),
                                          rev_title=str(m.module_name + ' Review'), rev_text = sample_text[random.randint(0,2)],
                                            rev_rating = random.randint(0,11), rev_upvotes = random.randint(0,100), rev_downvotes= random.randint(0,100))[0]
    review.save()

    return review


#def add_review(module, user, user_profile):


if __name__ == '__main__':
    print('Starting CourseRater population script...')
    populate()



