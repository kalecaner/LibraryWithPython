import sys
from Library import Library
from Book import Book

# Create a library object and initialize it with the "Books.txt" file
lib = Library("Books.txt")

# Main loop
continuity=True
while continuity==True:
   # Display the menu and get user input
   print("****MENU*****")
   print("1) Kitap Listesi")
   print("2) Kitap Ekle")
   print("3) Kitap Sil")
   print("Q) Çıkış")  


   userInput=input(" Yukarıda ki seçeneklerden birini seçiniz (1-4):")

   if userInput=='1':#     # List books as Business step
    books=lib.ListBooks()
    for book in books:
      print(f"Kitap Adı: {book.Name},Kitabın Yazarı: {book.Author}")
    print("Kitap listesi yukarıdaki gibidir")
   elif userInput=='2':  # add business step
       bookName=input("Kitap Adını  giriniz: ") 
       author=input("Yazar Adı: ")
       while True:
         try:
           year=int(input("Yayımlanma Yılı: "))
           break
         except ValueError:
           print("Geçersiz yıl girdiniz lütfen tekrar deneyiniz.")
       while True:
         try:
           pageAmount=int(input("Sayfa Sayısı: "))
           break
         except ValueError:
           print("Geçersiz Sayfa sayısı  girdiniz  Tam sayı değer ile tekrar deneyiniz")
       newBook=Book(bookName,author,year,pageAmount)  
       lib.AddBook(newBook)#add a book to the library
       print(f"{newBook.Name}-{newBook.Author}-{newBook.ReleaseDate}-{newBook.PageAmount} olarak belirlediğiniz kitabınız eklenmiştir")
       
   elif userInput=='3': #Delete Business Step   
     bookName=input("Silmek istediğiniz Kitap Adını  giriniz: ")
     lib.RemoveBook(bookName)
     print(f"{bookName} adlı kitap başarıyla silindi.")
   elif userInput=='q' or userInput=='Q': #exit Step
     continuity=False
     lib.CloseAll()
     sys.exit()
   else:
        # Invalid input
        print("Geçersiz  giriş yaptınız Lütfen listeden  seçim yapınız:")
  
