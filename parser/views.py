
from django.shortcuts import redirect
import requests

from django.views.generic import View, ListView, DetailView
from django.core.paginator import Paginator
import shutil
import xml.etree.ElementTree as ET
from parser.models import Mark, Model
from django.core.paginator import Paginator



class DawnloadView(View):
    
    def get(self, request):
        url = 'https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml'
        file_path = 'cars.xml'

        Model.objects.all().delete()
        Mark.objects.all().delete()

        with requests.get(url, stream=True) as response:
            with open(file_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
                
        with open("cars.xml", 'r', encoding="utf-8") as file:
            data = []    
            root = ET.parse(file)
            cars = root.findall('mark')
            for car in cars:
                mark = car.attrib["name"]
                mark_model = Mark.objects.create(mark_name=mark)
                filter = set()
                for spec in car.findall("folder"):
                    model_name = spec.attrib["name"].split(",")[0]
                    filter.add(model_name)
                for model_n in filter:
                    model = Model(mark=mark_model,model_name=model_n)
                    data.append(model)
            Model.objects.bulk_create(data)
        
        return redirect(to="landing-page")

class MarksListView(ListView):
    template_name = 'base.html'
    paginate_by = 10    
    model = Mark
    context_object_name = "marks_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        context['marks_list'] = paginator.get_page(page)
        return context
    
    
class ModelsDetailedListView(DetailView):
    model = Mark
    template_name = "models.html"
    paginate_by = 10 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        models_list = self.object.all_models.all()

        paginator = Paginator(models_list, self.paginate_by)
        page = self.request.GET.get('page') 
 
        context['models'] = paginator.get_page(page)
        return context