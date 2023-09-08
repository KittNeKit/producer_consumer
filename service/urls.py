from django.urls import path

from service.views import OrderListView, delete_order

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path(
        "/<int:pk>/delete_order/",
        delete_order,
        name="delete_order",
    ),
]

app_name = "service"
