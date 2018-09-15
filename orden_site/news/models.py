from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('published')
    def __str__(self):
        return self.title
        
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='photos')
    new = models.ForeignKey(News, related_name='photos', on_delete=models.CASCADE)