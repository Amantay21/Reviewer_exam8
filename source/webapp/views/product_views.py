from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum, Avg
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SimpleSearchForm, ProductForms
from webapp.models import Product, Review
from webapp.views.review_views import OrderForms


class ProductsView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 5



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.all()
        average_grade = review.aggregate(average_grade=Avg('grade'))['average_grade']
        context['review'] = review
        context['average_grade'] = average_grade
        context['form'] = OrderForms()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/products_create.html'
    form_class = ProductForms

    def get_success_url(self):
        return reverse('webapp:products_detail_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/products_update.html'
    form_class = ProductForms

    def get_success_url(self):
        return reverse('webapp:products_detail_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products_delete.html'
    success_url = reverse_lazy('webapp:index')
