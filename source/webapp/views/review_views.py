from django.db.models import F, Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ReviewForms
from webapp.models import Review, Product
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


class OrderForms:
    pass


class ReviewView(DetailView):
    template_name = 'reviews/review_view.html'
    model = Review




class ReviewCreateView(CreateView):
    template_name = 'reviews/review_create.html'
    form_class = ReviewForms

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.project = product
        review.save()
        form.save_m2m()
        return redirect('webapp:products_detail_view', pk=product.pk)


class ReviewUpdateView(UpdateView):
    template_name = 'reviews/review_update.html'
    model = Review
    form_class = ReviewForms

    def get_success_url(self):
        return reverse('webapp:products_detail_view', kwargs={'pk': self.object.project.pk})


class ReviewDeleteView(DeleteView):
    template_name = 'reviews/review_delete.html'
    model = Review

    def get_success_url(self):
        return reverse('webapp:products_detail_view', kwargs={'pk': self.object.project.pk})
