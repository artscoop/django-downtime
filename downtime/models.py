from django.db import models
from downtime.managers import PeriodManager
from django.utils.translation import ugettext, ugettext_lazy as _


class Period(models.Model):
    start_time = models.DateTimeField(blank=True, null=True, verbose_name=_(u"Start"))
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=_(u"End"))
    enabled = models.BooleanField(default=True, verbose_name=_(u"Enabled"))

    objects = PeriodManager()

    def __unicode__(self):
        return ugettext(u"scheduled downtime")
    
    class Meta:
        verbose_name = _(u"scheduled downtime")
        verbose_name_plural = _(u"scheduled downtimes")
