import seaborn as sns
df = sns.load_dataset("titanic")

#car_crashes veri setinde, içinde sayısal veri tutan kolonların isminin başına NUM_ ekler ve tüm harfleri büyütür.
"""
def func(df):
    name_list = []
    for index, col in enumerate(df.columns,0) :
        if df[col].dtype in [float, int]:
            df.rename(columns={col: "NUM_" + col}, inplace=True)
        name_list.append(df.columns[index])
        name_list[index] = name_list[index].upper()
    return name_list

lst = func(df)
lst
"""


#List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
#abbrev, noprevious
#df2 = df.drop(["abbrev", "no_previous"], axis = 1)




"""
Görev 1:  Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
Görev 2:  Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
Görev 3:  Her bir sutuna ait unique değerlerin sayısını bulunuz.
Görev 4:  pclass değişkeninin unique değerlerinin sayısını bulunuz.
Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
Görev 6:  embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
Görev 7:  embarked değeri C olanların tüm bilgelerini gösteriniz.
Görev 8:  embarked değeri S olmayanların tüm bilgelerini gösteriniz.
Görev 9:   Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
Görev 10:  Fare’i 500’den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
Görev 11:  Her bir değişkendeki boşdeğerlerin toplamını bulunuz.
Görev 12:  who değişkenini dataframe’den çıkarınız.
Görev 13:  deck değikenindeki boşdeğerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
Görev 14:  age değikenindeki boşdeğerleri age değişkenin medyanı ile doldurunuz.
Görev 15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
Görev 16:  30 yaşın altında olanlar 1, 30’a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
Görev 17:  Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
Görev 18:  Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 19:  Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day’e göre toplamını, min, max ve ortalamasını bulunuz.
Görev 21: size’i 3’ten küçük, total_bill’i 10’dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
Görev 22:  total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
Görev 23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe’e atayınız.
"""

#görev 1 
df = sns.load_dataset("titanic")

#görev 2
df["sex"].value_counts()

#görev 3
df.nunique()

#görev 4
df["pclass"].nunique()

#görev 5
df["pclass"].nunique()
df["parch"].nunique()

#görev 6
df["embarked"].dtype
df["embarked"].astype("category")
df["embarked"].dtype

#görev 7 

"""for index, i in enumerate(df["embarked"]):
   if i == 'C':
    df.iloc[index:index + 1, : ]"""
df[df["embarked"] == 'C'].head(10)

#görev 8

df[df["embarked"] != 'C'].head(10)

#Görev 9:

df[(df["sex"] == "female") & (df["age"] < 30)].head(10)

#görev 10

df[(df["fare"] < 500) & (df["age"] > 70)].head()

#görev 11

df.isnull().sum()

#görev 12

df = df.drop("who", axis = 1)
df.head()

#görev 13

mode = df["deck"].mode()[0]
df["deck"].fillna(mode)


"""
Görev 14:  age değikenindeki boşdeğerleri age değişkenin medyanı ile doldurunuz.
Görev 15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
Görev 16:  30 yaşın altında olanlar 1, 30’a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
Görev 17:  Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
Görev 18:  Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 19:  Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day’e göre toplamını, min, max ve ortalamasını bulunuz.
Görev 21: size’i 3’ten küçük, total_bill’i 10’dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
Görev 22:  total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
Görev 23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe’e atayınız.
"""

#görev 14
df["age"].fillna(df["age"].median())

#görev 15
df.groupby(['pclass',"sex"])["survived"].agg(["mean","count", "sum"])

