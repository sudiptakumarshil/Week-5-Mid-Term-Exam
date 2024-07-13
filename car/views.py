from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from car.models import Car


# Create your views here.
class LoadCarView(View):
    def get(self, request, *args, **kwargs):
        brand_id = request.GET.get('brand_id')
        if not brand_id:
            return JsonResponse({'error': 'Missing brand_id parameter'}, status=400)

        cars = Car.objects.filter(brand_id=brand_id).values()
        return JsonResponse(list(cars), safe=False)
