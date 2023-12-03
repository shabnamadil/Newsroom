from django.db import models
from .utils.validators import validate_email


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Contact(Base):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[validate_email])
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f'Message by {self.email}'
    

class WebsiteInformation(Base):
    website_name = models.CharField(max_length=255, null=True, blank=True)
    website_logo=models.FileField(upload_to='website/')
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(validators=[validate_email])
    tel_number = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link=models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    youtube_link=models.URLField(null=True, blank=True)

    def save(self):
        self.pk = 1
        return super().save() 

    def __str__(self) -> str:
        return f'All static information about {self.website_name}'