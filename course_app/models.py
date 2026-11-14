from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('teacher','teacher'),
    ('client','client'),
    )

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length = 100)
    profile_picture = models.ImageField(upload_to = 'profile_image')
    role = models.CharField(max_length=10,choices = ROLE_CHOICES,default = 'client')

class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField()
    teacher_role = models.CharField(max_length = 10,choices = ROLE_CHOICES,default = 'teacher')
    bio = models.TextField()

class Student(UserProfile):
    student_role = models.CharField(max_length=10,choices = ROLE_CHOICES,default = 'client')

class Links(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    links_url = models.URLField()

class Category(models.Model):
    category_name = models.CharField(max_length = 100, unique = True)

class Course(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 100)
    description = models.TextField()
    LEVEL_CHOICES = (
        ('beginner','beginner'),
        ('intermediate','intermediate'),
        ('advanced','advanced'),
    )
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Lesson(models.Model):
    name_lesson = models.CharField(max_length = 100)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

class Assignment(models.Model):
    name_assignment = models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

class Exam(models.Model):
    name = models.CharField(max_length = 100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()

class Question(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    name_question = models.CharField(max_length = 100)
    text = models.TextField()


class Answers(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answers = models.TextField()
    true_answer = models.BooleanField()

class Certificate(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.URLField()

class CourseReview(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(str(i), i) for i in range(1,6)])
    comment = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.item.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def get_total_price(self):
        return self.course.price

class Favorite(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite_item')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)












