from django.contrib import admin
from EcomApp.models import Setting, ContactMessage, FAQ
# Register your models here.
admin.site.register(Setting)

admin.site.register(ContactMessage)

admin.site.index_title = 'ECOMMERCE WEBSITE FOR ELECTRONICS'

class FAQamin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'created_at', 'updated_at']


# admin.site.register(FAQ, FAQamin)
