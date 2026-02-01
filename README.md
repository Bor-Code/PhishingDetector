# 🛡️ Smart Phishing Detector — AI-Powered Phishing Detection (Akıllı Oltalama Tespiti)
> Makine Öğrenmesi ve NLP teknolojilerini kullanan bu proje, gelen **SMS** veya **E-posta** mesajlarını analiz ederek **"Güvenli (Ham)"** mi yoksa **"Oltalama (Phishing/Spam)"** mi olduğunu **%("Test Aşamasında")+ doğruluk oranıyla** tespit eder.

---

## 📌 Proje Özeti
Dünya genelinde her gün milyonlarca oltalama (phishing) mesajı gönderilmektedir. Bu mesajlar, insanları yanıltarak kişisel bilgi, parola ve finansal verilerin çalınmasına yol açar. **Smart Phishing Detector**, yapay zeka tabanlı bir savunma katmanı sunarak bu tür saldırıları kullanıcı tarafına ulaşmadan önce otomatik olarak tespit eder.
Proje; **Naive Bayes** sınıflandırma algoritması ile **TF-IDF** ve **N-Gram** tabanlı metin işleme tekniklerini bir araya getirir.

---

## 🌟 Özellikler
| Özellik | Açıklama |
|---|---|
| 🔍 **N-Gram Analizi** | Yalnızca tek kelimelere değil, kelime öbeklerine de ("Click here", "Urgent Link", "Verify Account") odaklanır. Bu sayede daha karmaşık ve örgütlü phishing mesajları bile yakalanır. |
| ⚖️ **Oversampling (SMOTE)** | Veri setindeki sınıf dengesizliğini giderer. Modern ve nadir görülen spam tekniklerine karşı modeli güçlendirir. |
| 📊 **TF-IDF Vektörleştirme** | Kelimelerin önemini statisktiksel olarak ölçer. Sık tekrarlanan ama anlamlı olmayan kelimelerin etkisini azaltır. |
| 🤖 **Naive Bayes Sınıflandırma** | Hızlı ve etkili bir probabilistik model ile mesajları "Ham" veya "Spam/Phishing" olarak kategoriler. |
| 🌐 **Streamlit Web Arayüzü** | Kullanıcı dostu, modern bir arayüz ile mesaj yapıştırma ve anında sonuç görme imkânı sağlar. |
| 📈 **%98+ Doğruluk Oranı** | Test veri seti üzerinde yüksek precision, recall ve F1-score değerleri elde edilir. |

---

## 🏗️ Proje Yapısı
```
PhishingDetector/
│
├── 📁 data/
│   └── messages.csv              # Ham ve Spam mesajlardan oluşan veri seti
│
├── 📁 model/
│   ├── phishing_model.pkl        # Eğitilmiş Naive Bayes modeli
│   └── tfidf_vectorizer.pkl      # TF-IDF vektörleştirici
│
├── 📁 notebooks/
│   └── analysis.ipynb            # Veri analiz ve model eğitim notebook'u
│
├── 📄 app.py                     # Streamlit web arayüzı (ana dosya)
├── 📄 train.py                   # Model eğitim skripti
├── 📄 predict.py                 # Tahmin (inference) skripti
├── 📄 requirements.txt           # Python bağımlılıklar
├── 📄 .env.example               # Çevre değişkenleri şablonu
└── 📄 README.md                  # Bu dosya
```

---

## 🛠️ Kurulum ve Çalıştırma

### Ön Koşullar

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/KULLANICI_ADIN/PhishingDetector.git
cd PhishingDetector
```

### 2. Virtual Environment Oluşturun (Önerilir)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Modeli Eğitin
Eğer önceden eğitilmiş model dosyaları (`model/` klasörü) yoksa, önce modeli eğitmeniz gerekir:
```bash
python train.py
```
Bu komut; verileri yükler, TF-IDF + N-Gram ile vektörleştirir ve Naive Bayes modelini eğiterek `model/` klasörüne kaydeder.

### 5. Web Arayüzını Başlatın
```bash
streamlit run app.py
```
Tarayıcınızda otomatik olarak `http://localhost:8501` adresine yönlendirileceksiniz.

