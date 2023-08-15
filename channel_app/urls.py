from django.urls import path
from channel import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('admin/', admin.site.urls),
]
