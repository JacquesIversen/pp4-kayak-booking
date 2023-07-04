from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        pass
        # get items from duration
        halfdays = KayakVariant.objects.fitler(duration__name__contains='HalfDay')
        fulldays = KayakVariant.objects.fitler(duration__name__contains='FullDay')

        # pass into context
        context = {
            'halfdays': halfdays,
            'fulldays': fulldays,
        }

        # render
        return render(request, 'customer/order.html', context)