from django.http import HttpResponse


def Index(request):
    return HttpResponse("This is home <br> <a href='/admin/'>Admin</a> <br> <a href='/course/'>Course</a>")