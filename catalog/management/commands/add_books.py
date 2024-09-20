from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Все категории и продукты были удалены.'))

        category, _ = Category.objects.get_or_create(category_name='a vacuum cleaner', category_description='home appliances')

        products = [
            {'product_name': 'Deerma Vacuum Cleaner', 'product_description': 'DEM-DX1100W White', 'category': category},
            {'product_name': 'Starwind', 'product_description': 'SCM4410', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.product_name}'))
