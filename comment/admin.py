from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Comment


class CommentRateFilter(admin.SimpleListFilter):
    """
        We use this class to make our custom filter about comment rate.
    """
    title = _('Comment Rate Filter')
    parameter_name = "rate"
    
    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ("1", _("worst")),
            ("2", _("bad")),
            ("3", _("normal")),
            ("4", _("good")),
            ("5", _("well")),
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "1":
            return queryset.filter(rate = 1)
        if self.value() == "2":
            return queryset.filter(rate = 2)
        if self.value() == "3":
            return queryset.filter(rate = 3)
        if self.value() == "4":
            return queryset.filter(rate = 4)
        if self.value() == "5":
            return queryset.filter(rate = 5)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
        We make this class to show our Comment model in admin panel.  
    """
    list_display = ['id', 'user', 'product', 'rate', 'is_reply', 'status', 'reply_count_column']

    search_fields = ['user__icontains', 'product__icontains', 'content__icontains']
    
    list_editable = ['status', ]
    
    list_per_page = 10
    
    list_select_related = ['user', 'product']
    
    list_filter = ['status', 'is_reply', 'datetime_create', CommentRateFilter, ]
    
    autocomplete_fields = ['user', 'product']
    
    
    def get_queryset(self, request):
        """
            We overwrite the default queryset to add prefetch_related and make a new column in Comment model.
        """
        queryset = super(CommentAdmin, self).get_queryset(request)
        return queryset.prefetch_related("comment_replies").annotate(replies_count = Count("comment_replies"))
    
    
    def lookup_allowed(self, key, value):
        """
            We must override this method to use reply as filter for show the comment_replies by using reply_count_column method.
        """
        if key in ('reply'):
            return True
        return super(CommentAdmin, self).lookup_allowed(key, value)
    
    
    @admin.display(ordering="replies_count", description=_("# replies"))
    def reply_count_column(self, comment=Comment):
        """
            We use this method to get the number of comment`s replies in the changelist.
        """
        url = (
            reverse("admin:comment_comment_changelist")
            + "?"
            + urlencode({
                "reply" : comment.id,
            })
        )
        return format_html('<a href="{}" >{}</a>', url, comment.replies_count)

