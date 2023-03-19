from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})