from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Draft(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Under Review', 'Under Review'),
        ('Revision', 'Revision'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),)

    KB_CHOICES = (
        ('SNP', 'SNP'),
        ('Expression', 'Expression'),)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    kb = models.CharField(max_length=20, choices=KB_CHOICES)
    title = models.CharField(max_length=500)
    content = JSONField()
    paper = models.FileField(upload_to='uploads/%Y/%m%d/', null=True, blank=True)

    def __str__(self):
        return "{!s} | {} | {} | {}".format(self.user, self.status, self.kb, self.title)