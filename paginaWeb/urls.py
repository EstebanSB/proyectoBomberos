from django.urls import path

from .views import index
from .views import historia
from .views import galeria
from .views import nosotros
from .views import contacto




urlpatterns = [
    path('',index,name="inicio"),
    path('historia',historia,name="historia"),
    path('galeria',galeria,name="galeria"),
    path('nosotros',nosotros,name="nosotros"),
    path('contacto',contacto,name="contacto"),
    

]
