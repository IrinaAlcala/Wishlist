from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'


# class ItemDelete(DeleteView):
#    model = Item
#    success_url = '/'

def delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/')
  

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', { 'items': items })

def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'items/detail.html', { 'item': item })