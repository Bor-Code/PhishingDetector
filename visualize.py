import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#1-Veriyi Oku
try:
    df = pd.read_csv('spam.csv', encoding='latin-1')
except:
    print("Dataset bulunamadı!")
    exit()
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

#2-Sadece SPAM mesajlar
spam_messages = df[df['label'] == 'spam']['text']
spam_text = " ".join(spam_messages)

#3-Kelime Bulutu
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(spam_text)

#4-Ekrana Çiz
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Eksenleri kapat
plt.title("Spam Mesajlarda En Çok Geçen Kelimeler", fontsize=20)
plt.show()