from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from staff_manage.models import Staff
from staff_manage.forms import StaffInfoForm

def list_staff(request):
    staffs = Staff.objects.all()
    context = {"staffs": staffs}        
    return render(request, "list_staff.html", context)

def update_staff(request, id):
    staff = get_object_or_404(Staff, pk=id)
    if request.method == "POST":
        fm = StaffInfoForm(request.POST, instance=staff)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm = StaffInfoForm(instance=staff)
    
    context = {
        'form': fm,
        'staff': staff
    }
    return render(request, "update_staff.html", context)

def delete_staff(request, id):
    staff = get_object_or_404(Staff, pk=id)
    if request.method == "POST":
        staff.delete()
        return redirect('list_staff')
    return render(request, "list_staff.html")

def add_staff(request):
    if request.method == "POST":
        fm = StaffInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StaffInfoForm()
        context={'form': fm}
    return render(request, "add.html", context)

def search_staff(request):
    if request.method == "POST":
        search = request.POST.get('output')
        staffs=None
        if search:
            staffs = Staff.objects.filter(
                Q(fname__icontains=search) |
                Q(lname__icontains=search) |
                Q(email__icontains=search) |
                Q(department__icontains=search) |
                Q(phone__icontains=search)
            )
            return render(request, "list_staff.html", {"staffs": staffs})
        else:
            staffs = Staff.objects.all()
            return render(request, "list_staff.html", {"staffs": staffs})
    else:
        return HttpResponse("An Error Occurred")