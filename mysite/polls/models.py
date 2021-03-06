from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, CASCADE

# Create your models here.
class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField('date published')

class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)
