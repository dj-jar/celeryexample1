from django.db import models


class CommonTask(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    result = models.TextField()  # factorial function produces big numbers


class AddTask(CommonTask):
    a = models.IntegerField()
    b = models.IntegerField()
    def __unicode__(self):
        return u'{} + {}'.format(self.a, self.b)


class MulTask(CommonTask):
    a = models.IntegerField()
    b = models.IntegerField()
    def __unicode__(self):
        return u'{} * {}'.format(self.a, self.b)


class FacTask(CommonTask):
    n = models.IntegerField()
    def __unicode__(self):
        return u'{}!'.format(self.n)
