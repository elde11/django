from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from polls.models import Question,Choice
from django.utils import timezone
from .forms import VoteForm
from django.views.generic import ListView, DetailView



class IndexView(ListView):
    template_name = "polls/index.html" # renderowany szablon
    model = Question # queryset = Question.objects.all() 
    queryset = Question.objects.all() #skad brane obiekty do widoku
    context_object_name = 'question_list' # zmiena z wynikami do szablonu
    extra_context = {                     # dodatkowe zmienne do szablonu
        'title': 'List of question'
    }

class DetailsView(DetailView):
    template_name = "polls/details.html"
    model = Question
    pk_url_kwarg = 'question_id'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Question {self.object.id}',
            'form' : VoteForm(question_id=self.object.id),
        }
        context.update(kwargs)
        return super().get_context_data(**context)

class ResultsView(DetailView):
    template_name = "polls/results.html"
    model = Question
    pk_url_kwarg = 'question_id'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Question {self.object.id}',
            'form' : VoteForm(question_id=self.object.id),
        }
        context.update(kwargs)
        return super().get_context_data(**context)

def index (request):
    results = Question.objects.all()
    return render(request,"polls/index.html",{'title':'list of question','question_list':results})



def details (request,question_id):
    results = get_object_or_404(Question,id=question_id)
    #results = Question.objects.get(id=question_id)# dokładnie 1 wynik
    return render(
        request,"polls/details.html",
        {
            'title':f'Question{results.id}','question':results,
            'choices_filtred':results.choice_set.filter(choice_text__icontains="a"),
            'form': VoteForm(question_id=question_id),
            
        },
            
    )

def vote(request, question_id):
    # 1. sprawdzić czy POST
    # 2. odczytać dane POST
    # 3. sprawdzić poprawność danych POST
    # 4. akcja:
    #   - oddanie głosu na dany wybór
    #   - wyświetlić komunikat o zagłosowaniu poprawnie
    #   - przekierować użytkownika
    #
    # jeżeli nie POST -> akcje
    # jeżeli dane POST niepoprawne -> akcje
    # --------------------------
    # 1. sprawdzić czy POST
    if request.method == "POST":
        # 2. odczytać dane POST
        form = VoteForm(request.POST, question_id=question_id)
        
        # 3. sprawdzić poprawność danych POST
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice.votes += 1
            choice.save()

            print (f"Zagłosowano poprawnie na Choice {{choice.id}}")
            #   - przekierować użytkownika
            return redirect ('polls:results', question_id)
        else:
            print("Niepoprawne Dane")
            return redirect ('polls:details', question_id)

        #question = get_object_or_404(Question, id=question_id)
        #try:
        #    choice_id = int(data.get('choice', 0))
        #    choice = question.choice_set.get(id=choice_id)
        #except (ValueError, Choice.DoesNotExist):
            # jeżeli dane POST niepoprawne -> akcje
        #    print("Niepoprawne Dane")
        #    return redirect ('polls:details', question_id)
        #else:
            # 4. akcja:
            #   - oddanie głosu na dany wybór
        #    choice.votes += 1
         #   choice.save()
            #   - wyświetlić komunikat o zagłosowaniu poprawnie
          #  print (f"Zagłosowano poprawnie na Choice {{choice.id}}")
            #   - przekierować użytkownika
           # return redirect ('polls:details', question_id)
            
            #
    # jeżeli nie POST -> akcje
    else:
        return redirect('https://niebezpiecznik.pl/')
    # jezeli dane POST niepoprawne -> akcje 
    
     



