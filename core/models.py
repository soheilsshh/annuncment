from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField()
    def __str__(self):
        return self.username
    
    
class Catgory(models.Model):
    cat_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cat_name
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='images/' , default='images/defult.png')
    customuser = models.ForeignKey(CustomUser , on_delete=models.CASCADE , )
    catgory = models.ManyToManyField(Catgory)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.ForeignKey('self' , null=True ,blank=True ,on_delete=models.CASCADE ,related_name= 'reply')
    
    def __str__(self):
        return self.comment_text


