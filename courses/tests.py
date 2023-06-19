from django.test import TestCase

# Create your tests here.
from .models  import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name='programming')
        Category.objects.create(category_name='marketing')

    def test_categories_registered_correctly(self):
        programming = Category.objects.get(category_name='programming')
        marketing = Category.objects.get(category_name='marketing')
        self.assertEqual(programming, 'programming')
        self.assertEqual(marketing, 'marketing')