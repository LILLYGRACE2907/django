from django.http import HttpResponse
from .models import Faculty

def faculty_list(request):
    faculty_records = Faculty.objects.all()
    return HttpResponse(faculty_records)