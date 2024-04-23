from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F, ExpressionWrapper, DecimalField
from store.models import Product, Collection, Customer, Order, OrderItem
from tags.models import TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.db import connection

def say_hello(request): 
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1,2,'a'])

    return render(request, 'hello.html', {'name': 'Mosh'})
  