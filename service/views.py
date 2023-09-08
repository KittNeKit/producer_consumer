from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from service.models import Order
from service.notification import send_delete_order_text


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    queryset = Order.objects.all().select_related("employee")

    def get_queryset(self):
        return self.queryset.filter(employee=self.request.user)


class DeleteOrderView(View):
    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        send_delete_order_text(order, request.user)
        order.delete()
        return HttpResponseRedirect(reverse_lazy("service:order_list"))
