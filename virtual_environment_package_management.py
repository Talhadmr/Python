#virtual environment and package management 

"""
    sanal ortamlar bir oturumdan ilgili paket ve araçların farklı sürümlerinin kullanılmasına olanak sağlar.
"""

"""
    Eğer bir projede numpy 1.0.0 sürümü ve başka bir projede numpy'nin 1.2.1 sürümü kullanılacaksa
    bu sanal ortam sayesinde yapılır. Böylelikle birbirinden farklı projeler için izole ortamlar sağlar.
"""

"""
    ben sanal ortam  yöneticisi olarak conda'yı kullanacağım. Araştırmak isteyenler için pipenv de sanal ortam yöneticisi olarak kullanılır.
    kodları anaconda prompt terminalinden yazacağım. 
"""


# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

#Paket yöneticisi
"""
    Python içinde bulunan kütüphane/modül/paketleri kullanmak için paket yöneticisi ile paketler bilgisayara indirilir.
    pip, conda kullanılan başlıca paket yükleyicilerindendir.
    conda hem bir sanal ortam yöneticisi hem da bir paket yükleyicisidir.
"""
# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi:
# conda upgrade –all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

