from django.contrib import admin

from users.models import DeliveryAddress


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'city']
    prepopulated_fields = {'slug': ['user', ]}


