from django.shortcuts import render
from django.views import View
from Store.models.product import Products

class Cart(View):
    def get(self, request):
        # Get the cart dictionary from the session
        cart = request.session.get('cart', {})

        # Extract product IDs from the cart
        ids = list(cart.keys())

        # Convert IDs to integers (assuming your product IDs are integers)
        ids = [int(id) for id in ids]

        # Fetch products based on IDs
        products = Products.get_products_by_id(ids)
        print(products)

        return render(request, 'cart.html', {'products': products})
