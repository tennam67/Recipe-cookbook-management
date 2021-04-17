from django.urls import path

from cookbook.views import GetCreateBookView, GetUpdateDeleteBookView, GetAuthorCookBookView, SearchCookBookView

urlpatterns = [

    path('', GetCreateBookView.as_view()),
    path('<int:book_id>/', GetUpdateDeleteBookView.as_view()),
    path('author/<int:user_id>/', GetAuthorCookBookView.as_view()),
    path('search/<str:ref>/', SearchCookBookView.as_view())

]



