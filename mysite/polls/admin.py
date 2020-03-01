from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
## class changes the admin options for a model, in this case Question

admin.site.register(Question, QuestionAdmin)
##adding QuestionAdmin as the second argument to Question,
##let's us access these fields we've provided in QuestionAdmin

## NOTE: this only changes the order of the fields as the appear in the admin page
## NOTE: this let's us define much more detailed/numerous fields for admin page
