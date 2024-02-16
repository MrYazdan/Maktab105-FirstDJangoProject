from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import MusicModel, CategoryModel, AlbumModel


class AddMusicView(CreateView):
    """
    This view allows users to add new music entries.
    """
    model = MusicModel
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'Musics/add.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"


class InfoMusicView(ListView):
    """
    This view displays information about existing music entries.
    """
    model = MusicModel
    template_name = 'Musics/info.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"


class DeleteMusicByNameView(DeleteView):
    """
    This view allows users to delete music entries by their name.
    """
    model = MusicModel
    success_url = reverse_lazy('info')
    template_name = 'Musics/delete.html'

    def get(self, request, *args, **kwargs):
        """
        Get the name of the music entry from URL parameters,
        delete the corresponding music entry, and redirect to
        the success URL.
        """
        name = self.kwargs.get('pk')
        music = get_object_or_404(MusicModel, name=name)
        music.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect(self.success_url)


class DeleteMusicByIDView(DeleteView):
    """
    This view allows users to delete music entries by their ID.
    """
    model = MusicModel
    success_url = reverse_lazy('info')
    template_name = 'Musics/delete.html'

    def get(self, request, *args, **kwargs):
        """
        Get the ID of the music entry from URL parameters,
        delete the corresponding music entry, and redirect to
        the success URL.
        """
        self.object = self.get_object()  # noqa
        self.object.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        """
        Retrieve the music entry object by its ID.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)


class CountMusicView(TemplateView):
    """
    This view displays counts of albums, categories, and music entries.
    """
    template_name = 'Musics/count.html'

    def get_context_data(self, **kwargs):
        """
        Add counts of albums, categories, and music entries to the context.
        """
        context = super().get_context_data(**kwargs)
        album_count = AlbumModel.objects.count()
        category_count = CategoryModel.objects.count()
        music_count = MusicModel.objects.count()

        context['album_count'] = album_count
        context['category_count'] = category_count
        context['music_count'] = music_count

        return context