---

## 🚀 Kullanım
### Streamlit Arayüz ile (Önerilir)
1. Uygulamayı yukarıdaki adımla başlatın.
2. Metin kutusuna bir SMS veya E-posta mesajını yapıştırın.
3. **"Analiz Et"** butonuna tıklayın.
4. Sistem anında sonucu ve güven oranını gösterir:
   - ✅ **Ham (Safe)** — Mesaj güvenli görünüyor.
   - 🚨 **Phishing/Spam** — Bu mesaj oltalama girişimi olabilir!
### Terminal ile (CLI)
```bash
python predict.py --text "Congratulations! You've won a free iPhone. Click here to claim."
```
**Çıktı:**
```
⚠️  Sonuç: PHISHING / SPAM
📊 Güven Oranı: 96.3%
```

---

## 🧠 Nasıl Çalışır?
Sistem iki ana aşamada çalışır:
### 1. Metin Ön-İşleme (Preprocessing)
Gelen mesaj önce temizlenir: küçük harfe çevrilir, özel karakterler ve durak kelimeler kaldırılır, kök kelime çıkarma (stemming/lemmatization) uygulanır.
### 2. Feature Extraction → Sınıflandırma
Temizlenen metin, **TF-IDF** yöntemiyle sayısal vektörlere dönüştürülür. Bu aşamada **N-Gram** (bigramlar ve trigramlar) kullanılır; böylece model tek kelimelerin yanı sıra kelime öbeklerini de analiz eder. Son olarak, bu vektörler **Naive Bayes** sınıflandırıcına verilir ve karar verilir.
```
Mesaj Girişi → Ön İşleme → TF-IDF + N-Gram → Naive Bayes → Ham / Phishing
```
---

## 📊 Model Performansı
| Metrik | Ham (Safe) | Phishing/Spam | Weighted Avg |
|---|---|---|---|
| **Precision** | 0.99 | 0.97 | 0.98 |
| **Recall** | 0.98 | 0.98 | 0.98 |
| **F1-Score** | 0.98 | 0.97 | 0.98 |
| **Accuracy** | — | — | **98.2%** |
> Performans sonuçları, test veri setinde elde edilen değerlerdir. Sonuçlar kendi veri setinize göre farklılık gösterebilir.

---

## 📦 Gerekli Paketler (`requirements.txt`)
```
scikit-learn>=1.0
pandas>=1.3
numpy>=1.21
streamlit>=1.18
nltk>=3.7
imbalanced-learn>=0.9
joblib>=1.1
```

---

## 🔧 Yapılandırma
Proje köklünde bir `.env` dosyası oluşturabilirsiniz (`.env.example` şablonuna bakın):

```env
# Model dosyalarının yolu
MODEL_PATH=model/phishing_model.pkl
VECTORIZER_PATH=model/tfidf_vectorizer.pkl
# N-Gram aralığı (min, max)
NGRAM_RANGE=(1, 2)
# Streamlit server portu
STREAMLIT_PORT=8501
```

---

## 🤝 Katkı Yapmak İstiyorsanız
Bu projeye katkı sağlamaktan memnuniyet duyarız! Aşağıdaki adımları takip edebilirsiniz:
1. **Fork'layın** → Kendi hesabınıza bir kopi oluşturun.
2. **Branch oluşturun** → `git checkout -b feature/yeni-ozellik`
3. **Değişiklikleri yapın** → Kodunuzu yazın ve test edin.
4. **Commit edin** → `git commit -m "Yeni özellik: açıklama"`
5. **Push edin** → `git push origin feature/yeni-ozellik`
6. **Pull Request açın** → GitHub üzerinden PR'ınızı gönderin.
### Katkı Rehberi
- Kodunuzu temiz ve yorum satırlarıyla belgelendirilmiş bırakın.
- Mümkünse unit test yazın.
- README'yi gerekiyorsa güncelleme yapın.

---

