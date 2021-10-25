from django.urls import path
#https://www.youtube.com/watch?v=22TkO8og4_Q
#https://github.com/tomitokko/bitcoinwallet/tree/master/wallet
from . import views
urlpatterns=[path("",views.index,name='index'),
path("login",views.loginus,name='loginus'),
path("logout",views.logoutus,name='logoutus'),
path("dash",views.dash,name='dash'),
path('play/<int:pk>/',views.play,name="play"),
path('create',views.create,name="create"),
path('donate',views.donate,name='donate'),
path('register',views.register,name="register"),
path('api/userlist',views.userlist.as_view(),name='userlist'),
path('api/courselist',views.CourseList.as_view(),name='courselist'),
path('api/enrolledlist',views.EnrolledList.as_view(),name='enrolledlist'),

]
