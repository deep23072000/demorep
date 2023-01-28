from django.shortcuts import render,redirect
from . models import record,info,work,benifits


def index(req):
    rec=record.objects.all()
    rec1=work.objects.all()
    rec2=benifits.objects.all()
    return render(req,'index.html',{'rec':rec,'rec1':rec1,'rec2':rec2})

def consultancy(req):
    return render(req,'consultancy.html')

def consultancyTask(req):
    detail=info()
    name=req.POST.get("name")
    email=req.POST.get("email")
    contact=req.POST.get("contact")
    query=req.POST.get("query")
    detail.name=name
    detail.email=email
    detail.contact=contact
    detail.query=query
    detail.save()
    return redirect('/consultancy')

def services(req):
    return render(req,'services.html')

def portfolio(req):
    return render(req,'portfolio.html')


def contact(req):
    return render(req,'contact.html')

def contactTask(req):
    detail=info()
    name=req.POST.get("name")
    email=req.POST.get("email")
    contact=req.POST.get("contact")
    query=req.POST.get("query")
    detail.name=name
    detail.email=email
    detail.contact=contact
    detail.query=query
    detail.save()
    return redirect('/contact')

def about(req):
    return render(req,'about.html')


# Admin end views

def admin(req):
    return render(req,'admin.html')
    
def adminhome(req):
    admemail=req.POST.get("email")
    admpassword=req.POST.get("password")
    if admemail=="admin@gmail.com" and admpassword=="admin123":
        return render(req,'adminhome.html')
    else:
        return render(req,'admin.html')

def adminhomeedit(req):
    return render(req,'adminhome.html')
    
def cardTask(req):
    val=req.POST.get("card")
    val1=req.POST.get("work")
    val2=req.POST.get("benifits")
    if val=="card":
        card=record()
        color=req.POST.get("color")
        fa=req.POST.get("fa")
        header=req.POST.get("header")
        desc=req.POST.get("desc")
        card.faicon=fa
        card.heading=header
        card.content=desc
        card.color=color
        card.save()
        return redirect('/card')
    elif val1=="Work with Whiltor":
        card=work()
        image=req.POST.get("image")
        header=req.POST.get("header")
        desc=req.POST.get("desc")
        card.image=image
        card.heading=header
        card.content=desc
        card.save()
        return redirect('/card')
    
    elif val2=="benifits":
        card=benifits()
        image=req.POST.get("image")
        title=req.POST.get("title")
        card.image=image
        card.title=title
        card.save()
        return redirect('/card')

    else:
        return render(req,'adminhome.html')



def card(req):
    rec=record.objects.all()
    rec1=work.objects.all()
    rec2=benifits.objects.all()
    return render(req,'card.html',{'rec':rec,'rec1':rec1,'rec2':rec2})

def cardTaskdone(req):
    id=req.GET.get('bid')
    ob=record.objects.get(id=id)
    ob.delete()
    return redirect('/card')

def cardTaskwork(req):
    id=req.GET.get('bid')
    ob=work.objects.get(id=id)
    ob.delete()
    return redirect('/card')

def cardTaskbenifits(req):
    id=req.GET.get('bid')
    ob=benifits.objects.get(id=id)
    ob.delete()
    return redirect('/card')

def logout(req):
    return render(req,'index.html')

# Create your views here.
