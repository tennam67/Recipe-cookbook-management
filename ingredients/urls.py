from ingredients.views import GetCreateIngredientView, GetUpdateDeleteIngredientView
from django.urls import path

urlpatterns = [
    path('', GetCreateIngredientView.as_view()),
    path('<int:pk>/', GetUpdateDeleteIngredientView.as_view())
]
