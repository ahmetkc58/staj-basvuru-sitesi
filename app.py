from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import json

app = Flask(__name__, template_folder='.')  # Ana klasörü template klasörü olarak ayarla
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Mail taslağını oku
with open('mail-taslağı.md', 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

# Gmail bilgileri
GMAIL = ""
PASSWORD = ""
CV_PATH = ""

# İstatistikleri yükle
STATS_FILE = 'stats.json'

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    return {'sent': 0, 'failed': 0}

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f)

@app.route('/')
def index():
    stats = load_stats()
    return render_template('index.html', template=TEMPLATE, stats=stats)

@app.route('/get_stats')
def get_stats():
    stats = load_stats()
    return jsonify(stats)

@app.route('/set_credentials', methods=['POST'])
def set_credentials():
    global GMAIL, PASSWORD
    data = request.json
    GMAIL = data.get('email', '')
    PASSWORD = data.get('password', '')
    
    if not GMAIL or not PASSWORD:
        return jsonify({'success': False, 'message': 'Email ve şifre gerekli!'}), 400
    
    return jsonify({'success': True, 'message': 'Bilgiler kaydedildi!'})

@app.route('/get_template')
def get_template():
    return jsonify({'template': TEMPLATE})

@app.route('/save_template', methods=['POST'])
def save_template():
    global TEMPLATE
    data = request.json
    new_template = data.get('template', '')
    
    try:
        # Dosyaya kaydet
        with open('mail-taslağı.md', 'w', encoding='utf-8') as f:
            f.write(new_template)
        TEMPLATE = new_template
        return jsonify({'success': True, 'message': 'Taslak kaydedildi!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/upload_cv', methods=['POST'])
def upload_cv():
    global CV_PATH
    if 'cv' not in request.files:
        return jsonify({'success': False, 'message': 'CV dosyası seçilmedi'}), 400
    
    file = request.files['cv']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'Dosya seçilmedi'}), 400
    
    if file:
        filename = 'uploaded_cv.pdf'
        filepath = os.path.join(os.getcwd(), filename)
        file.save(filepath)
        CV_PATH = filepath
        return jsonify({'success': True, 'message': 'CV yüklendi!', 'path': filepath})

@app.route('/send', methods=['POST'])
def send_email():
    data = request.json
    company_name = data.get('company_name')
    email = data.get('email')
    
    if not company_name or not email:
        return jsonify({'success': False, 'message': 'Şirket adı ve mail gerekli!'}), 400
    
    # Gmail bilgilerini kontrol et
    if not GMAIL or not PASSWORD:
        return jsonify({'success': False, 'message': 'Önce Gmail bilgilerinizi girin!'}), 400
    
    try:
        # Mail içeriğini hazırla
        body = TEMPLATE.replace("[ŞİRKET ADI]", company_name)
        
        # Mail oluştur
        msg = MIMEMultipart()
        msg['From'] = GMAIL
        msg['To'] = email
        msg['Subject'] = "Uzun Dönem Staj Başvurusu - Ahmet Koç"
        
        html = body.replace('\n', '<br>')
        msg.attach(MIMEText(html, 'html', 'utf-8'))
        
        # CV ekle (sadece bir kez oku)
        if CV_PATH and os.path.exists(CV_PATH):
            with open(CV_PATH, 'rb') as f:
                cv = MIMEApplication(f.read(), _subtype="pdf")
                cv.add_header('Content-Disposition', 'attachment', filename='Ahmet_Koc_CV.pdf')
                msg.attach(cv)
        
        # Hızlı SMTP gönderimi (debug kapalı)
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as server:
            server.starttls()
            server.login(GMAIL, PASSWORD)
            server.send_message(msg)
        
        # İstatistikleri güncelle
        stats = load_stats()
        stats['sent'] += 1
        save_stats(stats)
        
        print(f"[✓] {company_name} -> {email}")
        return jsonify({'success': True, 'message': f'✅ {company_name} şirketine gönderildi!', 'stats': stats})
    
    except Exception as e:
        # İstatistikleri güncelle
        stats = load_stats()
        stats['failed'] += 1
        save_stats(stats)
        
        print(f"[✗] {company_name} -> {email}: {str(e)}")
        return jsonify({'success': False, 'message': f'Hata: {str(e)}', 'stats': stats}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
