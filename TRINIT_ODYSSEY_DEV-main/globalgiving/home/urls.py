from django.urls import path
from home import views
# from .views import land
urlpatterns = [
    path('register-ngo', views.registerngo, name='registerngo'),
    path('register-phil', views.registerphil, name='registerphil'),
    # path('sign-phil',views.signinphil,name='sign-phil'),
    # path('sign-ngo',views.signinngo,name='sign-ngo'),
    path('',views.home,name='home'),
    path('land',views.land,name='land'),
    path('signupn',views.signupn,name='signupn'),
    path('login',views.LoginPage,name="login"),
    path('signup',views.SignupPage,name="signup"),
    path('ngohome',views.ngohome,name='ngohome'),
    path('philhome',views.philhome,name='philhome'),
    path('ngoprof',views.ngoprof,name='ngoprof'),
    path('ngodisplay',views.ngodisplay,name='ngodisplay'),
    path('contacts',views.gotocon,name='contacts'),
    
]
