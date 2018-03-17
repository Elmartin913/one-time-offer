from django.shortcuts import render

from .forms import SubmitUrlForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            'form': the_form,
            'title': 'Submit url: ',
        }
        return render(request, 'home.html', context)