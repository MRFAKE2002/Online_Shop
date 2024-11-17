from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class CategoryManager(models.Manager):
    def available_categories(self):
        return self.prefetch_related("products").select_related('parent').filter(available=True, has_parent=False)


class Category(models.Model):
    name = models.CharField(_("name"), max_length=255, unique=True, )
    
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    
    datetime_create = models.DateTimeField(_("datetime_create"), auto_now_add=True)
    
    parent = models.ForeignKey("self", verbose_name = _("parent"), related_name ="parent_category", blank=True, null=True, on_delete=models.CASCADE)
    
    has_parent = models.BooleanField(_("has_parent"), default=False,)
    
    available = models.BooleanField(_("available"), default=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category:category_list", kwargs={"slug": self.slug})
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

