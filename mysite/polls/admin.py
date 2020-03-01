from django.contrib import admin

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    ## Now changing admin.StackedInline to admin TabularInline
    ## now instead of
##"Choice objects are edited on the Question admin page"
## this changes the Add Question in admin to provide fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    ## have to specify this or choices fields do not show
    list_filter = ['pub_date']
    ##this adds a filter sidebar in the admin page to sort by pub_date
    list_display = ('question_text', 'pub_date', 'was_published_recently',)
    ## list display changes the columns that are seen on the admin page.
    ## adding the date and published_recently, these fields now show on the
    ## add question table in admin page
    search_fields = ['question_text']
    ## adds a search box at the top of the admin page in questions

## class changes the admin options for a model, in this case Question

admin.site.register(Question, QuestionAdmin)
##adding QuestionAdmin as the second argument to Question,
##let's us access these fields we've provided in QuestionAdmin

## NOTE: this only changes the order of the fields as the appear in the admin page
## NOTE: this let's us define much more detailed/numerous fields in the admin page
