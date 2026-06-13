from django.db import models
from django.contrib.auth.models import User
class Song(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    artist=models.CharField(max_length=100,null=True, blank=True)
    audio_file=models.FileField(upload_to='audios/')
    cover_image=models.ImageField(upload_to='images/')
    lyrics=models.TextField(null=True, blank=True)
    released_by=models.ForeignKey(User, on_delete=models.CASCADE)
    release_date=models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title
class Artist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    stage_name=models.CharField(max_length=200)
    profile_image=models.ImageField(upload_to='artist/',blank=True, null=True)
    bio=models.TextField()
    genre=models.CharField(max_length=200, null=True,blank=True)
    whatsapp_number=models.CharField(max_length=50, blank=True,null=True)
    verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.stage_name
class Booking(models.Model):
    STATUS_CHOICES=(
        ('Pending', 'pending'),('accepted', 'Accepted'),('rejected', 'Rejected'),
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    artist_name=models.CharField(max_length=200)
    customer_name=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=50)
    event_date=models.DateField()
    event_location=models.CharField(max_length=300)
    message=models.TextField()
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.customer_name} - {self.artist_name}"
class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
# Create your models here.
