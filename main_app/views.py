from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView

from .models import Wish

# Create your views here.
class WishCreate(CreateView):
  model = Wish
  fields = '__all__'
    

class WishDelete(DeleteView):
  model = Wish
  success_url = '/'

def home(request):
    wishes = Wish.objects.all()
    return render(request, 'home.html', {'wishes': wishes})  

    

