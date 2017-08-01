from django.conf import settings
from django.db import models
from django_teams.models import Team
from django_pre_post.util import AnswerDisplay, ExpectedAnswerDisplay

QUESTION_TYPES = (
    (1, 'Fill In The Blank'),
    (2, 'Multiple Choice'),
    (3, 'Numeric'),
    (4, 'Open Ended'),
    (5, 'Rank'),
    (6, 'Info'),
)

MULTIPLE_CHOICES = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
)


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    expectedTextAnswer = models.TextField(blank=True, null=True)
    expectedNumericAnswer = models.IntegerField(blank=True, null=True)
    expectedMultipleChoiceAnswer = models.IntegerField(choices=MULTIPLE_CHOICES, blank=True, null=True)
    type = models.IntegerField(choices=QUESTION_TYPES)

    def __unicode__(self):
        data = self.content + ': ' + str(ExpectedAnswerDisplay(self, self))
        return (data[:90] + '...') if len(data) > 90 else data


class Questionaire(models.Model):
    name = models.CharField(max_length=255, default="my questionaire")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField(Question, through='QuestionOrder')
    public = models.BooleanField(default=False)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

    def get_questions(self):
        return self.questions.order_by('link_to_questionaire')


class QuestionOrder(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)
    rank = models.IntegerField()

    class Meta:
        ordering = ('rank',)


class Attempt(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questionaire = models.ForeignKey('django_pre_post.Questionaire', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.id)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attempt = models.ForeignKey(Attempt, blank=True, null=True, on_delete=models.CASCADE)
    textAnswer = models.TextField(blank=True, null=True)
    numericAnswer = models.IntegerField(blank=True, null=True)
    multipleChoiceAnswer = models.IntegerField(choices=MULTIPLE_CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return AnswerDisplay(self, self)
