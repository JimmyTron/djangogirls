from django.db import models

from tinymce import models as tinymce_models


class Company(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    logo = models.ImageField()

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    summary = models.TextField(max_length=300)
    description = tinymce_models.HTMLField()
    open = models.BooleanField(default=True)
    remuneration = models.CharField(max_length=50, blank=True, null=True)
    apply = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company} - {self.role}'
