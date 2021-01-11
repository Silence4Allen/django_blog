from django.db import models


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()  # 摘要
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    # admin界面显示每个article的title
    def __str__(self):
        return self.title
