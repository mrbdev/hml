from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings     # pour le model users déjà existant par défaut


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.tag_name


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_cod = models.CharField(max_length=5, unique=True)
    cat_name = models.CharField(max_length=50, unique=True)
    cat_parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, db_column='cat_parent_id')
    cat_desc = models.TextField(default='')
    cat_flg_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return (self.cat_cod + '-' + self.cat_name)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200, unique=True, verbose_name='title')
    post_slug = models.SlugField(max_length=200, unique=True)
    cat_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, db_column='cat_id')
    post_author_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, db_column='post_author_id', related_name='blog_posts_created')
    post_content = models.TextField()
    tags = models.ManyToManyField(Tag)
    post_status = models.IntegerField(choices=STATUS, default=0) # 1=publish et 0=draft
    post_dt_creation = models.DateTimeField(default=timezone.now)
    post_dt_last_publication = models.DateTimeField(null=True, blank=True,)
    post_usr_last_publication = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, db_column='post_usr_creation_id', related_name='blog_posts_published')
    post_dt_lastupd = models.DateTimeField(default=timezone.now)
    post_usr_lastupd = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, db_column='post_usr_lastupd_id', related_name='blog_posts_updated')
    post_flg_active = models.BooleanField(default=True)

    def Publish(self):
        self.post_dt_last_publication = timezone.now()
        self.save()

    class Meta:
        ordering = ['-post_dt_creation'] # tri par ordre decroissant (le tiret au début) sur la date de creation

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_content = models.TextField()
    post_id = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, db_column='post_id')
    usr_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, db_column='usr_id', related_name='blog_comments_created')
    com_status = models.BooleanField(default=True) # 1=visible et 0=not visible
    com_dt_creation = models.DateTimeField(default=timezone.now)
    com_dt_lastupd = models.DateTimeField(default=timezone.now)
    com_usr_lastupd = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, db_column='com_usr_lastupd_id', related_name='blog_comments_updated')
    com_flg_active = models.BooleanField(default=True)

    def __str__(self):
        return self.com_content

