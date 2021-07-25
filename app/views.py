from django.shortcuts import render, redirect
from .forms import ResumeForms
from .models import Resume
from django.views import View


class HomeView(View):
    def get(self, request):
        candidates = Resume.objects.all()
        form = ResumeForms()
        return render(request, 'app/home.html', {'form': form, 'candidates': candidates})

    def post(self, request):
        form = ResumeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'app/candidate.html', {'candidate': candidate})
