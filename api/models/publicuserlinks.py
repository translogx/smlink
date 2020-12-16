from djongo import models

class PublicUserLinks(models.Model):
    url = models.TextField()
    type = models.CharField(max_length=100)
    request_time = models.DateField()

    class Meta:
        abstract = True