from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from cart.cart import get_cart_len


class ListObjectsMixin:
    model = None
    template_name = None
    template_include = None
    number_per_page = settings.NUMBER_PER_PAGE

    def get(self, request):
        objects = self.model.objects.all().order_by('-created_at')

        query_search = request.GET.get('search', '')
        objects = objects.filter(
            Q(title__icontains=query_search) | Q(body__icontains=query_search)
        )

        paginator = Paginator(objects, self.number_per_page)
        page = int(request.GET.get('page', 1))

        if page > 1:
            return render(
                request,
                self.template_include,
                context={
                    'objects': paginator.get_page(page)
                }
            )

        return render(
            request,
            self.template_name,
            context={
                'objects': paginator.get_page(page),
                'pages': paginator.num_pages,
                'cart_len': get_cart_len(request)
            }
        )
