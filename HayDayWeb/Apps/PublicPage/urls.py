
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name="home_page"),
    path('about-us', About.as_view(), name="home_about_us"),
    path('services', Service.as_view(), name="home_services"),
    path('service-details', ServiceDetail.as_view(), name="home_service_details"),
    path('projects', Projects.as_view(), name="home_projects"),
    path('project-details', ProjectDetail.as_view(), name="home_project_detail"),
    path('blogs', Blogs.as_view(), name="home_blogs"),
    path('blog-details', BlogDetails.as_view(), name="home_blog_detail"),
    path('contact', Contact.as_view(), name="home_contact"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
