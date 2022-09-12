from django.shortcuts import render,get_object_or_404
from .models import worker, departament, news, product
from django.views import generic
from django.views.generic import DetailView

def index(request):
    news1 = news.objects.all()
    return render(request, "index.html", {"news": news1})

def newsDetailview(request, id):
    news1 = get_object_or_404(news, id=id)  # 2-ой способ
    return render(request, "news_detail.html", {"news": news1})

class workersList(generic.ListView):
    model = worker


def ProductList(request):
    Poezd = product.objects.all()
    return render(request,'Product_list.html', {'poezd': Poezd})

