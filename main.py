import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#1-Veri Seti Yükleme
try:
    df = pd.read_csv('spam.csv', encoding='latin-1')
except FileNotFoundError:
    print("HATA: 'spam.csv' dosyası bulunamadı!")
    exit()

df = df[['v1', 'v2']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

#!!!Model, pek çok noktada yetersiz kaldı.Bu bağlamda manuel eğitim verileri verildi
yeni_veriler = [
    {'text': "Hello, click on the PDF below and take advantage of Amazon's great discounts.", 'label': 1},
    {'text': "Download the attached PDF to verify your account.", 'label': 1},
    {'text': "Amazon: Your order is on hold. Click link.", 'label': 1},
    {'text': "Urgent: PDF invoice attached. Please pay immediately.", 'label': 1},
    {'text': "Click here to view your Amazon discount.", 'label': 1}
]

yeni_df = pd.DataFrame(yeni_veriler)
df = pd.concat([df] + [yeni_df] * 1000, ignore_index=True)
print(f"Veri Seti Hazır! Toplam Mesaj: {len(df)}")
print("-" * 30)

#2-Model Eğitimi
vectorizer = TfidfVectorizer(ngram_range=(1, 2)) 
X = vectorizer.fit_transform(df['text'])
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Kayıt
print("Model güncelleniyor...")
joblib.dump(model, 'spam_detector_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("✅ Nükleer Model Kaydedildi.")
print("-" * 30)

#3-Hemen Test Et
print("\n--- TEST BAŞLIYOR ---")
test_cumlesi = "Hello, click on the PDF below and take advantage of Amazon's great discounts."
print(f"Cümle: {test_cumlesi}")

vec = vectorizer.transform([test_cumlesi])
tahmin = model.predict(vec)
oran = model.predict_proba(vec)[0][1] * 100

if tahmin[0] == 1:
    print(f"\n>>> SONUÇ: ⚠️  SPAM! (Güven: %{oran:.2f})")
    print(">>> TEBRİKLER! Sonunda yakaladık.")
else:
    print(f"\n>>> SONUÇ: Güvenli (Hata devam ediyor)")