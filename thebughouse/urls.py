from django.urls import path

from . import views

app_name = 'thebughouse'
urlpatterns = [
    path('', views.home, name="home"),
    path('archive', views.archive, name="archive"),
    path('authors', views.authors, name="authors"),
    path('post/<int:year>/<str:author>/<str:title>', views.post, name="post"),
    path('control/<str:action>', views.control, name="control"),
    path('discussion', views.discussion, name="discussion"),
    path('discussion/<str:action>', views.discussion, name="discussion-action"),
    path('user/<str:form_type>', views.user, name="user")
]
