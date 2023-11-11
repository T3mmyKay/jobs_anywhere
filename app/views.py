from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
from django.template import loader

from app.models import JobPost

job_title = [
    "Python Developer",
    "Django Developer",
    "Full Stack Developer",
    "Front End Developer",
]

job_description = [
    "Python Developer Description",
    "Django Developer Description",
    "Full Stack Developer Description",
    "Front End Developer Description",
]


# Create your views here.
def hello(request):
    list = [
        "alpha", "beta"
    ]
    name = "Komolafe Temiloluwa"
    age = 24
    is_authenticated = False
    return render(request, 'app/hello.html',
                  context={'name': name, 'age': age, 'is_authenticated': is_authenticated,
                           'list': list})


def job_list(request):
    jobs = JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request, "app/jobs.html", context=context)


def job_detail(request, id):
    try:
        detail = JobPost.objects.get(id=id)
        if detail.id == 1:
            return redirect(reverse('jobs_home'))
    except JobPost.DoesNotExist:
        return HttpResponseNotFound("Job not found")
    site = "https://www.indeed.com/jobs?q=python&l=New+York%2C+NY"
    return render(request, "app/job_detail.html", context={'job': detail})


def jobs(request):
    html = "<h1>Job List</h1>"
    for i in range(len(job_title)):
        job_index = i
        detail_url = reverse('job_detail', args=(job_index,))
        html += f"<h2><a href='{detail_url}'>{job_title[i]}</a></h2> <h3>{job_description[i]}</h3>"
    return HttpResponse(html)
