from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ResourceForm
from .models import Category, Resource


def resource_list(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    resources = Resource.objects.select_related('category', 'created_by').all()

    if query:
        resources = resources.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if category_slug:
        resources = resources.filter(category__slug=category_slug)

    categories = Category.objects.all()

    context = {
        'resources': resources,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'resources/resource_list.html', context)


def resource_detail(request, pk):
    resource = get_object_or_404(Resource.objects.select_related('category', 'created_by'), pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})


@login_required
def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm()
    return render(request, 'resources/resource_form.html', {'form': form, 'title': 'Upload Resource'})


@login_required
def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if resource.created_by != request.user:
        return HttpResponseForbidden('You can only edit your own resources.')

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm(instance=resource)

    return render(request, 'resources/resource_form.html', {'form': form, 'title': 'Edit Resource'})


@login_required
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if resource.created_by != request.user:
        return HttpResponseForbidden('You can only delete your own resources.')

    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')

    return render(request, 'resources/resource_confirm_delete.html', {'resource': resource})
