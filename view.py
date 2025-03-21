from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy # type: ignore
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['titre', 'contenu', 'image']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'image']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
