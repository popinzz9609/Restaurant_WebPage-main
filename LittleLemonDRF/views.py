from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class RatingsView(View):

    def get(self, request):
        return HttpResponse("HiHi, Welcome!!")


from restaurant.models import Menu
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def menu_item(request):
    if request.method == 'GET':
        items = Menu.objects.all().values()
        return JsonResponse({'menu': list(items)})
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        item_description = request.POST.get('menu_item_description')

        menu = Menu(
            name=name,
            price=price,
            menu_item_description=item_description,
        )
        try:
            menu.save()
        except IntegrityError:
            return JsonResponse(
                {
                    'error': 'true',
                    'message': 'required field missing'
                },
                status=400)

    return JsonResponse(model_to_dict(menu), status=201)
