from import_export import resources
from .models import Restaurant
from .models import Person
from .models import Review

class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review