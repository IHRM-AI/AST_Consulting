from django.shortcuts import render
from django.http import JsonResponse
from .models import Job

def job_list(request):
    jobs = list(Job.objects.all().values())
    return JsonResponse(jobs, safe=False)
