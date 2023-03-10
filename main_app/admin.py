from django.contrib import admin
from .models import Verbiage, Etymology, Fact


admin.site.register(Verbiage)
admin.site.register(Etymology)
admin.site.register(Fact)