from django.urls import path

from . import views

app_name = 'thebughouse'
urlpatterns = [
    path('', views.home, name="home"),
    path('archive', views.archive, name="archive"),
    path('authors', views.authors, name="authors"),
    path('post', views.post, name="post"),
    path('control/<str:action>', views.control, name="control"),
    path('discussion', views.discussion, name="discussion"),
    path('user/<str:form_type>', views.user, name="user"),
]
