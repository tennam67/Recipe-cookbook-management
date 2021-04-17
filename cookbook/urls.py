from django.urls import path

from cookbook.views import GetCreateBookView, GetUpdateDeleteBookView

urlpatterns = [

    path('', GetCreateBookView.as_view()),
    path('<int:pk>/', GetUpdateDeleteBookView.as_view())

]



