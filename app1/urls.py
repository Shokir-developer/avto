
from django.urls import path
from .views import homepage, createCars, updateCars, deleteCars

urlpatterns = [
	path('', homepage, name='home'),
	path('create/', createCars, name='create_cars'),
	path('update/<str:pk>/', updateCars, name='update_cars'),
	path('delete/<str:pk>/', deleteCars, name='delete_cars'),
]
