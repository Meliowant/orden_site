from django.db import models
from django.utils.html import format_html

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('published')
    def __str__(self):
        return self.title
        
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='photo/')
    new = models.ForeignKey(News, related_name='photos', on_delete=models.CASCADE)
	
    def __str__(self):
        return format_html('<a src="{}"/>'.format(self.image.url))

    def image_tag(self):
	    return format_html('<img src="{}" width="100" height="100" />'.format(self.image.url))

    def delete_im(self):
        return format_html('<form method="POST" action="" enctype="multipart/form-data"><input type="submit" class="btn btn-default" value="Видалити"/></form>')