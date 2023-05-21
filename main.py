import numpy as np
from scipy.io.wavfile import write
from flask import Flask, render_template, send_file

app = Flask(__name__)


samplerate = 44100

def get_wave(freq, duration=1):
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0 
    
    return note_freqs
  
def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

@app.route("/a.wav")
def a():
  return send_file("static/a.wav")

@app.route("/A.wav")
def A():
  return send_file("static/A.wav")

@app.route("/B.wav")
def B():
  return send_file("static/B.wav")

@app.route("/c.wav")
def c():
  return send_file("static/c.wav")

@app.route("/C.wav")
def C():
  return send_file("static/C.wav")

@app.route("/d.wav")
def d():
  return send_file("static/d.wav")

@app.route("/D.wav")
def D():
  return send_file("static/D.wav")

@app.route("/E.wav")
def E():
  return send_file("static/E.wav")

@app.route("/f.wav")
def f():
  return send_file("static/f.wav")

@app.route("/F.wav")
def F():
  return send_file("static/F.wav")

@app.route("/g.wav")
def g():
  return send_file("static/g.wav")

@app.route("/G.wav")
def G():
  return send_file("static/G.wav")

@app.route("/")
def index():
  return render_template("index.html")

app.run(port=8080, host='0.0.0.0')

# octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
# for note in octave:
#   data = get_song_data(note)

#   data = data * (16300/np.max(data))

#   write(f'{note}.wav', samplerate, data.astype(np.int16))