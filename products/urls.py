from django.urls import path
from . import views as myviews

urlpatterns = [
    path('add_products/', myviews.add_products, name='add-products-url'),
    path('', myviews.products, name='products-url'),
    path('delete/<id>', myviews.delete, name='delete-url'),
    path('update/<id>',myviews.update_products, name='update-url'),
    path('pay/<id>',myviews.pay, name='pay-url'),

]
