from django.db import models


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'FAQ ID: {self.id}'
