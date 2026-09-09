from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Downloader Social Media</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7f6; text-align: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 400px; }
        input[type="text"] { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #028090; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold; }
        button:hover { background: #026670; }
        .info { margin-top: 15px; color: #555; font-size: 14px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Descargador de Videos 📥</h2>
        <p class="info">YouTube, Instagram, TikTok, Facebook, LinkedIn</p>
        <form action="/download" method="post">
            <input type="text" name="url" placeholder="Pega el enlace del video aquí" required>
            <br><br>
            <button type="submit">Descargar Video</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'format': 'b/best/bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'quiet': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            base, _ = os.path.splitext(filename)
            final_filename = f"{base}.mp4" if os.path.exists(f"{base}.mp4") else filename
            return send_file(final_filename, as_attachment=True)
    except Exception as e:
        return f"<h3>Error al procesar el video: {str(e)}</h3>", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)