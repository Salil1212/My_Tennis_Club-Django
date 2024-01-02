
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q
def members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))


def details(request,slug):
    mymember=Member.objects.get(slug=slug)
    template=loader.get_template('details.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))


def main(request):
    template=loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    # mymembers=Member.objects.values()
    # mymembers=Member.objects.values_list("firstname")
    # mydata=Member.objects.filter(firstname='Salil').values()
    # mydata=Member.objects.filter(firstname='Salil').values_list('firstname')
    # mydata=Member.objects.filter(firstname='Safal').values()|Member.objects.filter(lastname="nigam").values()
    # mydata=Member.objects.filter(Q(firstname='Safal')|Q(lastname="nigam")).values()
    # mydata=Member.objects.filter(firstname__startswith='S').values()
    # mydata=Member.objects.all().order_by('firstname').values()
    # mydata=Member.objects.all().order_by('-firstname').values()
    mydata=Member.objects.all().order_by('-id','firstname').values()





    template=loader.get_template('template.html')
    context={
       
        'mymembers':mydata,
     

    }
    return HttpResponse(template.render(context,request))