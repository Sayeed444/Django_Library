from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Author,Name,Book
# Create your views here.
def home(request):
    Storage_book=Name.objects.all().count()
    author=Author.objects.all().count()
    books=Book.objects.all().count()
    context={
        'Storage_book':Storage_book,
        'author':author,
        'books':books,
    }
    return render(request,'second/home.html',context)

class Author_List_Veiw(ListView):
    template_name = 'second/author.html'
    model = Author
    #context_object_name = 'author_x'
    paginate_by = 12

class Author_Detail_View(DetailView):
    model = Author

class Book_list_View(ListView):
    template_name = 'second/book.html'
    model = Book
    paginate_by = 12

class Book_Detail_View(DetailView):
    model = Book
    template_name = 'second/book_details.html'