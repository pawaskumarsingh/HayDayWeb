from django.shortcuts import render
from django.views import View

# Create your views here.


class Home(View):
    template_name = 'PublicPage/homepage/home.html'

    def get(self, request):
        return render(request, self.template_name)


class About(View):
    template_name = 'PublicPage/about/about.html'

    def get(self, request):
        return render(request, self.template_name)


class Service(View):
    template_name = 'PublicPage/services/service.html'

    def get(self, request):
        return render(request, self.template_name)


class Projects(View):
    template_name = 'PublicPage/projects/projects.html'

    def get(self, request):
        return render(request, self.template_name)


class ProjectDetail(View):
    template_name = 'PublicPage/projects/project_details.html'

    def get(self, request):
        return render(request, self.template_name)


class Blogs(View):
    template_name = 'PublicPage/blog/blog.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogDetails(View):
    template_name = 'PublicPage/blog/blog_detail.html'

    def get(self, request):
        return render(request, self.template_name)



class Contact(View):
    template_name = 'PublicPage/contact/contact.html'

    def get(self, request):

        return render(request, self.template_name)


class ServiceDetail(View):
    template_name = 'PublicPage/services/service_details.html'

    def get(self, request):

        return render(request, self.template_name)