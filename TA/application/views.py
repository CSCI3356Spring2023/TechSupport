from django.shortcuts import render
from .forms import ApplicationForm
from django.contrib import messages
from login.models import CustomUser

def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(id=request.user.id)
            if user.can_apply():
                user.increment_applications()
                user.save()
                form.save()
                return render(request, 'success.html')
            else:
                form.add_error(None, "You have already applied to 5 courses (maximum number of applications)")
        else:
            form = ApplicationForm()
        return render(request, 'application.html', {'form': form})
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})
