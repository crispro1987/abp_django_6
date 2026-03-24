from django.urls import path
from .views import home
#from django.conf.urls import handler404

urlpatterns = [
    path('',home, name="pagina_inicio"),
]

#handler404 = 'app.views.error_404'
#handler403 = 'app.views.error_403'