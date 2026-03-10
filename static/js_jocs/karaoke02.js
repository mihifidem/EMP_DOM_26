// Karaoke sincronizado con lyrics_sync.json
let lyrics = [
  {
    "time": 17.41,
    "text": "El camino se ilumina;"
  },
  {
    "time": 20.79,
    "text": "Con la luz de tu venida;"
  },
  {
    "time": 24.08,
    "text": "El desierto florecerá;"
  },
  {
    "time": 27.74,
    "text": "Y tu amor nos guiará;"
  },
  {
    "time": 32.71,
    "text": "Preparamos el corazón;"
  },
  {
    "time": 36.68,
    "text": "Como tierra buena en flor;"
  },
  {
    "time": 40.25,
    "text": "Para escuchar tu voz;"
  },
  {
    "time": 45.21,
    "text": "Y seguir tu canción;"
  },
  {
    "time": 53.84,
    "text": "Ven Señor no tardes más;"
  },
  {
    "time": 61.63,
    "text": "Que tu pueblo te espera ya;"
  },
  {
    "time": 69.14,
    "text": "Con esperanza y fe;"
  },
  {
    "time": 75.83,
    "text": "Nuestro canto es para ti;"
  },
  {
    "time": 83.65,
    "text": "Las montañas se allanarán;"
  },
  {
    "time": 87.46,
    "text": "Los valles se levantarán;"
  },
  {
    "time": 90.84,
    "text": "Proclamando tu verdad;"
  },
  {
    "time": 94.76,
    "text": "Que es camino y libertad;"
  },
  {
    "time": 99.87,
    "text": "Preparamos el corazón;"
  },
  {
    "time": 103.53,
    "text": "Como tierra buena en flor;"
  },
  {
    "time": 107.24,
    "text": "Para escuchar tu voz;"
  },
  {
    "time": 113.39,
    "text": "Y seguir tu canción;"
  },
  {
    "time": 119.75,
    "text": "Ven Señor no tardes más;"
  },
  {
    "time": 127.3,
    "text": "Que tu pueblo te espera ya;"
  },
  {
    "time": 134.62,
    "text": "Con esperanza y fe;"
  },
  {
    "time": 140.7,
    "text": "Nuestro canto es para ti;"
  },
  {
    "time": 179.62,
    "text": "Ven Señor no tardes más;"
  },
  {
    "time": 187.25,
    "text": "Que tu pueblo te espera ya;"
  },
  {
    "time": 193.65,
    "text": "Con esperanza y fe;"
  },
  {
    "time": 203.76,
    "text": "Nuestro canto es para ti;"
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
