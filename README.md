# Modern AI Chat Aplikacija

## ✅ Trenutno Implementirano
- Chat funkcionalnost sa OpenAI integracijom
- Streaming odgovora u realnom vremenu
- Kompletan UI sa QML
- Sistem za upravljanje sesijama
- Perzistencija podataka u JSON formatu
- Podrška za više chat sesija

## 🔄 Poznati Problemi
1. UI greška pri pristupu undefined vrednostima u ChatView.qml
2. Nedostaje obrada grešaka na UI nivou
3. Model selektor nije povezan sa backend-om
4. Brisanje sesija nije potpuno implementirano

## 📋 Sledeći Koraci
1. Implementirati error handling
2. Povezati model selector
3. Dodati loading indikatore
4. Implementirati pretragu sesija
5. Dodati export/import funkcionalnost

## 🔄 Poslednje Izmene
1. Centralizovano čuvanje sesija u root sessions.json
2. Stabilizovan rad sa sesijama
3. Dodat detaljniji logging
4. Rešeni problemi sa crash-om aplikacije

## 🎯 Trenutna Struktura
```
├── .env                    # Environment varijable (OpenAI API ključ)
├── README.md              # Dokumentacija projekta
├── current_structure.txt  # Ovaj fajl
├── generate_structure.py  # Helper skripta
├── sessions.json         # Centralni fajl za čuvanje sesija
└── src/
    ├── __init__.py       # Python paket marker
    ├── api/
    │   ├── __init__.py   # API paket marker
    │   └── openai_client.py  # OpenAI API klijent
    ├── ui/
    │   ├── __init__.py   # UI paket marker
    │   ├── chat_bridge.py # Most između Python i QML
    │   ├── qml_test.py   # Glavni Python fajl
    │   └── qml/
    │       ├── ChatView.qml      # Glavni QML UI
    │       └── MessageDelegate.qml # Komponenta za poruke
    └── utils/            # Direktorijum za pomoćne funkcije

```

### 2️⃣ Faza: UI Komponente
Dodati u postojeći ChatView.qml:
- [ ] Sidebar panel (260px širina)
  - [ ] Logo sekcija (50-60px visina)
  - [ ] "New Chat" dugme (44px visina)
  - [ ] Lista sesija
  - [ ] Settings dugme
- [ ] Header (48-50px)
  - [ ] Naziv sesije
  - [ ] Export/Pin dugmad

### 3️⃣ Faza: Settings
Implementirati u postojeći kod:
- [ ] API podešavanja
  - [ ] Model dropdown
  - [ ] Temperature slider
  - [ ] Max tokens input
- [ ] UI podešavanja
  - [ ] Dark/Light tema
  - [ ] Font veličina

## 🎨 UI Specifikacije

### Dimenzije
- Glavni prozor: 800x600px (minimum)
- Sidebar: 260px širina
- Header: 48-50px visina
- Input: 48-60px visina
- Avatari: 30x30px
- Dugmad: 44px visina

### Boje
- Sidebar: #202123 (dark)
- Pozadina: #ffffff / #1f1f1f
- User poruke: #007AFF
- AI poruke: #f7f7f8
- Borderi: #e5e7eb
- Disabled: #6B7280

### Responzivnost
- Breakpoint: 800px
- Ispod 800px: sakrivanje sidebara
- Touch support na mobilnom

## 💾 Storage Plan
- SQLite za sesije
- JSON export/import
- Struktura:
  ```json
  {
    "sessionId": "uuid",
    "title": "Naziv sesije",
    "messages": [
      {
        "role": "user/ai",
        "content": "tekst",
        "timestamp": "HH:MM"
      }
    ]
  }
  ```

## 🔧 Tehnički Detalji

### OpenAI API
- Model: GPT-4/3.5
- Temperature: 0.7 default
- Max tokens: 2000 default
- Stream: true

### Error Handling
- Rate limits (3500 req/min)
- Timeout (30s)
- Network errors
- Invalid API key

## 📈 Sledeći Koraci

1. Implementirati sidebar u postojeći ChatView.qml
2. Dodati session management u chat_bridge.py
3. Implementirati settings sistem
4. Dodati dark/light temu

## 🐛 Known Issues
1. Fale ikonice za akcije
2. Nema error handling za API
3. Nedostaje session management
4. Responsive design nije implementiran

## 💡 Development Tips
- Koristiti postojeću strukturu
- Pratiti QML best practices
- Testirati na različitim veličinama ekrana
