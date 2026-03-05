# 🎓 Öğrenci Sınav Notu Tahminleme (Student Performance Predictor)

Bu proje, öğrencilerin çalışma alışkanlıkları ve demografik verilerini analiz ederek sınav sonuçlarını tahmin eden bir **Makine Öğrenmesi (Machine Learning)** projesidir. Model, **FastAPI** kullanılarak bir web servisi haline getirilmiş ve **Render** üzerinde yayına alınmıştır.

🚀 **Canlı Uygulama:** [Buraya Tıkla](https://examgradeprediction.onrender.com/)

---

## 🛠️ Kullanılan Teknolojiler

* **Programlama Dili:** Python 3.11
* **Makine Öğrenmesi:** Scikit-learn, NumPy, Pandas
* **Web Framework:** FastAPI, Uvicorn
* **Arayüz:** HTML5, Jinja2 (Templating)
* **Deployment:** GitHub & Render

---

## 📊 Proje Hakkında

Bu uygulama, makine öğrenmesinde **Lineer Regresyon** (veya hangi algoritmayı kullandıysan onu yazabilirsin) algoritmasını kullanarak şu parametrelere göre not tahmini yapar:
* Haftalık Çalışma Saatleri
* Önceki Sınav Notları
* Okul Katılım Oranı
* Sosyal Faaliyetler vb.

### 🏗️ Proje Mimarisi

1.  **Veri Analizi:** Veri seti Pandas ile temizlendi ve analiz edildi.
2.  **Model Eğitimi:** Scikit-learn kullanılarak model eğitildi ve `.pkl` formatında kaydedildi.
3.  **API Geliştirme:** FastAPI ile modelin tahmin yapabileceği bir uç nokta (endpoint) oluşturuldu.
4.  **Deployment:** GitHub deposu Render'a bağlanarak CI/CD (Sürekli Dağıtım) sağlandı.

---

## 💻 Yerel Kurulum (Local Setup)

Projeyi kendi bilgisayarınızda çalıştırmak için:

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/RuveydaArslan/ExamGradePrediction.git](https://github.com/RuveydaArslan/ExamGradePrediction.git)
   
## Gerekli kütüphaneleri kurun
  pip install -r requirements.txt

## Uygulamayı başlatın
  uvicorn app:app --reload
  
