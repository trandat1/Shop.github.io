from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from store.models.products.categories import category


class page_customer():
    def index(request):
        cat = category.get_all_categories()
        cus = request.session.get('Username')
        cart = request.session.get('cart')
        if not cart:
            cart = []
            request.session['cart'] = []
        if cus:
            template = loader.get_template('customer/customer.html')
            context = {
                'user': cus,
                'cat': cat,
                'count': len(cart)
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('index'))

    def logout(request):
        request.session['Username'] = None
        request.session['customer_id'] = None
        request.session['cart']=[]
        return HttpResponseRedirect(reverse('customer'))
