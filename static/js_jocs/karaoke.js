// Karaoke sincronizado con lyrics_sync.json
let lyrics = [
  {
    "time": 6.38,
    "text": "Algo empieza hoy;"
  },
  {
    "time": 11.51,
    "text": "El día despierta despacio;"
  },
  {
    "time": 13.56,
    "text": "El cielo empieza a brillar"
  },
  {
    "time": 16.59,
    "text": "Hay un susurro en el aire;"
  },
  {
    "time": 19.11,
    "text": "Que me invita a esperar;"
  },
  {
    "time": 21.86,
    "text": "El mundo camina lento;"
  },
  {
    "time": 24.58,
    "text": "Mi corazón dice sí;"
  },
  {
    "time": 27.15,
    "text": "Algo bonito comienza;"
  },
  {
    "time": 30.39,
    "text": "Algo empieza Hoy aquí;"
  },
  {
    "time": 37.01,
    "text": "Espero tranquilo;"
  },
  {
    "time": 40.85,
    "text": "Con calma y con paz;"
  },
  {
    "time": 43.48,
    "text": "Jesús viene cerca;"
  },
  {
    "time": 45.99,
    "text": "Ya no tardará;"
  },
  {
    "time": 50.36,
    "text": "Espero tranquilo;"
  },
  {
    "time": 54.03,
    "text": "Con luz en mi interior;"
  },
  {
    "time": 58.95,
    "text": "Abro el corazón;"
  },
  {
    "time": 62.84,
    "text": "Algo empieza hoy;"
  },
  {
    "time": 74.37,
    "text": "Una luz pequeña se enciende;"
  },
  {
    "time": 77.73,
    "text": "Como una vela recta;"
  },
  {
    "time": 81.51,
    "text": "No hace ruido, no empuja;"
  },
  {
    "time": 83.6,
    "text": "Solo quiere acompañar;"
  },
  {
    "time": 85.98,
    "text": "Aprendo a mirar en silencio;"
  },
  {
    "time": 89.43,
    "text": "A escuchar con atención;"
  },
  {
    "time": 92.33,
    "text": "Cuando espero con confianza;"
  },
  {
    "time": 97.31,
    "text": "Habla más fuerte, amor;"
  },
  {
    "time": 104.03,
    "text": "Espero tranquilo;"
  },
  {
    "time": 107.8,
    "text": "Con calma y con paz;"
  },
  {
    "time": 111.2,
    "text": "Que si viene cerca;"
  },
  {
    "time": 117.38,
    "text": "Ya no tardará, espero tranquilo;"
  },
  {
    "time": 121.28,
    "text": "Con luz en mi interior;"
  },
  {
    "time": 126.84,
    "text": "Abro el corazón;"
  },
  {
    "time": 132.41,
    "text": "Algo empieza hoy;"
  },
  {
    "time": 136.5,
    "text": "No corro, no grito;"
  },
  {
    "time": 139.2,
    "text": "No tengo prisa hoy;"
  },
  {
    "time": 145.93,
    "text": "Espero en silencio y mi alma Dios;"
  },
  {
    "time": 156.51,
    "text": "Espero tranquilo, sentado aquí estoy;"
  },
  {
    "time": 161.65,
    "text": "Jesús viene a cerca, lo siento en mi voz;"
  },
  {
    "time": 166.01,
    "text": "Espero tranquilo;"
  },
  {
    "time": 169.88,
    "text": "Con todo mi ser;"
  },
  {
    "time": 174.75,
    "text": "Abro el corazón;"
  },
  {
    "time": 178.98,
    "text": "Y aprendo a esperar;"
  }
]

const audio = document.getElementById('karaoke-audio');
const lyricsDiv = document.getElementById('karaoke-lyrics');
const playBtn = document.getElementById('playBtn');
const pauseBtn = document.getElementById('pauseBtn');
const restartBtn = document.getElementById('restartBtn');

let currentIndex = -1;
let interval = null;

function updateLyrics() {
  if (!lyrics.length) return;
  const currentTime = audio.currentTime;
  // Buscar la última línea cuyo tiempo sea menor o igual al actual
  let idx = lyrics.length - 1;
  for (let i = 0; i < lyrics.length; i++) {
    if (currentTime < lyrics[i].time) {
      idx = i - 1;
      break;
    }
  }
  if (idx < 0) idx = 0;
  // Adelantar una línea
  if (idx < lyrics.length - 1) idx = idx + 1;
  if (idx !== currentIndex) {
    currentIndex = idx;
    renderLyrics(idx);
  }
}

function renderLyrics(activeIdx) {
  let html = '';
  for (let i = Math.max(0, activeIdx - 1); i <= Math.min(lyrics.length - 1, activeIdx + 1); i++) {
    html += `<div${i === activeIdx ? ' class="active"' : ''}>${lyrics[i].text}</div>`;
  }
  lyricsDiv.innerHTML = html;
}

function startSync() {
  if (interval) clearInterval(interval);
  interval = setInterval(updateLyrics, 100);
}
function stopSync() {
  if (interval) clearInterval(interval);
}

audio.addEventListener('play', startSync);
audio.addEventListener('pause', stopSync);
audio.addEventListener('ended', stopSync);
audio.addEventListener('seeked', updateLyrics);

playBtn.addEventListener('click', () => { audio.play(); });
pauseBtn.addEventListener('click', () => { audio.pause(); });
restartBtn.addEventListener('click', () => { audio.currentTime = 0; audio.play(); });

// Inicializa con la primera línea
lyricsDiv.innerHTML = '<div>...</div>';
