from django.contrib import admin
from .models import UserProfile
from .models import medicalRecord
from .models import foodDiet
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(medicalRecord)
admin.site.register(foodDiet)
