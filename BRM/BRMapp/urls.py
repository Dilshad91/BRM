from django.conf.urls import url
from BRMapp import views

urlpatterns = [
    url('new-book',views.newBook),
    url(r'^add',views.add),
    url('view-books',views.viewBooks),
    url('edit-book',views.editBook),
    url('edit',views.edit),
    url('search-book',views.searchBook),
    url('search',views.search),
    url('delete-book',views.deleteBook),
    

]
