from django.urls import path
from .views import *

urlpatterns = [
    path('load-car-by-brand', LoadCarView.as_view(), name='car.by_brand'),
    path('buy-now', BuyNowView.as_view(), name='car.buy_now'),
    path('<int:car_id>/leave-comment/', CommentCreateView.as_view(), name='car.leave_comment')
]
