from django.shortcuts import render
from .login import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
  