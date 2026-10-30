from flask import Flask
import random
app = Flask(__name__)

rastgele_gercekler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
                     "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
                      "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
                       "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız." ]



@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>    <a href="ikincisayfa">İkinci Sayfa </a>   '


@app.route("/ikincisayfa")
def ikincisayfa():
    return '''
    <h1>İkinci Sayfa</h1>
    <a href="/">Anasayfaya Dön</a>
    <br>
    <a href="/rastgele_gercekler">Rastgele Gerçekler</a>
    '''

@app.route("/rastgele_gercekler")
def ucuncusayfa():
    bilgi = random.choice(rastgele_gercekler)
    return f'''
    <h1>{bilgi}</h1>
    <a href="/ikincisayfa">İkinci Sayfaya Dön</a>
    <br>
    <a href="/">Anasayfa</a>
    '''

@app.route("/gizli")
def gizli():
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    olusan_sifre = ""

    for i in range(12):
        olusan_sifre += random.choice(karakterler)

    return f'''
    <h1>Gizli Sayfa</h1>
    <h2>Sifre Olusturucu</h2>
    <h3>{olusan_sifre}</h3>
    <a href="/gizli">Yeni Sifre Olustur</a>
    <br>
    <a href="/">Ana Sayfa</a>
    '''

app.run(debug=True)
