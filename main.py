import shutil
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from coin import CoinTossSimulation


def move_font_files():
    STREAMLIT_STATIC_PATH = Path(st.__path__[0]) / "static"
    CSS_PATH = STREAMLIT_STATIC_PATH / "assets/fonts/"
    if not CSS_PATH.is_dir():
        CSS_PATH.mkdir()

    css_file = CSS_PATH / "Monserrat"
    if not css_file.exists():
        shutil.copy("layout/Monserrat", css_file)


st.markdown(
    """
    <style>
@font-face {
font-family: 'Montserrat';
font-style: normal;
font-weight: normal;
src:url(https://fonts.google.com/specimen/Montserrat?query=mont)
}
html, body, [class*="css"] {
font-family: 'Montserrat'
}
</style>
""",
    unsafe_allow_html=True,
)

# option menu
selected = option_menu(
    menu_title="Main Menu",
    options=["Olasılık Dünyası", "Temel Olasılık", "Yazı/Tura", "Zar Simülasyonu", "Monty Hall Oyunu", "İletişim"],
    default_index=0,
    icons=["book", "hand-index", "coin", "dice-3", "door-open", "envelope"],
    orientation="horizontal",
)
if selected == "Olasılık Dünyası":
    # alt baslik
    st.subheader("Olasılık Kuramı Nasıl Ortaya Çıkmıştır?🧮 ")

    # text
    st.write("Olasılık kuramı, 17. yüzyılın ortalarından itibaren gelişmeye başlamıştır. Öncelikle Fransız matematikçi "
             "Blaise Pascal ve Pierre de Fermat tarafından olasılık kuramının temelleri atılmıştır. Pascal ve Fermat, "
             "birçok matematik problemi çözmek için olasılık kuramını kullanmaya başlamışlardır. Örneğin, Fermat, "
             "bir kâğıt oyununda kazanma olasılığını hesaplamak için olasılık kuramını kullanmıştır.")
    st.write("I. yüzyılın sonlarına doğru, olasılık kuramı, özellikle Fransa'da, birçok matematikçi tarafından daha "
             "ayrıntılı olarak incelenmeye başlandı. Bu çalışmalar, olasılık kuramının daha geniş bir alana "
             "uygulanabileceğini göstermiştir. Örneğin, 18. yüzyılda İsveçli matematikçi Anders Johann Lindström, "
             "olasılık kuramının tahmin ve istatistik alanlarında kullanılabileceğini göstermiştir.")
    st.write("II. yüzyılda, İngiliz matematikçi Thomas Bayes, olasılık kuramınıntemelini oluşturan Bayes Teoremi'ni "
             "ortaya attı. Bu teoremi, olaylar arasındaki ilişkileri ve olasılıkları modellemek için kullanılır. "
             "20. "
             "yüzyılın başlarında, olasılık kuramı ve istatistik alanlarındaki çalışmalar hızlandı ve bugün "
             "olasılık "
             "kuramı ve istatistik, birçok alanda kullanılmaktadır.")


    def load_lottieurl(url: str) -> object:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    # animasyon
    lottie_question = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_u7yrcwlk.json")
    st_lottie(
        lottie_question,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        height=150
    )
    st.write("Belirli bir olay A için olasılık P(A) 0 ile 1 arasında değişen bir sayı ile temsil edilir.Hiç olanaksız "
             "bir olay için olasılık 0 olur ve kesinlikle olacak bir olayın olasılığı 1 olur. Bazı istatikçicler bu "
             "uçsal olasılık değerlerinin sadece teorik olduğunu iddia etmektedirler çünkü kabul ettikleri olasılık "
             "açıklaması deneylemelerle limitte göresel çoklukluk (relatif frekans) değerine dayanır.Diğer Bayes-tipi, "
             "özellikle, olasılık açıklamasına göre bu uçsal olasılık değerlerini sübjektif olarak düşünmek ve "
             "olaylara bu değeleri koymak imkan dahilindedir.")
