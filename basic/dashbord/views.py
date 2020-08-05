from django.shortcuts import render,redirect
from .models import Components

# Create your views here.

def update(request):
    if request.method == 'POST':
        name = request.POST['name']
        n_del = request.POST['delete']
        if name != "" and n_del == "":
            new_item = Components(name=name)
            new_item.save()
        elif name == "" and n_del != "":
            Components.objects.filter(name=n_del).delete()
        else:
            print("Nothin can do")
        return redirect('update')
    else:
        items = Components.objects.all()
        return render(request,'dashbord.html',{'items':items})

def value(request):
    if request.method == 'POST':
        val = request.POST['but']
        print("Recived some stuff")
        val=val.split('/')
        feed=val[0]
        cur_state=val[1]
        Components.objects.filter(name=feed).update(state=cur_state)
        print(feed,' is ',cur_state)
        return redirect('update')
    else:
        return redirect('update')
