from django.urls import path
from . import views


urlpatterns = [
    # path('todos/', TodoList.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/completed', views.TodoToggleComplete.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),

]