from django.shortcuts import render
from .models import *
app_name = "home"

# Create your views here.

class BaseView(View):
    view = {}

class HomeView(BaseView):
    def get(self, request):
        self.view['categories'] = Category.objects.all()
        self.view['subcategories'] = SubCategory.objects.all()
        self.view['sliders'] = Slider.objects.all()
        self.view['ads'] = Ad.objects.all()
        self.view['products'] = Product.objects.filter(status= 'active')

        return render(request, 'index-4.html', self.view)
def home(request):
    return render(request, 'index-4.html')