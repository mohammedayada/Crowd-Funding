from django.db import models

from category.models import Category
from django.conf import settings
# Create your models here.
#projects (id (pk), title, details, target, currnt_donation, start_date, end_date, avg_rate, categ_id (fk)
# , user_id (fk) )
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField()
    target = models.FloatField(default=0)
    current_donation = models.FloatField(default=0)
    start_date = models.DateField(auto_now=False, auto_now_add=False,)
    end_date = models.DateField(auto_now=False, auto_now_add=False,)
    avg_rate = models.FloatField(default=0)


    def __str__(self):
        return "user name: "+self.user.username+" "+self.title+" category: "+self.category.name


class Project_imgs(models.Model):
    project = models.ForeignKey(Project,
                                 on_delete=models.CASCADE)
    img = models.ImageField()