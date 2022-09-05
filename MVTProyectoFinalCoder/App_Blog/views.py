from django.shortcuts      import render, redirect
from .models               import Post
from django.db.models      import Q
from .forms                import PostForm
from django.contrib        import messages
from django.views.generic  import DeleteView, UpdateView
from django.core.paginator import Paginator
from App_Register.models   import Avatar

from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

# @method_decorator(login_required, name='dispatch')
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
                categoria=data["categoria"]
            )
            post.save()
            messages.success(request, 'El post fue creado con éxito!')
            return redirect('/blog/create')
    else:
        postformulario=PostForm()

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "PostCreate.html", {"postformulario": postformulario, "url":avatar.avatar.url})
    except:
        return render(request, "PostCreate.html")

# @method_decorator(login_required, name='dispatch')
def PostTable(request):
    posts     = Post.objects.all()
    contexto = {"posts": posts}

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "PostTable.html", {"posts": posts, "url":avatar.avatar.url})
    except:
        return render(request, "PostTable.html", contexto)

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):

    model         = Post
    template_name = "PostDelete.html"
    success_url   = "/blog/table"

@method_decorator(login_required, name='dispatch')
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

def Categoria(request, categoria):
    listado_posts = Post.objects.filter(categoria=categoria)
    paginator     = Paginator(listado_posts,3)
    pagina        = request.GET.get("page") or 1
    posts          = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas       = range(1, posts.paginator.num_pages + 1)
    contexto      = {"posts": posts, "paginas":paginas, "pagina_actual":pagina_actual}

    return render(request, "PostList.html", contexto)

def PostDetail(request, id):
    posts     = Post.objects.filter(id=id)
    contexto = {"posts": posts}
    return render(request, "PostDetail.html", contexto)