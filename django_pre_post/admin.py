# This is where you can add stuff to the admin view
from django.contrib import admin

from django_pre_post.models import Answer, Question, Questionaire, Attempt
from django_pre_post.util import AnswerDisplay


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question", "questionaire", "attempt", "owner", 'relevant_answer', 'created', 'modified']
    list_display_links = ["question"]
    fields = ('question', 'owner', 'attempt', 'textAnswer', 'numericAnswer', 'multipleChoiceAnswer')
    readonyfields = ('created', 'modified')

    def relevant_answer(self, obj):
        return AnswerDisplay(self, obj.question)

    def questionaire(self, obj):
        return obj.attempt.questionaire


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['number', 'question_type', 'content', 'expected_answer', 'created', 'modified']
    list_filter = ["questionaire", "type"]
    search_fields = ["content"]

    def question_type(self, obj):
        return obj.get_type_display()

    def expected_answer(self, obj):
        return AnswerDisplay(self,obj)


class QuestionaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'team', 'created', 'modified', 'public']
    list_filter = ["owner", "team"]
    search_fields = ["name", "owner", 'team']


class AttemptAdmin(admin.ModelAdmin):
    list_display = ['questionaire', 'owner', 'created', 'modified']
    list_filter = ["questionaire", "owner"]
    search_fields = ["questionaire", "owner"]


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionaire, QuestionaireAdmin)
admin.site.register(Attempt, AttemptAdmin)
