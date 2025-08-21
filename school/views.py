from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from school.forms import SchoolForm
from school.models import School
# from django.urls import reverse_lazy


@require_POST
def school_register(request):
    form_data = request.POST
    form = SchoolForm(form_data, request.FILES)
    if form.is_valid():
        form.save(request=request)
        return redirect("app:dashboard")

    return render(request, "app/dashboard.html", {"form": form})


@require_GET
@login_required
def school_profile(request):
    school_admin = request.user
    try:
        school_data= school_admin.school
    
    except Exception as e:
        print(e)
        return redirect("app:dashboard")
    
    context={
        'admin': school_admin,
        'school': school_data,
    }
    return render(request, "school/profile.html", context)