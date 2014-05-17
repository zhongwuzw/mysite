from django.test import TestCase
from books.models import Author

c = Author.objects.create('a','b','zwhs@so.com')
c.save()
