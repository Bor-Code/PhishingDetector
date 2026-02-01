import streamlit as st
import joblib

#1-Modeli Geri Getir
@st.cache_resource
def load_model():
    try:
        model = joblib.load('spam_detector_model.pkl')
        vectorizer = joblib.load('vectorizer.pkl')
        return model, vectorizer
    except:
        return None, None
model, vectorizer = load_model()

#2-Sayfa Tasarım
st.title("🕵️‍♂️ Yapay Zeka Phishing Dedektörü")
st.write("Aşağıdaki kutuya şüpheli bir mesaj yapıştırın.")
st.sidebar.title("⚠️DİKKAT⚠️")
st.sidebar.info("Yapay zeka modeli eğitim aşamasındadır.Lütfen yanıtınız kontrol doğrulamasını yapın!")

#!!!Eğer model dosyaları yoksa uyarı ver
if model is None:
    st.error("HATA: Model dosyaları (.pkl) bulunamadı! Lütfen önce main.py dosyasını çalıştırın.")
else:
#3-Kullanıcı
    user_input = st.text_area("Mesajı Buraya Girin:", height=100)
    if st.button("ANALİZ ET"):
        if user_input:
            input_vec = vectorizer.transform([user_input])
            prediction = model.predict(input_vec)
            if prediction[0] == 1:
                st.error("🚨 DİKKAT! Bu mesaj OLTALAMA (Phishing) olabilir!")
            else:
                st.success("✅ GÜVENLİ. Bu mesaj temiz görünüyor.")
                st.balloons()
        else:
            st.warning("Lütfen önce bir metin girin.")