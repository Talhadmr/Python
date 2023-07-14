#fonksiyonlar

"""
    Fonksiyon kendini tekrar eden ilgili eylemleri gerçekleştirmek için kullanılan, yeniden düzenlenebilir kod bloklarıdır.

    matematik gören herkes fonksiyonlarla çalışmıştır. Programlamadaki fonksiyonlar da matematiktekiler ile çok benzerdir.

    matematik:
            "f(x) = 2x + 8" 
    Python:
            def func(x):
                2x + 8:
    gördüğünüz üzere birbirine benzer yapılar.
    Başta yazılan "def" ifadesi bunun bir fonksiyon olduğunu python'a bildirmek için kullanılır 
    "func" fonskiyonun ismini belirtemkte daha sonra bu foksiyonu çağırmak istediğimizde bu ismi kullanacağız.
    "(x)" x bir parametredir. Fonksiyonu çağırırken bu parametreye gerekli argümanlar atanır.
    ":" bu işaretin altına yazdığımız her şey bu fonksiyonun ne yapacağını gösterir.
"""

#Fonksiyon çağırma

"""
    def circle(r,pi):
        area = pi*r**2
        print(area)
    
    Yukarıda yazılan fonksiyon dairenin alanını hesaplayan bir fonksiyon.

    Bu fonksiyonu çağıralım şimdi, örneğin yarıçapı 4, pi sayısını da 3 olarak kabul edelim.
        
        circle(4,3)
    
    Fonksiyonun adını yazıp, açtığımız parantezin içini sırasıyla belirlediğimiz r ve pi argümanları ile doldurduk.
    program bu değerleri alıp yukarıdaki circle fonksiyonuna götürdü ve bu sayılar ile area değişkenine eşitlediğimiz 
    formülü çalıştırdı. 
    print ile area değişkenini ekrana bastı

        output---> 48
"""

#return 

""" 
    return kavramı programlama öğrenirken en çok kafamı karıştıran kavramların başında gelirdi.
    yukarıdaki circle fonksiyonunda değeri sadece ekrana bastık. 
    Peki bu fonksiyondan bir değişken döndüremez miyiz?
    
    eğer return kullanmazsak:

        def circle(r, pi):
            area = pi*r**2

        a = circle(4, 3)
        print(a) ---> output: None 

        circle fonksiyonu hiçbir değer döndürmediği için a değişkeni boş kaldı. (bazı derleyicilerde hata verebilir)

    
    eğer return kullanırsak:

        def circle(r, pi):
            area = pi*r**2
            return (area)
        
        a = circle(4, 3)
        print(a) ---> output: Bunun sonucunda ekrana circle fonksiyonundan gelen area değerini basacaktır.

        
    Bu şekilde fonksiyondan herhangi bir değeri döndürebilir ve bunu istediğiniz gibi kullanabilirsiniz.

    daha iyi kavrayabilmek için bir örnek daha yapalım.

    eğer return kullanmazsak:
        
        def vki(weight, height):
            result = weight/height**2

        num = vki(70, 1.75)
        print(num) ---> None

    eğer return kullanırsak:
        def vki(weight, height):
            result = weight/height**2
            return (result)

        num = vki(70, 1.75)
        print(num) ---> 22.857
        Fonksiyondan dönen değeri istediğiniz gibi kullanabilirsiniz.

        dönen değeri farklı bir işlemin içinde kullanabilirsiniz.
        example:
            age = 22
            age*num

            
"""


#docstring

"""

     Bir fonksiyon tanımlanırken fonksiyon hakkında bilgiler vermeliyiz ki bir sonraki takım arkadaşımız
    yazılan fonksiyonun nasıl çalıştırılacağını, ne işe yaradığını anlasın.

    example:
            def vki(weight, height):
            '''
            Calculates body mass index. /// fonksiyonun ne işe yaradığından bahsedilir.

                Parameters:
                    weight (int): ///burada parametrenin ismi ve tipini belirtiyoruz
                    height (float): ///fonksiyonun ne işe yaradığını bilmeyen biri boy kısmına integer olarak boyunu yazabilirdi.


                Returns:
                    binary_sum (float): body mass index /// fonksiyonun ne döndüğü yazılır.
            '''
    
            result = weight/height**2
            return (result)    
"""

#ön tanımlı argüman 

"""
    Fonksiyon tanımlanırken parametre kullandığımızdan bahsettik fakat
    bu paramtreler ön tanımsızdı.

    ön tanımsız bir fonksiyon:

        def circle(r, pi):
            area = r*pi**2
        
    ön tanımlı bir fonksiyon:

        def circle(r, pi = 3.14):
            area = r*pi**2
    
    ön tanımlı fonksiyonda pi parametresine bir değere eşitledik.
    eğer fonksiyonu çağırırken pi değerini belirtmezsek donksiyon pi değerini 3.14 olarak alıp işleme devam edecektir.
    Bu değeri sonradan fonksiyonu çağırırken de değştirebilirsiniz. 
    örneğin fonksiyonu circle(4, 3) diye çağırdığınızda fonksiyon artık pi değerini 3 olarak alacaktır. 
"""

#Local/global variable

"""
    a = 5

    a burada bir değişkendir fakat yazıldığı yere göre global veya local değişken olarak isimlenidirilir.

    eğer bir fonksiyonun içinde tanımlayacaksanız bu loacal değişkendir.
    local değişkene yazdığınız bloğun dışından ulaşamazsınız.

    example:
        def say_Hello(): /// fonksiyonlar hiç argüman almadan da kullanılabilir.
            local_a = 21
            print("Hello")
        şimdi fonksiyonun dışından bu fonksiyona ulaşmaya çalışalım.
        print(local_a) ---> output: NameError: name 'a' is not defined 
        a isminde bir şey tanımlanmadı diye hata vaerdi.

    global_a = 13

    print(global_a) ---> output: 13

    global değişkenlerden her yerden ulaşılabilir. Bir fonksiyonun içinde dahi ulaşabilirsiniz.

    exampla:
        def say_Hello():
            print(global_a) ---> output: 13

    
    bir global değişkeni localde değiştirmeye çalışırsanız bile global değerini korumaya devam edecektir.

    example: 

    global_a = 7

    def sayhell():
        global_a = 9

    sayhell()
    print(global_a) ---> output: 7

"""
