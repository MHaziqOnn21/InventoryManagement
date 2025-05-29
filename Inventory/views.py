from django.shortcuts import render, get_object_or_404
from .models import Inventory
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def home(request):
    inventory = Inventory.objects.all()
    return render (request, 'inventory/home.html', {'inventory' : inventory})

# View details
@login_required
def inventory_detail(request, pk):
    inventory_details = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'inventory_details' : inventory_details})

# Add new inventory item
class InventoryCreateView (LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Inventory
    template_name = "inventory/inventory_form.html"
    fields = ['name', 'category', 'ser_number', 'tag_number', 'quantity', 'description', 'location', 'd_o_p', 'purchase', 'vendor', 'receipt', 'condition', 'assigned_to', 'intended_usage', 'additional_notes']
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

# Update inventory item
class InventoryUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inventory
    template_name = "inventory/inventory_form.html"
    fields = ['name', 'category', 'ser_number', 'tag_number', 'quantity', 'description', 'location', 'd_o_p', 'purchase', 'vendor', 'receipt', 'condition', 'assigned_to', 'intended_usage', 'additional_notes']
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

# Delete inventory item
class InventoryDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inventory
    template_name = "inventory/inventory_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_staff
    






