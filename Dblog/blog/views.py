from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from Dblog.blog.models import Blog, User, Tag
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    articles = Blog.objects.all()
    paginator = Paginator(articles,1)
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render_to_response('index.html',
                  locals(),
                  context_instance=RequestContext(request))

def content(request):   
    articleid = request.GET.get('id')
    article = Blog.objects.get(id = articleid)
    tags = Tag.objects.filter(blog = article)
    return render_to_response('content.html',
                  locals(),
                  context_instance=RequestContext(request))


def archieve(request):
    try:
        articles = Blog.objects.all()
    except Blog.DoesNotExist :
        raise Http404
    return render_to_response('archieve.html',
                  locals(),
                  context_instance=RequestContext(request))

def searchtag(request):
    tagid = request.GET.get('id')
    seartag = Tag.objects.filter(id = tagid)
    articles = Blog.objects.filter(tag = seartag)
    return render_to_response('archieve.html',
                  locals(),
                  context_instance=RequestContext(request))

def blog_search(request):
    if 'keyword' in request.GET:
      s = request.GET['keyword']
      if  not s:
          return render_to_response('index.html',
                        locals(),
                        context_instance=RequestContext(request))
      else:
          articles = Blog.objects.filter(title__icontains = s)
          return render_to_response('archieve.html',
                            locals(),
                            context_instance=RequestContext(request))
    return redirect('/')

def recent_comment(request):
    return render_to_response('recentcomment.html',
                              locals(),
                              context_instance=RequestContext(request))

def category(request):
    tags = Tag.objects.all()
    # nums = []
    # for searchtag in tags:
    #     articles = Blog.objects.filter(tag = searchtag)
    #     num = len(articles)
    #     nums.append(num)
    return render_to_response('category.html',
                              locals(),
                              context_instance=RequestContext(request))


def portfolio(request):
    return render_to_response('porfolio.html',
                              locals(),
                              context_instance=RequestContext(request))