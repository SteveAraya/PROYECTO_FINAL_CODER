from django.shortcuts import render, redirect

from .models import Post

from .forms import PostForm
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.core.paginator import Paginator
# Create your views here.

def PostCreate(request):
    print('method:',request.method)
    if(request.method=="POST"):
        postformulario = PostForm(request.POST, request.FILES)
        print(postformulario)
        if(postformulario.is_valid()):
            print("es valido")
            data=postformulario.cleaned_data
            post = Post(
                titulo=data["titulo"],
                sub_titulo=data["sub_titulo"],
                cuerpo=data["cuerpo"],
                fecha=data["fecha"],
                imagen=data["imagen"],
                # categoria=data["categoria"]
            )
            post.save()
            messages.success(request, 'El post fue creado con éxito!')
            return redirect('/blog/create')
    else:
        postformulario=PostForm()
    return render(request, "PostCreate.html", {"postformulario":postformulario})

def PostTable(request):
    posts     = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "PostTable.html", contexto )

class PostDelete(DeleteView):
    model         = Post
    template_name = "PostDelete.html"
    success_url   = "/blog/table"

class PostUpdate(UpdateView):
    model         = Post
    template_name = "PostEdit.html"
    fields        = "__all__"
    success_url   = "/blog/table"

def PostList(request):

    listado_posts  = Post.objects.all()
    paginator     = Paginator(listado_posts,3)
    pagina        = request.GET.get("page") or 1
    posts          = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas       = range(1, posts.paginator.num_pages + 1)
    contexto      = {"posts": posts, "paginas":paginas, "pagina_actual":pagina_actual}

    return render(request, "PostList.html", contexto )

def PostDetail(request, id):
    posts     = Post.objects.filter(id=id)
    contexto = {"posts": posts}
    return render(request, "PostDetail.html", contexto)