from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Post

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"pages/home.html",context={},status=200)


def posts_detail_view(request,posts_id,*args,**kwargs):
    data={
       "id":posts_id,
       
    }
    status=200

    try:
        obj=Post.objects.get(id=posts_id)
        data['content']=obj.content
    except:
        data['message']="Not found"
        status=404

        

    
    return JsonResponse(data,status=status)