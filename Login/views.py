from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, HttpResponse, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from Login.models import Item
from Login.forms import ItemForm, QuantityForm
from django.core.urlresolvers import reverse
# create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    item = Item.objects.filter(is_deleted=False)
    return render(request,"home.html", context= {'name':'sagar', 'item':item})

@login_required(login_url="/login/")
def delete(request, pk):
    query = Item.objects.get(pk=pk)
    query.is_deleted = True
    query.save()
    return HttpResponseRedirect("/list/")

@login_required(login_url="/login/")
def edit_item(request, id=None, template_name='item_edit.html'):
    #raise Exception(id)
    if id:
        item = get_object_or_404(Item, pk=id)
        
        {'charfield1': 'foo', 'charfield2': 'bar'}
    #form = ItemForm(request.POST or None, instance=article)
    form = ItemForm({'price':item.price,'name':item.name, 'weight':item.weight, 'quantity':item.quantity, 'batch_no':item.batch_no})
    if request.POST and form.is_valid():
    	name = request.POST['name']
    	price = request.POST['price']
    	weight = request.POST['weight']
    	batch_no = request.POST['batch_no']
    	quantity = request.POST['quantity']
    	Item.objects.filter(id=id).update(name=name,price=price,weight=weight,batch_no=batch_no,quantity=quantity)
        # Save was successful, so redirect to another page
        item_save_success = 'items'
        redirect_url = reverse(item_save_success)
        return redirect(redirect_url)

    return render(request, template_name, {
        'form': form, 'item':item
    })

@login_required(login_url="/login/")
def add_quantity(request, id=None, template_name='add_quantity.html'):
    if id:
        item = get_object_or_404(Item, pk=id)
        
    #form = ItemForm(request.POST or None, instance=article)
    form = QuantityForm({'quantity':item.quantity})
    if request.POST and form.is_valid():
    	old_quantity = int(item.quantity)
    	new_quantity = int(request.POST['quantity'])
    	Item.objects.filter(id=id).update(quantity=old_quantity + new_quantity)
        # Save was successful, so redirect to another page
        item_save_success = 'items'
        redirect_url = reverse(item_save_success)
        return redirect(redirect_url)

    return render(request, template_name, {
        'form': form, 'item':item
    })

