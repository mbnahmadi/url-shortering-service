from django.db import models
from django.utils.translation import gettext_lazy as _
import string
import random

# Create your models here.


class ShortUrlModel(models.Model):
    url = models.URLField(verbose_name=_('url'), max_length=2000)
    shortcode = models.CharField(verbose_name=_('Short Code'), max_length=8, unique=True, blank=True)
    access_count = models.IntegerField(verbose_name=_('Access Count'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_shortcode(self, length=6):
        '''
        generate random uniq short code with specific length
        '''
        characters = string.ascii_letters + string.digits  #character and digits (a-z, A-Z) , (0-9)
        while True:
            shortcode = ''.join(random.choice(characters) for _ in range(length))
            if not ShortUrlModel.objects.filter(shortcode=shortcode).exists(): # check return uniq code
                return shortcode

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = self.generate_shortcode()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.shortcode}'

    class Meta:
        verbose_name = _('Short URL')    
        verbose_name_plural = _('Short URLs')    
