from django.urls import path

from .api_views import (
    CategoryAPIView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    NotebookDetailAPIView,
    CustomerListAPIView)


urlpatterns = [
    path('categories/<str:id>/', CategoryAPIView.as_view(), name='categories_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('customers/', CustomerListAPIView.as_view(), name='customers_list'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebook_list'),
    path('notebooks/<str:id>/', NotebookDetailAPIView.as_view(), name='notebook_detail')
]