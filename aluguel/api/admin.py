from django.contrib import admin
from .models import Item, Tema, Client, Rent


# Register your models here.
admin.site.register(Item)
admin.site.register(Tema)
admin.site.register(Client)
admin.site.register(Rent)