from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.WishCreate.as_view(), name='wishes_create'),
    path('<int:pk>/delete/', views.WishDelete.as_view(), name='wishes_delete'),  
]

# path('add/', views.ItemCreate.as_view(), name='add_item'),
#  path('<int:pk>/edit/', views.ItemUpdate.as_view(), name='edit_item'),
#  path('<int:pk>/delete/', views.ItemDelete.as_view(), name='delete_item'),
