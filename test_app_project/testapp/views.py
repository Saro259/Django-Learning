from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from testapp.models import ToDo


# Create your views here.
COMPLETED_TO_BOOL = {
    "0": False,
    "1": True
}

ORDER_TO_STRING = {
    "0": "created_at",
    "1": "-created_at"
}

def index(request):
    search = request.GET.get("todoSearch")  # request.GET is in itself a dictionary, so dictionary.get() either gives the value present in the memory or a defualt value i e None 
    completed = request.GET.get("completed")
    order = request.GET.get("order")
    all_todos = ToDo.objects.all() # arranges in descending order
    if search != None:
        all_todos = all_todos.filter(title__icontains=search) # to filter them with the search  # print(all_todos.query) to print queries
    if completed != None:
        value = COMPLETED_TO_BOOL.get(completed)
        all_todos = all_todos.filter(completed=value)
    if order != None: 
        value = ORDER_TO_STRING.get(order) 
        all_todos = all_todos.order_by(value)
    data = {
        "todos" : all_todos 
    }
    page_name = "index.html"
    return render(request, page_name, context=data)

def add_view(request):
    if request.method=="GET":
        return HttpResponse("Invalid Method")
    else:
        todo_input = request.POST['todoInput']
        ToDo.objects.create(title=todo_input)
        return redirect("todo_index")
            
def delete_view(request, todo_id): # to delete details of specific id 
    if request.method=="POST":
        return HttpResponse("Invalid Method")
    else:
        try:
            todo_object = ToDo.objects.get(id=todo_id)
            todo_object.delete() 
            return redirect("todo_index")
        except ToDo.DoesNotExist:
            return HttpResponse("Error todo not found")

def mark_view(request, todo_id): # to mark specific id as completed 
    if request.method=="POST":
        return HttpResponse("Invalid Method")
    else:
        try:
            todo_object = ToDo.objects.get(id=todo_id)
            todo_object.completed = True
            todo_object.save() 
            return redirect("todo_index")
        except ToDo.DoesNotExist:
            return HttpResponse("Error todo not found")







