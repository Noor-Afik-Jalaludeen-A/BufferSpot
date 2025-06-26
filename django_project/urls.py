from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.models import User
from django.apps import apps
from django.db import connection
from django.db.models.signals import post_save
from users.models import Profile
from users.signals import create_user_profile, save_profile

def setup_view(request):
    try:
        # Disconnect signals to avoid auto profile creation during loaddata
        post_save.disconnect(create_user_profile, sender=User)
        post_save.disconnect(save_profile, sender=User)

        # Clear all data
        with connection.constraint_checks_disabled():
            for model in apps.get_models():
                model.objects.all().delete()
        connection.check_constraints()

        # Load fixture
        call_command('loaddata', 'db_backup.json')

        # Create superuser if not present
        if not User.objects.filter(username='NoorAfikJalaludeenA').exists():
            User.objects.create_superuser(
                username='NoorAfikJalaludeenA',
                email='noorafikjalaludeen2204@gmail.com',
                password='Afza@2122'
            )

        # Reconnect signals
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_profile, sender=User)

        return HttpResponse("✅ Data loaded and superuser created successfully.")
    
    except Exception as e:
        return HttpResponse(f"❌ Error: {str(e)}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup/', setup_view),
    path('', include('Blog.urls')),
    path('', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
