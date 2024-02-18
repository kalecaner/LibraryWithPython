from Book import Book
import os

#library class   makes about books like data Layer
class Library:

  def __init__(self,filePath):# constructor method 
   # Initialize a new Library object with the given file path.
    self.filePath = filePath
    if  os.path.exists(filePath):# check that is three file
      self.file=open(self.filePath,"a+", encoding='utf-8')   #open  file  as  insert row mode
    else:     
      self.file=open(self.filePath,"w+", encoding='utf-8') #create file and  writing mode
     
        
    
  def AddBook(self,Book):# add new Book in the txt file     
      Bookstr=f"{Book.Name}-{Book.Author}-{Book.ReleaseDate}-{Book.PageAmount}\n" #create  a string  to add in txt file
      check=self.IsDublicate(Book) #check if it is frome  same bookname
      if check==True:
        print(f"Veri listesinde {Book.Name} isimli kitap mevcuttur.")
      else:
        try:
          if self.file.closed: #check   open writing Mode
            self.file=open(self.filePath,"a+", encoding='utf-8')
          self.file.write(Bookstr)
          print(f"Kitap başarıyla eklendi.\nVeriler : {Bookstr}")     
        except Exception as e:
          print("bir hata Oluştu")
          self.file.close()
          self.file=open(self.filePath,"a+", encoding='utf-8')
      self.CloseAll()
      


  def ListBooks(self): #list all books
    books = []
    with open(self.filePath, "r", encoding='utf-8') as file:
        lines = file.read().splitlines()
        if len(lines)>0:
            for line in lines:
                if line:
                    Name, Author, ReleaseDate, PageAmount = line.split('-')
                    PageAmount = int(PageAmount)
                    book = Book(Name, Author, ReleaseDate, PageAmount)
                    books.append(book)
        else:
          print("Listede veri bulunmamaktadır")

    return books    
  def IsDublicate (self,Book):
   books=self.ListBooks()
   if len(books)>0:
    for book in books:
      if book.Name==Book.Name and book.Author==Book.Author:
        return True
      else:
        return False
   else:
     return False 
  def RemoveBook(self,bookName): #Delete  the book
    books=self.ListBooks()
    thereIsBook=False
    for i,book in enumerate(books):
     if book.Name==bookName:
        thereIsBook=True
        break
    if thereIsBook==False:
     print("Belirttiğiniz Kitap adı Listede bulunmamakta lütfen tekrar deneyiniz")
    elif  thereIsBook==True: 
     with open(self.filePath, 'w', encoding='utf-8') as file:
       for i,book in enumerate(books[:i] + books[i+1:]):
        Bookstr=f"{book.Name}-{book.Author}-{book.ReleaseDate}-{book.PageAmount}\n" 
        if self.file.closed:
             self.file=open(self.filePath,"w", encoding='utf-8')    
        file.write(Bookstr)    
       self.CloseAll()
  def CloseAll(self):
     if not self.file.closed: #check   open writing Mode
       self.file.seek(0)
       self.file.close()
    
  

      
   
      
 
   
         
         
       
        




  