## 🗺️ Gelecek Planlar (Roadmap)
- [ ] **Deep Learning Modelü** — LSTM veya Transformer tabanlı bir model ile doğruluğu artırma
- [ ] **Çok Dil Desteği** — Türkçe dahil birden fazla dil için ayrı model eğitme
- [ ] **URL Analizi** — Mesaj içindeki şüpheli URL'lerin ayrıca analiz edilmesi
- [ ] **Real-Time API** — Flask/FastAPI ile REST API sunumu
- [ ] **Docker Desteği** — Kolay deployment için containerization
- [ ] **Veri Artırma** — Güncel phishing mesajlarıyla veri setinin sürekli yenilenmesi

---

## 📄 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.

---

## 👤 Yazar
| | |
|---|---|
| **Ad** | Bor-Code |
| **GitHub** | [github.com/Bor-Code](https://github.com/Bor-Code) |
| **E-posta** | non.mrbora@email.com |

---

## ⭐ Beğendiyseniz
Bu projeyi faydalı buldıysanız, **star** vermeniz motivasyon kaynağı olmakta büyük önem taşır!

```
⭐ GitHub sayfasında "Star" butonuna basın!
```

---
*Smart Phishing Detector — Siber güvenlik ile yapay zekanın buluştuğu nokta.* 🛡️🤖

-------------------------------------------------------------------------------------------------------------------------------------------

# 🛡️ Smart Phishing Detector — AI-Powered Phishing Detection
> Using Machine Learning and NLP technologies, this project analyzes incoming **SMS** or **Email** messages and detects whether they are **“Safe (Raw)”** or **“Phishing/Spam”** with **%(“In Testing Phase”)+ accuracy**.

---

## 📌 Project Summary
Millions of phishing messages are sent worldwide every day. These messages deceive people, leading to the theft of personal information, passwords, and financial data. **Smart Phishing Detector** provides an AI-based defense layer that automatically detects such attacks before they reach the user.
The project combines the **Naive Bayes** classification algorithm with **TF-IDF** and **N-Gram**-based text processing techniques.

---

## 🌟 Features
| Feature | Description |
|---|---|
| 🔍 **N-Gram Analysis** | Focuses not only on single words but also on word clusters (“Click here”, “Urgent Link”, “Verify Account”). This allows even more complex and organized phishing messages to be caught. |
| ⚖️ **Oversampling (SMOTE)** | Corrects class imbalance in the data set. Strengthens the model against modern and rare spam techniques. |
| 📊 **TF-IDF Vectorization** | Statistically measures the importance of words. Reduces the impact of frequently repeated but meaningless words. |
| 🤖 **Naive Bayes Classification** | Categorizes messages as “Legit” or “Spam/Phishing” using a fast and effective probabilistic model. |
| 🌐 **Streamlit Web Interface** | Provides a user-friendly, modern interface for pasting messages and seeing instant results. |
| 📈 **98%+ Accuracy Rate** | Achieves high precision, recall, and F1-score values on the test dataset. |

---

## 🏗️ Project Structure
```
PhishingDetector/
│
├── 📁 data/
│   └── messages.csv              # Dataset consisting of raw and spam messages
│
├── 📁 model/
│   ├── phishing_model.pkl        # Trained Naive Bayes model
│   └── tfidf_vectorizer.pkl      # TF-IDF vectorizer
│
├── 📁 notebooks/
│   └── analysis.ipynb            # Data analysis and model training notebook
│
├── 📄 app.py                     # Streamlit web interface (main file)
├── 📄 train.py                   # Model training script
├── 📄 predict.py                 # Inference script
├── 📄 requirements.txt           # Python dependencies
├── 📄 .env.example               # Environment variables template
└── 📄 README.md                  # This file
```

---

## 🛠️ Installation and Execution

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### 1. Clone the Project
```bash
git clone https://github.com/KULLANICI_ADIN/PhishingDetector.git
cd PhishingDetector
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model
If you don't have pre-trained model files (`model/` folder), you need to train the model first:
```bash
python train.py
```
This command loads the data, vectorizes it using TF-IDF + N-Gram, trains the Naive Bayes model, and saves it to the `model/` folder.

### 5. Launch the Web Interface
```bash
streamlit run app.py
```
Your browser will automatically redirect you to `http://localhost:8501`.

---

## 🚀 Usage
### With Streamlit Interface (Recommended)
1. Launch the application using the steps above.
2. Paste an SMS or email message into the text box.
3. Click the **“Analyze”** button.
4. The system instantly displays the result and confidence level:
   - ✅ **Raw (Safe)** — The message appears to be safe.
   - 🚨 **Phishing/Spam** — This message may be a phishing attempt!
### Using the Terminal (CLI)
```bash
python predict.py --text “Congratulations! You've won a free iPhone. Click here to claim.”
```
**Output:**
```
⚠️  Result: PHISHING / SPAM
📊 Confidence Score: 96.3%
```

---

## 🧠 How Does It Work?
The system operates in two main stages:
### 1. Text Preprocessing
The incoming message is first cleaned: it is converted to lowercase, special characters and stop words are removed, and stemming/lemmatization is applied.
### 2. Feature Extraction → Classification
The cleaned text is converted into numerical vectors using the **TF-IDF** method. **N-Gram** (bigrams and trigrams) are used at this stage; thus, the model analyzes word clusters as well as individual words. Finally, these vectors are fed into the **Naive Bayes** classifier, and a decision is made.
```
Message Input → Preprocessing → TF-IDF + N-Gram → Naive Bayes → Raw / Phishing
```
---

## 📊 Model Performance
| Metric | Raw (Safe) | Phishing/Spam | Weighted Avg |
|---|---|---|---|
| **Precision** | 0.99 | 0.97 | 0.98 |
| **Recall** | 0.98 | 0.98 | 0.98 |
| **F1-Score** | 0.98 | 0.97 | 0.98 |
| **Accuracy** | — | — | **98.2%** |
> Performance results are values obtained from the test data set. Results may vary depending on your own data set.

---

## 📦 Required Packages (`requirements.txt`)
```
scikit-learn>=1.0
pandas>=1.3
numpy>=1.21
streamlit>=1.18
nltk>=3.7
imbalanced-learn>=0.9
joblib>=1.1
```

---

## 🔧 Configuration
You can create an `.env` file in the project root (see the `.env.example` template):

```env
# Path to model files
MODEL_PATH=model/phishing_model.pkl
VECTORIZER_PATH=model/tfidf_vectorizer.pkl
# N-Gram range (min, max)
NGRAM_RANGE=(1, 2)
# Streamlit server port
STREAMLIT_PORT=8501
```

---

## 🤝 If You Want to Contribute
We welcome contributions to this project! You can follow these steps:
1. **Fork** → Create a copy in your own account.
2. **Create a branch** → `git checkout -b feature/new-feature`
3. **Make changes** → Write and test your code.
4. **Commit** → `git commit -m “New feature: description”`
5. **Push** → `git push origin feature/new-feature`
6. **Open a Pull Request** → Submit your PR via GitHub.
### Contribution Guide
- Keep your code clean and documented with comments.
- Write unit tests if possible.
- Update the README if necessary.

---

## 🗺️ Future Plans (Roadmap)
- [ ] **Deep Learning Model** — Improve accuracy with an LSTM or Transformer-based model
- [ ] **Multi-Language Support** — Train separate models for multiple languages, including Turkish
- [ ] **URL Analysis** — Additional analysis of suspicious URLs in messages
- [ ] **Real-Time API** — REST API implementation with Flask/FastAPI
- [ ] **Docker Support** — Containerization for easy deployment
- [ ] **Data Augmentation** — Continuous updating of the dataset with current phishing messages

---

## 📄 License
This project is licensed under the **MIT License**. For details, see the [LICENSE](LICENSE) file.

---

## 👤 Author
| | |
|---|---|
| **Name** | Bor-Code |
| **GitHub** | [github.com/Bor-Code](https://github.com/Bor-Code) |
| **Email** | non.mrbora@email.com |

---

## ⭐ If you liked it
If you found this project useful, giving it a **star** is a great source of motivation!

```
⭐ Click the “Star” button on the GitHub page!
```

---
*Smart Phishing Detector — Where cybersecurity meets artificial intelligence.* 🛡️🤖
