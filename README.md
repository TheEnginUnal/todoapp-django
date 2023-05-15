# todoapp

Python dili ve django kütüphanesi kullanarak bir to-do app tasarladım. Verileri bir veri tabanında tutmayı tercih ettim.
Front-end kısmınında bootstrap kullanılmıştır.
Giriş kısmında 2 tanımlı kullanıcı mevcut ;
superkullanıcı; admin-12345
normal kullanıcı; engin-engin12345

Siteye ilk giriş login sayfası bu şekilde ; 

![login](https://github.com/TheEnginUnal/todoapp-django/assets/101329489/e49551ee-1ac1-4232-b30e-68b8703247fc)

Normal kullanıcı ile giriş sağlandığında eğer kullanıcıya ait bir list yoksa sadece addlist alanı geliyor, eğer var ise hem addlist alanı ve beraberinde kullanıcıya ait liste ve içerisindeki itemler geliyor
![addlist](https://github.com/TheEnginUnal/todoapp/assets/101329489/6bdd954e-b5e5-4adc-b894-36441d9f966e)
Liste alanında kullanıcı yeni görevler ekleyebiliyor ayrıca finished butonu ile bitirdiği taskı bitirebiliyor. Taskı bitirir ise ToDoItem nesnesninin silinme tarihi değişiyor ve item listede görünmüyor.
![Screenshot 2023-05-15 215825](https://github.com/TheEnginUnal/todoapp/assets/101329489/7a208fab-0fff-4d4b-91a2-f05e6d4b40f3)

Eğer Kullanıcı sisteme superuser olarak giriş yapar ise karşısna tüm kullanıcların bulunduğu bir liste çıkıyor ; 
![superuser](https://github.com/TheEnginUnal/todoapp/assets/101329489/1e48fc6c-cf38-479e-9a24-d71fa41816b5)

Super Kullanıcı  info butonu ile diğer kullanıcıların listelerini görüntüleyebiliyor ve aynı zamanda üzerinde oynama yapabiliyor
![super](https://github.com/TheEnginUnal/todoapp/assets/101329489/41d5e73d-b1e5-44e2-87de-8f89eb5a4b41)


KOD KISMI;
Süper kullanıcıya ait işlemler superuser fonksiyon içerisinde gerçekleşiyor ![superuserkod](https://github.com/TheEnginUnal/todoapp/assets/101329489/0795c79d-f096-4bf7-a9bd-8857af0476cc)
superuser sayfasında butona post işlemi yapılması ile istenilen kullanıcının bilgilerine erişiliyor ve kullanıcıya ait liste veri tabanında ön yüze getiriliyor.

Normal kullanıcı için online olan kullanıcı için aynı işlemler yapılıyor;
![normaluserkod](https://github.com/TheEnginUnal/todoapp/assets/101329489/c356f735-d102-41f6-b8fe-5a30832ee89b)

getlist methodu veri tabanında bulunan ve online olan kullanıcının  verilerine erişmek için ; ![getlist](https://github.com/TheEnginUnal/todoapp/assets/101329489/dac51168-7ac3-44ae-b2a7-786f62d2eb2b)
