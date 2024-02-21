from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    def __str__(self):
        return f'{self.user.username} Profile'
class medicalRecord (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)  
    image = models.ImageField(upload_to='medical_record')

    def __str__(self):
        return f'{self.user.username} medicalRecord'
class foodDiet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    good_foods = models.TextField()  
    bad_foods = models.TextField()


    def __str__(self):
        return f'{self.user.username} foodDiet'

