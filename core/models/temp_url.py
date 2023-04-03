from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

class TempURL(models.Model):
    path = models.CharField(max_length=400)
    slug = models.UUIDField(default=uuid.uuid4, unique=True)

    valid = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def is_valid(self):
        if (timezone.now() - self.created_at).total_seconds() < 300 and self.valid:
            return True
        else:
            return False

    def get_absolute_url(self):
        return f"{settings.BASE_URL}download/{self.slug}/"