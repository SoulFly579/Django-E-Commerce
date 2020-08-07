from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Sistem Açık'),
        ('False', 'Sistem Kapalı'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    smtpserver = models.CharField(max_length=20)
    smtpemail = models.CharField(max_length=20)
    smtppassword = models.CharField(max_length=10)
    smtpport = models.CharField(max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    reference = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title