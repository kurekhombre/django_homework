from django.urls import path
from calculator import views

urlpatterns = [
    path('', views.calc),
    path('add/<int:value1>/<int:value2>', views.add),    
    path('substract/<int:value1>/<int:value2>', views.substract),    
    path('multiply/<int:value1>/<int:value2>', views.multiply),    
    path('divide/<int:value1>/<int:value2>', views.divide),    
]
