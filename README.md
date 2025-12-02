# Day 7 – Tiny Intent Classifier (Rule + Similarity)

Çok basit bir niyet sınıflandırıcı:
- greeting
- weather
- help
- other

Ana fikir: önce keyword, sonra TF-IDF cosine ile en yakın örneği bul.

Kurulum ve çalıştırma:

```bash
pip install -r requirements.txt
python intent_cli.py
```
