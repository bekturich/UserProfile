from django.db import models


class UserProfile(models.Model):
    nickname = models.CharField(max_length=32, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='profiles_images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nickname


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hashtag = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post}'


