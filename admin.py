from django.contrib import admin
from .models import *

admin.site.register(UserSession)
admin.site.register(HallDetails)
admin.site.register(DetailFood)
admin.site.register(CategoryFood)
admin.site.register(HallSlot)
admin.site.register(Booking)
admin.site.register(Contactus)


class Booking(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'input_formats': ('%d/%m/%Y,')},
    }
