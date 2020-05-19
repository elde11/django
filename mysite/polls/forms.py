from django import forms

from .models import Choice


#class QuestionForm(forms.Form):
 #   question2 = forms.ChoiceField(choices=[])
  #  question = forms.ModelChoiceField(queryset=Question.objects.all())


class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.all(),widget = forms.RadioSelect,
    empty_label="none")
    
    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id', None)
        super().__init__(*args, **kwargs)
        if question_id:
            self.fields['choice'].queryset = Choice.objects.filter(question=question_id)
