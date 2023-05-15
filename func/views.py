from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoItem,ToDoList 
from datetime import date

# Anasayfadır. Kullanıcı buradan giriş işlemlerini sağlayabilir.
@csrf_exempt
def home(request):

    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect(list)
        else:
            return render(request, "home.html", {
                "error" : "username or password is incorrect"
            })

    return render(request, 'home.html')


# List fonksiyonu, kullanıcıya ait listlerin olduğu, listler oluşturabildiği ve görev ekleyebildiği sayfa için yazılmıştır.
@csrf_exempt
def list(request):
# Bir normal kullanıcı tanımlı birde super kullanıcı tanımlı, bütün fonksiyonlar bu view içerisinde gerçekleşiyor
    if request.user.is_superuser:
        if request.method == "POST":
            if 'userinfo' in request.POST:
                username = request.POST["userinfo"]
                user = User.objects.get(username = username)
                
                superlist = ToDoList.objects.filter(userid = user.id)
                superlists = []
                for l in superlist:
                    items = ToDoItem.objects.filter(listid= l,deletionDate = None)
                    # completion rate 
                    allitem = ToDoItem.objects.filter(listid = l)
                    compilerate = 0
                    if len(allitem) > 0: 
                        compilerate = 100 - ((len(items) / len(allitem) ) * 100)
                    
                    list_data = {
                        'superlistid' : l.id,
                        'supername' : l.name,
                        'superitems' : items,
                        'supercomplie' : compilerate
                    }

                    superlists.append(list_data)
                
                return render(request, "superlist.html",
                            {'superlists': superlists}
                            )
            

            
      
        return render(request, "superlist.html")



    if request.method ==  "POST":
        if 'addTask' in request.POST:
            listid = request.POST["addTask"]
            content = request.POST["content"]
            newitem = ToDoList.objects.get(pk = listid)
            ToDoItem.objects.create(userid=request.user,listid = newitem , content = content)            
            return redirect('list')
        elif 'finished' in request.POST:
            itemid = request.POST["finished"]
            finisheditem = ToDoItem.objects.get(pk = itemid)
            finisheditem.deletionDate = date.today()
            finisheditem.save()
            return redirect('list')
        elif 'deleteList' in request.POST:
            listid = request.POST["deleteList"]
           
            deletionList = ToDoList.objects.get(pk = listid)
            deletionList.delete()
            return redirect('list')
        elif 'addList' in request.POST:
            name = request.POST["newListName"]
            ToDoList.objects.create(userid= request.user,name = name)
            return redirect('list')

 
    else:      
        return render(request,"list.html")

# Kullanıcıya ait list ve itemleri getiren fonksiyon 
def getList(request):
    if request.user is not None:
        list = ToDoList.objects.filter(userid = request.user)
        lists = []
        for l in list:
            items = ToDoItem.objects.filter(listid= l,deletionDate = None)
            # completion rate 
            allitem = ToDoItem.objects.filter(listid = l)
            compilerate = 0
            if len(allitem) > 0: 
                compilerate = 100 - ((len(items) / len(allitem) ) * 100)
                
           


            list_data = {
                'listid' : l.id,
                'name' : l.name,
                'items' : items,
                'complie' : compilerate
            }

            lists.append(list_data)
            
        return ({
            'lists' : lists,     
            })
    else:
        return render("home.html")


def superuserlist(request):
    return render(request, "superlist.html")


def getUserInfo(request):
    users = User.objects.all()
    return ({
        'users' : users
    })

