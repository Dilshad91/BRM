from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BRMapp.forms import NewBookForm, SearchForm
from BRMapp import models


def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-books')
def searchBook(request):
    form=SearchForm()
    res=render(request,'BRMapp/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'BRMapp/search_book.html',{'form':form,'books':books})
    return res
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)#intializing bookid fields
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMapp/view-books')
def viewBooks(request):
    books=models.Book.objects.all()
    #username=request.session['username']
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res
def newBook(request): #making a function to see form
    form=NewBookForm() #making a object of the form class NewBookForm by making a variable named form
    res=render(request,'BRMapp/new_book.html',{'form':form})
    return res
def add(request):#making a function to add data which is filled by the user
    if request.method=='POST':
        form=NewBookForm(request.POST)#To obtain form data which is stored in the form variable after submit
        book=models.Book()#making a object of the class Book by making a variable named book to represent record
        book.title=form.data['title']#filling the record and inserting into table
        book.price=form.data['price']#filling the record and inserting into table
        book.author=form.data['author']#filling the record and inserting into table
        book.publisher=form.data['publisher']#filling the record and inserting into table
        book.save()
        s="Record Stored<br><a href='/BRMapp/view-books'>view all Book</a>"
        return HttpResponse(s)
