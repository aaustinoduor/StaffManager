from django.urls import path
from .views import list_staff, update_staff, delete_staff, add_staff, search_staff

urlpatterns = [
    path('', list_staff, name='list_staff'),
    path('update_staff/<int:id>/', update_staff, name='update_staff'),
    path('delete_staff/<int:id>/', delete_staff, name='delete_staff'),
    path('add/', add_staff, name="add_staff"),
    path("search_staff", search_staff, name="search")
]
