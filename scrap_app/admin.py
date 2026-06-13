from django.contrib import admin
from .models import UserProfile, ScrapMaterial, PickupRequest, ScrapCollection, Transaction, Notification


admin.site.register(UserProfile)
admin.site.register(ScrapMaterial)
admin.site.register(PickupRequest)
admin.site.register(ScrapCollection)
admin.site.register(Transaction)
admin.site.register(Notification)