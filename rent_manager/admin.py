from django.contrib import admin
from .models import *

# Register your models here.
class EntityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entity._meta.fields]

class MaintenanceHistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MaintenanceHistory._meta.fields]
    raw_id_fields = ['entity']

class TenantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tenant._meta.fields]
    raw_id_fields = ['tenant', 'entity']

class TenantProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TenantProfile._meta.fields]
    

class TenantPaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TenantPayment._meta.fields]
    raw_id_fields = ['tenant']


admin.site.register(Entity, EntityAdmin)
admin.site.register(MaintenanceHistory, MaintenanceHistoryAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(TenantProfile, TenantProfileAdmin)
admin.site.register(TenantPayment, TenantPaymentAdmin)