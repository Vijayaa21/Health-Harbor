from django.contrib import admin
from .models import UserProfile, medicalRecord, foodDiet, Contact
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(medicalRecord)
admin.site.register(foodDiet)
admin.site.register(Contact)
