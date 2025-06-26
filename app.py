from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)
    return jsonify({'download': download, 'upload': upload, 'ping': ping})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
