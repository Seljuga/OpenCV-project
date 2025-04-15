from django.shortcuts import render, get_object_or_404

from counter.models import PeopleCounting


# Create your views here.
def dashboard(request):
    counting_results = PeopleCounting.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'counting_results': counting_results})

def details(request, pk):
    counting_results = get_object_or_404(PeopleCounting, pk=pk)
    return render(request, 'dashboard/details.html', {'counting_results': counting_results})