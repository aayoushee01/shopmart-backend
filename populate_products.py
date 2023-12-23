import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopmart.settings')
application = get_wsgi_application()

from products.models import Product

json_file_path = 'dummy.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

for product_data in data['products']:
    Product.objects.create(
        id=product_data['id'],
        title=product_data['title'],
        description=product_data['description'],
        price=product_data['price'],
        discountPercentage=product_data['discountPercentage'],
        rating=product_data['rating'],
        stock=product_data['stock'],
        brand=product_data['brand'],
        category=product_data['category'],
        thumbnail=product_data['thumbnail'],
        images=product_data['images'],
    )
