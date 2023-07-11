#print

print("Hello world", sep = '', end = '\n' )

"""print fonksiyonu aldığı string argümanı
    dışarıya(terminale)çıktı olarak yazar.
    
    Aldığı parametreler:

        object: çıktı olarak yazılacak arguman.


        sep: 2 veya daha fazla object argümaı verildiğinde
            onları belli değerler ile ayırma olanağı sağlar.

            example: 
                    print("hello", "world", sep = ";") 
                    ---> output: Hello;world
            
            default = ''
        

        end: Ekrana basılacak son karakteri temsil eder.
            varsayılan değeri \n'dir. Printf yazdığımızda 
            yeni satıra geçmesinin sebebi \n ile bitmesidir.
            
            example: 
                    printf("Hello world", end = 1)
                    printf("Hello againn", end = &) 
                    ---> output: Hello world1Hello again&

            default = '\n'


        file: Object parametresine yazacağımız stringin istediğimiz
                bir dosyaya yazılabilmesini sağlar.

            example : 
                    sample = open('samplefile.txt', 'w')
                    print('Hello world', file = sample)
                    sample.close()
                    ---> Hello world stringini samplefile.txt dosyasının içine yazar.
            
            default = sys.stdout
"""