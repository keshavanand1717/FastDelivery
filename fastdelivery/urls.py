from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views
from core.courier import apis as courier_apis
from django.conf import settings
from django.conf.urls.static import static

cutomer_urlpatterns = [
    path('',customer_views.home,name="home"),
    path('profile/',customer_views.profile_page,name="profile"),
    path('payment/',customer_views.payment_method_page,name="payment"),
    path('create_job/',customer_views.create_job_page,name="create_job"),
    
    path('jobs/current/',customer_views.current_jobs_page,name="current_jobs"),
    path('jobs/archived/',customer_views.archived_jobs_page,name="archived_jobs"),
    path('jobs/<job_id>/',customer_views.job_page,name="job"),
    
]
courier_urlpatterns = [
    path('',courier_views.home,name="home"),
    path('jobs/current/',courier_views.current_job_page,name="current_job"),
    path('jobs/available/',courier_views.jobs_available,name="available_jobs"),
    path('jobs/<job_id>/',courier_views.job_page,name="courier_job"),
    path('jobs/current/',courier_views.current_job_page,name="current_job"),
    path('jobs/current/<id>/take_photo/',courier_views.current_job_take_photo_page,name="current_job_take_photo"),
    path('api/jobs/current/<id>/update/',courier_apis.current_job_update_api,name="current_job_update_api"),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/',views.sign_up),

    path('customer/', include((cutomer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
