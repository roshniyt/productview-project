from django.contrib import admin

# Register your models here.
from .models import HeroSection
admin.site.register(HeroSection)

from .models import SampleResult
admin.site.register(SampleResult)