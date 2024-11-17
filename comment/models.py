from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from product.models import Product


class CommentManager(models.Manager):
    def published_comments(self):
        return self.filter(status=_("published"))

class Comment(models.Model):
    STATUS_CHOICES = [
        ("draft", _("draft")),
        ("published", _("published")),
    ]
    
    user = models.ForeignKey(get_user_model(), verbose_name=_('user'), related_name = 'comments', on_delete=models.CASCADE)
    
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name = 'comments', on_delete=models.CASCADE)
    
    content = models.TextField(_('content'))
    
    rate = models.PositiveIntegerField(_('rate'), default=1)
    
    datetime_create = models.DateTimeField(_('datetime_create'), auto_now_add=True)
    
    reply = models.ForeignKey(("self"), verbose_name=_('reply'), related_name = 'comment_replies', on_delete=models.CASCADE, blank=True, null=True)
    
    is_reply = models.BooleanField(_('is_reply'), default=False)
    
    status = models.CharField(_('status'), max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0])
    
    objects = CommentManager()

    def __str__(self):
        return f" comment_id :{self.id}"
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
