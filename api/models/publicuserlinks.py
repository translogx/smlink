from djongo import models

class PublicUserLinks(models.Model):
    
    url = models.TextField()
    type = models.CharField(max_length=100)
    url_refid = models.CharField(max_length=50)

    #managers
    objects = models.DjongoManager() #default manager


    class Meta:
        abstract = False
    
    def geturlbyid(self, urlid):
        """
        fetch url by url ref id
        """
        
        try:
            query = PublicUserLinks.objects.query = 'db.cars.find({ "url": "'+urlid+'"}'
            urls = PublicUserLinks.objects.from_queryset(query)
            # filter(url= urlid)
        except Exception as e:
            urls = []
            print(e)
        
        

        return urls

    def geturls(self):
        """
        fetch url by url ref id
        """
        
        try:
            urls = PublicUserLinks.objects.all()
            # filter(url= urlid)
        except Exception as e:
            urls = []
            print(e)
        
        

        return urls
