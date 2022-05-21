from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(Studentmodel)
admin.site.register(Addcourse)
admin.site.register(Payfee)