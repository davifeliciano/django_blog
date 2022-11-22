from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        return self.user.username

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None:
        super().save()
        image = Image.open(self.image.path)
        if image.height > 500 or image.width > 500:
            output_size = (500, 500)
            image.thumbnail(output_size)
            image.save(self.image.path)
