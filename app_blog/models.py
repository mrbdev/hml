from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_cod = models.CharField(max_length=5, unique=True)
    cat_name = models.CharField(max_length=50, unique=True)
    cat_parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, db_column='cat_parent_id')
    # created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return (self.cat_cod + '-' + self.cat_name)
