from accounts import views as accounts_views
# for django images
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('dashboard/', include('dashboard.urls')),
    # Signup url
    path('signup/', accounts_views.signup, name='signup'),

    # Login url:
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Logout url:
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # password reset:
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'
    ),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'
    ),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'
    ),
    # password change:
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'), name='password_change'
    ),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'
    ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for django images
