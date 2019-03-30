from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.Author_List_Veiw.as_view(), name='author'),
    path('author/<int:pk>', views.Author_Detail_View.as_view(), name='author_details'),
    path('book/', views.Book_list_View.as_view(), name='book'),
    path('book/<int:pk>', views.Book_Detail_View.as_view(), name='book_details'),

]
