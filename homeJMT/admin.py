from django.contrib import admin

from .models import carousel , product, contacts, data,about,cards
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(carousel)
admin.site.register(product)
admin.site.register(contacts)
admin.site.register(about)
admin.site.register(cards)

@admin.register(data)

class DataAdmin(ImportExportModelAdmin):
    pass
