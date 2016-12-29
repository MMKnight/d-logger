from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from .models import Entry
# Create your tests here.
def create_entry(title,content,tags):
    return Entry.objects.create(title=title,content=content,tags=tags)
class EntryModelTest(TestCase):
    def test_tags_validation(self):
        #Tags must be <= 5
        entry = create_entry("This is entr","Too many entruesfgfsfsg",
        ['dog','sans','sdad','dksow[fk]','dfdf','dfwf',',sfwf'])
        self.assertRaises(ValidationError,entry.clean())
