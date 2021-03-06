from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    # fetures

    feture_1 = models.CharField(max_length=100)
    feture_2 = models.CharField(max_length=100)
    feture_3 = models.CharField(max_length=100)
    feture_4 = models.CharField(max_length=100)
    feture_5 = models.CharField(max_length=100)

    # free trial

    is_free_trial = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title

    
    def get_plan_total(self):
        return dev([price for p in self.price.all()])  


class PhoneThumbnail(models.Model):
    title = models.CharField(max_length=100)
    phone_image = models.ImageField(upload_to='home_inamge_th')
    
    def __str__(self):
        return self.title

class DesktopThumbnail(models.Model):
    title = models.CharField(max_length=100)
    desktop_image = models.ImageField(upload_to='home_desktop_th')

    def __str__(self):
        return self.title

class Logo(models.Model):
    favor_icon = models.ImageField(upload_to = 'favor icon', blank=True)
    # logo used in home temlate
    home_ligth = models.ImageField(upload_to = 'home_ligth logo', blank=True) 
    # logo used in dashboard template
    dashboard_ligth = models.ImageField(upload_to = 'dashboard_ligth logo', blank=True) 
    # logo used in home temlate
    home_dark = models.ImageField(upload_to = 'home_dark logo', blank=True) 
    # logo used in dashboard template
    dashboard_dark = models.ImageField(upload_to = 'dashboard_dark', blank=True)

          
