from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice
admin.site.register (Choice)

class QuestionAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('question_text', )}),
        ('Date information', {'fields': ('pub_date', )}) )

admin.site.register (Question, QuestionAdmin)
