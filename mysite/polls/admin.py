from django.contrib import admin

from .models import Question

from polls.models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display=('question_text','pub_date')
    list_filter = ('pub_date','id', 'question_text' )
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]



class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['question']



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
