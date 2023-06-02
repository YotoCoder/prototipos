from django.contrib import admin
from datetime import datetime, timedelta
from django.db import models
from .models import Sell


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):

    change_list_template = 'admin/grafics.html'

    def changelist_view(self, request, extra_context=None):

        # amount sum for the last 7 days

        total = Sell.objects.filter(
            created_at__gte=datetime.now() - timedelta(days=7)
        ).aggregate(models.Sum('amount'))['amount__sum']

        extra_context = {
            'total': total,
        }

        return super().changelist_view(request, extra_context=extra_context)
