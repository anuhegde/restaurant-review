from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Restaurant
from .models import Person, Review


@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    pass