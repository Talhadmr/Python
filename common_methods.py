#common methods/functions

"""
    pythonda kullanılan belli başlı metod ve fonksiyonlar vardır.
    Metod bir sınıfın altında oluşturlmuş fonksiyonlardır.
    Bu fonksiyonlara ulaşmak için dir() fonksiyonu kullanılır.

    example:
            lst = [1, 2, 3]
            print(dir(lst))---> output: 'append', 'clear', 'copy', 'count',
                                  'extend', 'index', 'insert', 'pop', 
                                  'remove', 'reverse', 'sort']

    yukarıda "lst" liste tipinde oluşturulmuş bir nesnedir. dir fonskiyonuna arguman olarak bu nesneyi gönderdiğimizde;
    listeler üzerine uygulanabilecek fonksiyonları sıraladı bize.
"""
###     int()       ###

"""
    float bir sayıyı integer olarak değiştirmek için int fonksiyonu kullanılır.

    example:
            a_flo = 12.3
            print(type(a_flo))---> output: float

            a_int = int(a_int)
            print(type(a_int))---> output: int 

"""

###     float()     ###

"""
    integer bir sayıyı floata çevirmek için kullanılır.

    example:
        a_int = 3
        a_flo = float(a_int)

        print(a_flo)---> output: 3.0
"""



###     append      ###
"""
    listelerin sonuna yeni eleman eklenmesini sağlar.

    example:    
            lst = [1, 2, 3]
            lst.append(4)
            print(lst)---> output: [1, 2, 3, 4]
"""

###     insert      ###
"""
    listelerin belli bir indexine eleman eklemek için kullanılır.

    example:
            lst = [1, 2, 3]
            lst.insert(1, "a") /// ilk argüman; verilen değerin indexini, ikinci argüman; listeye eklenecek değeri taşır///
            print(lst)---> output: [1, 'a', 2, 3]
"""

###     pop     ###
"""
    listelerden eleman silmek için kullanılır.

    example:
            lst = ["a", "b", "c"]
            lst.pop(1) // aldığı argüman silinecek değerin indexini taşır.
            print(lst)---> output: ['a', 'c'] /// gördüğünüz üzere 1. indexteki "b" değeri listeden silindi.///
"""

###     upper       ###
"""
    Bir stringin içinde bulunan tüm küçük harfli karakterleri büyük harfe dönüştürür.
    str = "hello"
    str.upper()
    print(str)---> "HELLO" /// harflerin tümü büyüdü ///
"""

"""
    ***********************************************************************************************************
    *      Yukarıda Yazdığım fonksiyonlar gibi onlarce fonksiyon var.                                         *
    *      Bu fonksiyonlara ulaşmak için dir() fonksiyonunu kullanabilirsiniz                                 *         
    *      detaylı araştırma için interneti kullanabilirsiniz.                                                *              
    *      Keep going on... basssss                                                                           *
    *                                                                                                         *
    ***********************************************************************************************************

"""
