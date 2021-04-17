from django.urls import path

# from recipe.views import GetRecipeView, CreateRecipeView
from recipe.views import GetCreateRecipeView, GetUpdateDeleteRecipeView

urlpatterns = [

    path('', GetCreateRecipeView.as_view()),
    path('<int:pk>/', GetUpdateDeleteRecipeView.as_view())
    # path('', GetRecipeView.as_view()),
    # path('create/', CreateRecipeView.as_view()),
]
