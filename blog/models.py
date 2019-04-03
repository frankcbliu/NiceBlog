from django.db import models

class BlogInfo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    imgurl = models.CharField(db_column='imgUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)
    viewnum = models.IntegerField(db_column='viewNum', blank=True, null=True)  # Field name made lowercase.
    commentnum = models.IntegerField(db_column='commentNum', blank=True, null=True)  # Field name made lowercase.
    likenum = models.IntegerField(db_column='likeNum', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=50, blank=True, null=True)
    classid = models.IntegerField(db_column='classId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blog_info'

