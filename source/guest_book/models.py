from django.db import models


# Create your models here.
class Book(models.Model):
    ACTIVE = 'Active'
    BLOCKED = 'Blocked'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked'),
    )
    author = models.CharField(max_length=40, null=False, blank=False, default='Author', verbose_name='Author')
    email = models.EmailField(max_length=40, null=True, blank=True, default='john_doe@mail.com', verbose_name='john_doe@mail.com')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Text')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Crated at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def get_status_color(self):
        status_colors = {
            'Active': 'green',
            'Blocked': 'red',
        }
        return status_colors.get(self.status, 'gray')

    def __str__(self):
        return "{}. {}".format(self.pk, self.text)

