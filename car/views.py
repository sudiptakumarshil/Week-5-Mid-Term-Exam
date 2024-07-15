from django.views import View
from django.http import JsonResponse
from car.models import Car, Comment, Invoice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
class LoadCarView(View):
    def get(self, request, *args, **kwargs):
        brand_id = request.GET.get('brand_id')
        if not brand_id:
            return JsonResponse({'error': 'Missing brand_id parameter'}, status=400)

        cars = Car.objects.filter(brand_id=brand_id).values()
        return JsonResponse(list(cars), safe=False)


class BuyNowView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            car = Car.objects.get(id=request.POST.get('car_id'))
            if car.quantity > 0:
                invoice = Invoice(car=car, quantity=1, user=request.user)
                invoice.save()
                car.quantity -= 1
                car.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Car out of stock'})
        except Car.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Car not found'})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('home')
    login_url = 'user.login'

    def form_valid(self, form):
        car_id = self.kwargs.get('car_id')
        car = get_object_or_404(Car, id=car_id)
        form.instance.car = car
        messages.success(self.request, 'Commented Successfully!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_id = self.kwargs.get('car_id')
        context['car'] = get_object_or_404(Car, id=car_id)
        context['comments'] = Comment.objects.filter(car_id=car_id)
        return context

    def get_success_url(self):
        return self.request.path
