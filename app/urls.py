from django.urls import path,include
from . import views

urlpatterns = [
   path('', views.index,name='index'),
   path('view',views.view,name='view'),
   path('update/<int:pk>',views.update,name='update'),
      path('delete/<int:pk>',views.delete,name='delete'),
      path('accounts/', include('django.contrib.auth.urls')),


]
