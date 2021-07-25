from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('Haryana', 'Haryana'),
    ('Punjab', 'Punjab'),
    ('Chandigarh', 'Chandigarh'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Bihar', 'Bihar'),
    ('Rajasthan', 'Rajasthan'),

)


class Resume(models.Model):
    name = models.CharField(max_length=100)  # TextInput
    dob = models.DateField(auto_now=False, auto_now_add=False) # DateInput
    gender = models.CharField(max_length=50) #
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_img', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
