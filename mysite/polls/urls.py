from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    #/
    #path ('',views.index,name='index'), # polls:index
    path ('',views.IndexView.as_view(),name='index'),
    #/polls/<question_id>
    path ('<int:question_id>',views.DetailsView.as_view(), name='details'), #polls:details
    path ('<int:question_id>/results',views.ResultsView.as_view(), name='results'), #polls:results
    #<question_id/vote>
    path ('<int:question_id>/vote',views.vote, name='vote'), #polls:details
]