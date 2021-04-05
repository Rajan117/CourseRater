from django.test import TestCase
import importlib
import os
import CourseRate.models
import CourseRate.forms
import CourseRate.views
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.template.defaultfilters import slugify
import random
import datetime


# Create your tests here.

#Model tests


#Tests the University model
class UniversityModelTests(TestCase):

    def create_university(self, university_name='The University of Glasgow'):
        return CourseRate.models.University.objects.create(university_name=university_name)

    def test_university_creation(self):
        u = self.create_university()

        self.assertTrue(isinstance(u, CourseRate.models.University))

    def test_str_function(self):
        u = self.create_university()

        self.assertEqual(u.__str__(), u.university_name)

    def test_slug(self):
        u = self.create_university()

        self.assertEqual(slugify(u.university_name), u.slug)




#Tests the Departments Model
class DepartmentsModelTests(TestCase):

    def create_university(self, university_name='The University of Glasgow'):
        return CourseRate.models.University.objects.create(university_name=university_name)


    def create_department(self,department_name='Computing Science'):
        university = self.create_university()
        return CourseRate.models.Departments.objects.create(university=university, department_name=department_name)

    def test_department_creation(self):
        d = self.create_department()

        self.assertTrue(isinstance(d, CourseRate.models.Departments))

    def test_department_uni_instance(self):
        d = self.create_department()

        self.assertTrue(isinstance(d.university, CourseRate.models.University))

    def test_str_function(self):
        d = self.create_department()

        self.assertEqual(d.__str__(), str(d.department_name + " | " + d.university.university_name))

    def test_unique_slug(self):
        d = self.create_department()

        self.assertEqual(slugify(d.university.university_name)+'-'+slugify(d.department_name),d.unique_slug)


#Tests the Modules Model
class ModulesModelTests(TestCase):

    def create_university(self, university_name='The University of Glasgow'):
        return CourseRate.models.University.objects.create(university_name=university_name)


    def create_department(self,department_name='Computing Science'):
        university = self.create_university()
        return CourseRate.models.Departments.objects.create(university=university, department_name=department_name)

    def create_module(self,module_name='WAD2'):
        department = self.create_department()
        return CourseRate.models.Modules.objects.create(department=department,module_name=module_name)

    def test_module_creation(self):
        m = self.create_module()

        self.assertTrue(isinstance(m, CourseRate.models.Modules))

    def test_module_uni_instance(self):
        m = self.create_module()

        self.assertTrue(isinstance(m.department.university, CourseRate.models.University))

    def test_module_department_instance(self):
        m = self.create_module()

        self.assertTrue(isinstance(m.department, CourseRate.models.Departments))

    def test_str_function(self):
        m = self.create_module()

        self.assertEqual(m.__str__(),str(m.module_name + " | " + m.department.department_name + " | "
                + m.department.university.university_name))

    def test_unique_slug(self):
        m = self.create_module()

        self.assertEqual(m.department.unique_slug + "-" + slugify(m.module_name), m.unique_slug)

#Test UserProfile Model
class UserProfileModelTests(TestCase):

    user = User.objects.create_user('User'+str(random.randint(10000,200000)), email=None, password="Test123")

    def create_user_profile(self):
        return CourseRate.models.UserProfile(user=self.user)


    def test_user_profile_creation(self):

        up = self.create_user_profile()

        self.assertTrue(isinstance(up, CourseRate.models.UserProfile))

    def test_user_instance(self):

        up = self.create_user_profile()

        self.assertTrue(isinstance(up.user, User))


#View Tests

class HomeViewTest(TestCase):

    def test_home_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertTemplateUsed(response, 'CourseRater/home.html')


class AboutViewTest(TestCase):

    def test_about_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/about/')
        self.assertTemplateUsed(response, 'CourseRater/about.html')


class RegisterViewTest(TestCase):

    def test_register_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/register/')
        self.assertTemplateUsed(response, 'CourseRater/register.html')


class LoginViewTest(TestCase):

    def test_login_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/login/')
        self.assertTemplateUsed(response, 'CourseRater/login.html')

class AddUniversityViewTest(TestCase):

    def test_not_logged_in(self):

        response = self.client.get('http://127.0.0.1:8000/CourseRate/add_university/')
        self.assertEqual(response.status_code, 302)


#Form Tests

