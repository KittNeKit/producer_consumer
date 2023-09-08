from django.urls import path

from service.views import OrderListView, DeleteOrderView

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path(
        "<int:pk>/delete_order/",
        DeleteOrderView.as_view(),
        name="delete_order",
    ),
]

app_name = "service"
