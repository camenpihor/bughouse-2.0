from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class Post(models.Model):
    author = models.TextField()
    title = models.TextField()
    created_at_utc = models.DateField(auto_now_add=True)
    content_warngins = ArrayField(models.TextField())
    url = models.TextField()
    html = models.TextField()
    num_views = models.TextField()

    class Meta:
        db_table = "post"