class UniversityFormTests(TestCase):

    def create_university(self, university_name='The University of Edingburgh'):
        return CourseRate.models.University.objects.create(university_name=university_name)

    def test_uni_form_creation(self):

        u = self.create_university()

        form = CourseRate.forms.UniversityForm(data={'university_name' : u.university_name})

        self.assertTrue(isinstance(form, CourseRate.forms.UniversityForm))


    def test_valid_uni_form(self):

        form = CourseRate.forms.UniversityForm(data={'university_name' : 'Random Uni'})

        self.assertTrue(form.is_valid())

    def test_invalid_uni_form(self):

        form = CourseRate.forms.UniversityForm(data={'university_name' : ''})

        self.assertFalse(form.is_valid())


class DepartmentFormTests(TestCase):

    def create_university(self, university_name='The University of Edingburgh'):
        return CourseRate.models.University.objects.create(university_name=university_name)

    def create_department(self,department_name='Computing Science'):
        university = self.create_university()
        return CourseRate.models.Departments.objects.create(university=university, department_name=department_name)

    def test_dep_form_creation(self):

        d = self.create_department()

        form = CourseRate.forms.DepartmentForm(data={'department_name' : d.department_name})

        self.assertTrue(isinstance(form, CourseRate.forms.DepartmentForm))


    def test_valid_dep_form(self):

        form = CourseRate.forms.DepartmentForm(data={'department_name' : 'Physics'})

        self.assertTrue(form.is_valid())

    def test_invalid_dep_form(self):

        form = CourseRate.forms.DepartmentForm(data={'department_name' : ''})

        self.assertFalse(form.is_valid())


class ModuleFormTests(TestCase):

    def create_university(self, university_name='The University of Edingburgh'):
        return CourseRate.models.University.objects.create(university_name=university_name)

    def create_department(self,department_name='Computing Science'):
        university = self.create_university()
        return CourseRate.models.Departments.objects.create(university=university, department_name=department_name)

    def create_module(self,module_name='WAD2'):
        department = self.create_department()
        return CourseRate.models.Modules.objects.create(department=department,module_name=module_name)

    def test_mod_form_creation(self):

        m = self.create_module()

        form = CourseRate.forms.ModuleForm(data={'module_name' : m.module_name})

        self.assertTrue(isinstance(form, CourseRate.forms.ModuleForm))


    def test_valid_mod_form(self):

        form = CourseRate.forms.ModuleForm(data={'module_name' : 'Physics1'})

        self.assertTrue(form.is_valid())

    def test_invalid_mod_form(self):

        form = CourseRate.forms.ModuleForm(data={'module_name' : ''})

        self.assertFalse(form.is_valid())

class ReviewFormTests(TestCase):

    def test_review_form_creation(self):

        form = CourseRate.forms.ReviewForm(data={'rev_title' : 'Physics1 review', 'rev_text' : 'Enjoyed this course very much because...', 'rev_rating' : 6})

        self.assertTrue(isinstance(form, CourseRate.forms.ReviewForm))

    def test_valid_review_form(self):

        form = CourseRate.forms.ReviewForm(data={'rev_title' : 'Physics1 review', 'rev_text' : 'Enjoyed this course very much because...', 'rev_rating' : '6', 'rev_upvotes' : 10, 'rev_downvotes' : 3})

        self.assertTrue(form.is_valid())

    def test_invalid_review_form(self):

        form = CourseRate.forms.ReviewForm(data={'rev_title' : '', 'rev_text' : '', 'rev_rating' : ''})

        self.assertFalse(form.is_valid())

class UserFormTests(TestCase):

    def test_user_form_creation(self):

        form = CourseRate.forms.UserForm(data={'username' : 'TommyS122', 'email' : 't122s@gmail.com', 'password' : 'randompass123'})

        self.assertTrue(isinstance(form, CourseRate.forms.UserForm))


    def test_valid_user_form(self):

        form = CourseRate.forms.UserForm(data={'username' : 'TommyS122', 'email' : 't122s@gmail.com', 'password' : 'randompass123'})

        self.assertTrue(form.is_valid())

    def test_invalid_user_form(self):

        form = CourseRate.forms.UserForm(data={'username' : '', 'email' : 't122s@gmail.com', 'password' : 'randompass123'})

        self.assertFalse(form.is_valid())
        
