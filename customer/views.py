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

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            kayak_variant = KayakVariant.objects.get(pk__contains=int(item))
            item_data = {
                'id': kayak_variant.pk,
                'name': kayak_variant.name,
                'price': kayak_variant.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

            for item in order_items['items']:
                price += item['price']
                item.ids.append(item['id'])

            order = OrderModel.objects.create(price=price)
            order.items.add(*item_id)

            context = {
                'items': order_items['items'],
                'price': price
            }

            return render(request, 'customer/order_confirmation.html', context)

