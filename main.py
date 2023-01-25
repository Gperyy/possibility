import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

import shutil
import math
from pathlib import Path
from coin import CoinFlipSimulation
import plotly.figure_factory as ff
import numpy as np


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
    options=["Olasılık Dünyası", "Yazı/Tura", "Zar Simülasyonu", "Monty Hall Oyunu", "İletişim"],
    default_index=0,
    icons=["book", "coin", "dice-3", "door-open", "envelope"],
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

    num_flips = st.slider('Kaç kere para atmak istediğinizi seçiniz', 1, 100)
    sim1 = CoinFlipSimulation(num_flips)
    simulation_result = sim1.run_simulation
    heads, tails = simulation_result.get("heads"), simulation_result.get("tails")
    st.write("Simulasyon Sonuclari:")
    st.success(f"heads {heads}")
    st.success(f"tails: {tails}")
    st.warning(f"sum: {[heads + tails]}")

    arr = sim1.plot_normal_distribution
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

if selected == "Zar Simülasyonu":
    st.title(f"You have selected {selected}")
if selected == "Monty Hall Oyunu":
    st.title(f"You have selected {selected}")
if selected == "İletişim":
    st.title(f"You have selected {selected}")
