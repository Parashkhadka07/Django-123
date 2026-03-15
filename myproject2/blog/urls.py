from django.urls import path,re_path
from .import views

urlpatterns=[
    path('post/<int:post_id>/',views.post_details,name='post_details'),
    path('user/<str:username>',views.user_profile,name='username'),
    path('dates/<int:year>/<int:month>/<int:day>',views.dates,name='dates')
]