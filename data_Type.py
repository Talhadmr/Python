#data types

#numeric types

i = 4
""" i integer bir değer olan 4 sayısını temsil etmektedir
    integer sayılar; -2.147.483.648 ve 2.147.483.647 arasındaki
    tüm TAM sayı değerleri alabilir.
"""

f = 3.14
"""f float bir değer olan 3.14 sayısını temsil eder.
    float sayılar; ondalık sayıları temsil etmemize yarar.    
"""

#text types

c = 'c'
""" 
    c char bir değer olan c karakterini tutar içinde.
    char değerler; tek bir harften oluşan string yapılardır.
"""

s = "Data"
"""
    s Data yazısını içinde tutan string bir değişkendir.
    string; birden fazla karakterin bir araya gelmesi ile oluşur.
"""

#boolean types

t = True
"""
    t True olan boolean veri tipini temsil eder.
    True boolen; Koşulların doğru olduğu durumlarda geri dönülem değerdir.

    example: 
            1 = 1 ---> bunun sonucu doğru olduğundan eğer bir if koşulunun içine yazarsak True dönecektir.
"""

f = False
"""
    f False olan boolean veri tipini temsil eder.
    False boolen; Koşulların yanlış olduğu durumlarda geri dönülem değerdir.

    example: 
            1 = 0 ---> bunun sonucu yanlış olduğundan eğer bir if koşulunun içine yazarsak False dönecektir.
"""
#sequence types

l = ["elma", "armut", "muz"]
"""
    l liste tipinde oluşturulmuş bir nesnedir. 

    (Nesne:
        pythonda liste, integer, değişken, fonksiyon... neredeyse her şeyin genel bir ismidir.)
    
    liste; İçinde string, integer... değerleri tutabilen yapılardır.
    ***listenin içinde bulunan her bir değerin bir index numarası vardır.
    ***ilk değerin indexi sıfırdır ve artarak devam eder.
    ***üçüncü değere ulaşılmak istendiğinde l[2] yazılır.
    ***listenin içindeki değerler değiştirilebilir.
    ***ikinci değer farklı bir değer ile değiştirilmek istendiğinde l[1] = "kiraz" yazılmalı.
    ***listeye yeni eleman eklenebilir. 
    ***l.append("portakal") yazıldığında listenin sonuna portakal nesnesi eklenir.
"""

tup = ("apple", "banana", "cherry")
"""
    tup tuple tipinde oluşturulmuş bir nesnedir.
    ***listeler ile çok ortak özellikleri vardır fakat tuple içindeki değerler değiştirilmezler.
    ***indexleri vardır. listeler gibi indexler ile ulaşılabilir.
    ***iki tupple birleştirilebilir.
"""

dic = {"name" : "Talha",
       "Age": 22}
"""
    dic sözlük(dictionary) tipinde oluşturulmuş bir nesnedir.
    sözlükler key ve value olmak üzere iki yapıdan oluşur.
    ***key üzerinden value ulaşılabilir. örneğin print(dic["name"])---> çıktı olarak Talha basacaktır.
    
"""