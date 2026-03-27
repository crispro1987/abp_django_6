from django.urls import path
from .views import home, login_view, logout_view, register_view
#from django.conf.urls import handler404

urlpatterns = [
    path('',home, name="pagina_inicio"),
    path('login',login_view, name="login"),
    path("register",register_view, name="register_form"),
    path('logout', logout_view, name="logout"),
]

#handler404 = 'app.views.error_404'
#handler403 = 'app.views.error_403'