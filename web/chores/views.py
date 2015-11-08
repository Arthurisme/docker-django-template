from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import  ChoreList, Chore
from django.template import RequestContext,loader

def index(request):
    # 04-01 simple page
    # return HttpResponse("You are at the ChoreList index.")

    #read all chorelist data to view and show:
    lists = ChoreList.objects.all()
    # template=loader.get_template('chores/index.html')
    # context=RequestContext(request,{
    #     'chorelists':lists
    # })
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(template.render(context))
    context= {  'chorelists':lists }
    return render(request,'chores/index.html',context)

def newlist(request):
    if request.POST:
        list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
        list.save()
        return HttpResponseRedirect('/chores')
        # return HttpResponse("Got it.")
    else:
        return render(request,'chores/newlist.html',{})

def detail(request, chorelist_id):
    # return HttpResponse("You are looking at ChoreList #%s ." % chorelist_id)
    # template=loader.get_template('chores/index.html')
    # context=RequestContext(request,{
    #     'chorelists':lists
    # })
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(template.render(context))
    # context= {  'chorelist':lists }

    list = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request,'chores/detail.html',{'chorelist': list})

# def chores(request, chorelist_id):
#     list = get_object_or_404(ChoreList, pk=chorelist_id)
#     chores=list.chore_set.all()
#     return render(request,'chores/chores.html',{'chorelist': list, 'chores':chores})

def choredetail(request, chorelist_id, chore_id):
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    return render(request,'chores/choredetail.html',{'chorelist': list, 'chore':chore})

def updatechore(request, chorelist_id, chore_id):
    list = get_object_or_404(ChoreList, pk=chorelist_id)

    chore = get_object_or_404(Chore, pk=chore_id)

    if 'complete' in request.POST:
        chore.complete=True
    else:
        chore.complete=False
    chore.save()
    # return render(request,'chores/choredetail.html',{'chorelist': list, 'chore':chore})
    return HttpResponseRedirect('/chores/'+chorelist_id+'/chores/'+chore_id)

