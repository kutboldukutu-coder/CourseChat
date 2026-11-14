from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class LinksInline(admin.TabularInline):
    model = Links
    extra = 1

@admin.register(Category, Course, Lesson, Assignment, Exam, Question, Answers)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class StudentAdmin(admin.ModelAdmin):
    inlines = [LinksInline]

admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Links)
admin.site.register(Certificate)
admin.site.register(CourseReview)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)









