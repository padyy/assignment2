from django.urls import path
from . import views


urlpatterns = [
    path('Home/', views.home_page, name='home_page'),
    path('TrainerCreation/', views.create_trainer, name='create_trainer'),
    path('ReadTrainer/', views.TrainerList.as_view(), name='ReadTrainer'),
    path('success/<str:message>/', views.success, name='success'),
    path('UpdateTrainerPage/', views.TrainerUpdateList.as_view(), name='TrainerUpdateList'),
    path('UpdateTrainer/<int:id>/', views.update_trainer, name='update_trainer'),
    path('DeleteTrainerPage/', views.TrainerDeleteList.as_view(), name='ReadTrainer'),
    path('DeleteTrainer/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('About/', views.about_page, name='about_page'),
    
]