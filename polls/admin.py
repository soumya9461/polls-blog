from django.contrib import admin
from .models import Question, choice

admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls admin area"
admin.site.index_title = "Welcome to Polls admin area"

class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]


#admin.site.register(Question)
#admin.site.register(choice)
admin.site.register(Question, QuestionAdmin)