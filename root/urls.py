from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('thebughouse.urls')),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('', auth_views.PasswordResetDoneView.as_view(), name="password_reset_complete")
]
