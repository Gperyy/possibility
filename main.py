import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Yazı/Tura", "Zar Simülasyonu", "Monty Hall Oyunu", "Concat"],
                  icons=["coin", "dice-5-fill", "door-open", "envelope"],
                  menu_icon="cast", default_index=0,
                  orientation="horizontal")
    selected
#mark_delete
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


def load_lottieurl(url: str) -> object:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ana baslik
st.title('OLASILIK DÜNYASINA GİRİŞ 🧮 ')
# alt baslik
st.subheader("Olasılık Kuramı Nasıl Ortaya Çıkmıştır? ")
# text

st.markdown("Olasılık kuramı, 17. yüzyılın ortalarından itibaren gelişmeye başlamıştır. Öncelikle Fransız matematikçi "
            "Blaise Pascal ve Pierre de Fermat tarafından olasılık kuramının temelleri atılmıştır. Pascal ve Fermat, "
            "birçok matematik problemi çözmek için olasılık kuramını kullanmaya başlamışlardır. Örneğin, Fermat, "
            "bir kâğıt oyununda kazanma olasılığını hesaplamak için olasılık kuramını kullanmıştır.")
st.markdown("I. yüzyılın sonlarına doğru, olasılık kuramı, özellikle Fransa'da, birçok matematikçi tarafından daha "
            "ayrıntılı olarak incelenmeye başlandı. Bu çalışmalar, olasılık kuramının daha geniş bir alana "
            "uygulanabileceğini göstermiştir. Örneğin, 18. yüzyılda İsveçli matematikçi Anders Johann Lindström, "
            "olasılık kuramının tahmin ve istatistik alanlarında kullanılabileceğini göstermiştir.")
st.markdown("II. yüzyılda, İngiliz matematikçi Thomas Bayes, olasılık kuramınıntemelini oluşturan Bayes Teoremi'ni "
            "ortaya attı. Bu teoremi, olaylar arasındaki ilişkileri ve olasılıkları modellemek için kullanılır. 20. "
            "yüzyılın başlarında, olasılık kuramı ve istatistik alanlarındaki çalışmalar hızlandı ve bugün olasılık "
            "kuramı ve istatistik, birçok alanda kullanılmaktadır.")

# animasyon
lottie_question = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_u7yrcwlk.json")
st_lottie(
    lottie_question,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    height=200
)

# text2
st.markdown("Belirli bir olay A için olasılık P(A) 0 ile 1 arasında değişen bir sayı ile temsil edilir.Hiç olanaksız "
            "bir olay için olasılık 0 olur ve kesinlikle olacak bir olayın olasılığı 1 olur. Bazı istatikçicler bu "
            "uçsal olasılık değerlerinin sadece teorik olduğunu iddia etmektedirler çünkü kabul ettikleri olasılık "
            "açıklaması deneylemelerle limitte göresel çoklukluk (relatif frekans) değerine dayanır.Diğer Bayes-tipi, "
            "özellikle, olasılık açıklamasına göre bu uçsal olasılık değerlerini sübjektif olarak düşünmek ve "
            "olaylara bu değeleri koymak imkan dahilindedir.")
import os
import site
import glob

site_packages = site.getsitepackages()
for site_package in site_packages:
    option_menu_js = os.path.join(site_package, "streamlit_option_menu/frontend/dist/js/*.js")
    js_files = glob.glob(option_menu_js)
    for js_file in js_files:
        with open(js_file, "r") as filein:
            contents = filein.read()
        mod_contents = contents.replace("href:\"#\"", "href:\"#dummy\"")
        with open(js_file, "w") as fileout:
            fileout.write(mod_contents)