from flask import Flask, render_template, request, send_file
import yt_dlp as youtube_dl
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {
        'format': 'best',
        'outtmpl':  os.path.join(os.getenv('HOME', os.getenv('USERPROFILE')), 'downloads', '%(title)s.%(ext)s')
    }
    
    if not os.path.exists(os.path.join(os.getenv('HOME', os.getenv('USERPROFILE')), 'downloads')):
        os.makedirs(os.path.join(os.getenv('HOME', os.getenv('USERPROFILE')), 'downloads'))

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            return 'f"Error de descarga {str(e)}"'
        
    return "Su video se esta descargando"

if __name__ == '__main__':
    app.run(debug=True)