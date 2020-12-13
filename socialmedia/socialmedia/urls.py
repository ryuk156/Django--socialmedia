
from django.contrib import admin
from django.urls import path
from posts.views import home_view,posts_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('posts/<int:posts_id>',posts_detail_view)
]
