from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ReviewForms
from webapp.models import Review, Product
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


class ReviewView(DetailView):
    template_name = 'reviews/review_view.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        context['review'] = review
        return context


class ReviewCreateView(CreateView):
    template_name = 'reviews/review_create.html'
    form_class = ReviewForms

    def form_valid(self, form):
        project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('webapp:products_detail_view', pk=project.pk)


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
