from django.db import models


class Developer(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)

    def is_free(self):
        return self.tasks.count() == 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
