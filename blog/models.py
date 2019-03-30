from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50,null=True)
    content = models.CharField(max_length=200,null=True)
    class Meta:
        managed = False
        db_table = 'blog_info'