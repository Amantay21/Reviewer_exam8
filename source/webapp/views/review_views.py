from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ReviewForms
from webapp.models import Review, Product
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView


# class IndexView(View):
#
#     def get(self, request, *args, **kwargs):
#         tasks = Task.objects.all()
#         context = {
#             'tasks': tasks
#         }
#         return render(request, 'index.html', context)


class ReviewView(TemplateView):
    template_name = 'tasks/tasks_view.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Review, pk=kwargs.get('pk'))
        context['task'] = task
        return context


class TaskCreateView(CreateView):
    template_name = 'tasks/tasks_create.html'
    form_class = ReviewForms

    def form_valid(self, form):
        project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('webapp:projects_detail_view', pk=project.pk)


class TaskUpdateView(UpdateView):
    template_name = 'tasks/task_update.html'
    model = Review
    form_class = ReviewForms

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Review

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.project.pk})