if selected == "Temel Olasılık":
    st.markdown('**“THE WORLD IS AN UNCERTAIN PLACE”**')
    st.write("Bu bölüm olasılık teorisinin temel kavramlarını tanıtmak amaçlıdır.")
    st.write("Yarınki hava durumu gibi sıradan görünen bir şey hakkında tahminlerde "
             "bulunmak gerçekten de zor bir iştir. Modern zamanların en gelişmiş bilgisayarları ve modelleriyle bile "
             "meteoroloji uzmanları yarın yağmur yağıp yağmayacağını kesin olarak söyleyemezler. Yapabilecekleri en "
             "iyi şey, yarın yağmur yağma olasılığına ilişkin en iyi tahminlerini vermektir. Örneğin, meteoroloji "
             "uzmanları yarın yağmur yağacağından oldukça eminlerse, yağmur yağma ihtimalinin %90 olduğunu "
             "söyleyebilirler. Muhtemelen hayatınız boyunca bu tür ifadeler duymuşsunuzdur, ancak yağmur olasılığının "
             "%90 olduğunu söylediklerinde bunun tam olarak ne anlama geldiğini hiç merak ettiniz mi? ")


    # animasyon
    def load_lottieurl(url: str) -> object:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_think = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_o18imdcr.json")
    st_lottie(
        lottie_think,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        height=350
    )
    st.subheader(':blue[Şans Oyunları]')
    st.write("Şans olaylarının mantıksal olarak tutarlı bir şekilde analiz edilmesini sağlayan matematiksel temel, "
             "olasılık teorisi olarak bilinir. Bir olayın olasılığı, o olayın gerçekleşmesinin ne kadar muhtemel "
             "olduğunun sayısal bir göstergesidir. Bu değer her zaman 0 ve 1 aralığındadır; 0 imkansızlığı, "
             "1 ise güveni ifade eder. İki potansiyel sonucu yazı veya tura olan adil bir yazı tura, olasılıksal bir "
             "deneyin klasik bir örneğidir. Bu durumda yazı tura atma olasılığı 50/50'ye eşittir. Gerçek bir yazı "
             "tura atma kümesinde tam olarak %50'den daha fazla ya da daha az tura gelebilir. Ancak, daha fazla yazı "
             "tura atıldığında, uzun vadede tura gelme sıklığı kaçınılmaz olarak %50'ye yaklaşacaktır.Adil olmayan "
             "veya ağırlıklı bir madeni para için iki sonuç eşit olasılıkta değildir.Sonuçlara sayılar atarsak - "
             "örneğin yazı için 1, tura için 0 - o zaman rastgele değişken olarak bilinen matematiksel nesneyi "
             "yaratmış oluruz.")
    st.subheader(':orange[Beklenti]')
    st.write("Rastgele bir değişkenin beklentisi, bu rastgele değişkenin dağılımının merkezini yakalamaya çalışan bir "
             "sayıdır. Verilen dağılımdan alınan birçok bağımsız örneğin uzun dönemli ortalaması olarak "
             "yorumlanabilir. Daha açık bir ifadeyle, rastgele değişkenin desteğindeki tüm olası değerlerin olasılık "
             "ağırlıklı toplamı olarak tanımlanır,")
    st.latex("{E}[X] = \sum_{x \in \mathcal{▢}}xP(x)")
    st.subheader(':green[Varyans]')
    st.write("Beklenti bir merkezilik ölçüsü sağlarken, rastgele bir değişkenin varyansı o rastgele değişkenin "
             "dağılımının yayılımını ölçer. Varyans, rastgele değişken ile beklentisi arasındaki karesel farkın "
             "ortalama değeridir.")
    st.latex("{Var}(X) = {E}[(X -{E}[X])^2]")

if selected == "Yazı/Tura":
    st.subheader("Yazı/Tura Deneyleri 🪙")
    st.write("Kısa cevaplar alabilmek için en iyi yollardan biri de madeni paraları kullanmaktı fakat ilk "
             "olarak Lidyalılar tarafından MÖ 10.yüzyılda kullanılmaya başlanmıştır. Zaten kullanılmaya başladığında "
             "da Tanrıların insanlar hakkında karar verdiği bir araç olarak düşünülmemiştir. Dokuz yüzyıl sonra ise "
             "Julius Caesar (Sezar) yazı turayı başlatmıştır. Romalıların paralarının bir yüzünde Sezar’ın kafasının "
             "resmi vardı ve para havaya atıldığında Türkçe’de baş anlamına gelen head kısmı yani Sezar’ın kafasının "
             "olduğu kısım gelirse dileğin Tanrı tarafından yerine getirileceği veya bir konudaki haklı tarafın kim "
             "olduğunu gösteriyordu. Kısaca kazanmak için head kısmı gelmeliydi.")
    st.write("Paranın havada yakalandığı klasik yazı tura oyununda yalnız iki olasılık vardır, para ya yazı ya tura "
             "gelir. Yazının ya da turanın art arda birkaç defa gelmesi doğal karşılanır ancak yazı tura atılmaya "
             "devam edilirse, yazıların ya da turaların oranı gitgide %100'ye yaklaşır.  Paranın havada yakalanmadığı "
             "yazı tura oyununda yere düşen paranın dik gelmesi ihtimali çok düşüktür. Bu nedenle yazı ve tura "
             "oranları uzun vadede yine %50'ye çok yakın olacaktır.")


    def load_lottieurl(url: str) -> object:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_question = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1l9gpfir.json")
    st_lottie(
        lottie_question,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        height=300
    )

    num_tosses = st.number_input("Kaç Kez para atmak istersiniz? :coin:", format="%d", min_value=1, max_value=1000)
    sim = CoinTossSimulation(num_tosses)
    simulation_result = sim.run_simulation
    heads, tails = simulation_result[0], simulation_result[1]

    st.plotly_chart(sim.plot_result)

if selected == "Zar Simülasyonu":
    st.title(f"You have selected {selected}")
if selected == "Monty Hall Oyunu":
    st.title(f"You have selected {selected}")
if selected == "İletişim":
    st.title(f"You have selected {selected}")
