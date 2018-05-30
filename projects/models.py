from django.db import models

class ParserPhoto(models.Model):
    user = models.CharField(max_length=50)
    url = models.CharField(max_length=250)
    photos = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Photo in %s' % self.user