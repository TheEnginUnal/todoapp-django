# todoapp

Python dili ve django kütüphanesi kullanarak bir to-do app tasarladım. Verileri bir veri tabanında tutmayı tercih ettim.
Front-end kısmınında bootstrap kullanılmıştır.
Giriş kısmında 2 tanımlı kullanıcı mevcut ;
superkullanıcı; admin-12345
normal kullanıcı; engin-engin12345

Siteye ilk giriş login sayfası bu şekilde ; 

![login](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/e49551ee-1ac1-4232-b30e-68b8703247fc)

Normal kullanıcı ile giriş sağlandığında eğer kullanıcıya ait bir list yoksa sadece addlist alanı geliyor, eğer var ise hem addlist alanı ve beraberinde kullanıcıya ait liste ve içerisindeki itemler geliyor
![addlist](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/b9dfcf9c-15e2-49be-82f0-edb13a04a520)

Liste alanında kullanıcı yeni görevler ekleyebiliyor ayrıca finished butonu ile bitirdiği taskı bitirebiliyor. Taskı bitirir ise ToDoItem nesnesninin silinme tarihi değişiyor ve item listede görünmüyor.
![Screenshot 2023-05-15 215825](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/6bcddbc3-abe3-48c1-8441-ad2848cebde2)


Eğer Kullanıcı sisteme superuser olarak giriş yapar ise karşısna tüm kullanıcların bulunduğu bir liste çıkıyor ; 
![superuser](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/2abb7e24-a285-447f-9d6d-3a303e07f17c)


Super Kullanıcı  info butonu ile diğer kullanıcıların listelerini görüntüleyebiliyor ve aynı zamanda üzerinde oynama yapabiliyor

![super](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/47e1d139-f3eb-42e3-87a1-6d3c2a0a66b8)


KOD KISMI;
Süper kullanıcıya ait işlemler superuser fonksiyon içerisinde gerçekleşiyor 
![superuserkod](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/ad2e58a0-f923-4456-842e-2299cd865a25)

superuser sayfasında butona post işlemi yapılması ile istenilen kullanıcının bilgilerine erişiliyor ve kullanıcıya ait liste veri tabanında ön yüze getiriliyor.

Normal kullanıcı için online olan kullanıcı için aynı işlemler yapılıyor;
![normaluserkod](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/a5d6048a-5a6c-48d4-941c-3a0c96853e0a)


getlist methodu veri tabanında bulunan ve online olan kullanıcının  verilerine erişmek için ; 
![getlist](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/78872b15-62ff-44fb-ae2e-2bf9c2683bc1)
