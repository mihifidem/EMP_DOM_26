// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {}
  {
    "time": 23.34,
    "text": "En esta casa hay amor"
  },
  {
    "time": 28.56,
    "text": "En una casa pequeña"
  },
  {
    "time": 33.1,
    "text": "Sencilla como las demás"
  },
  {
    "time": 38.67,
    "text": "Dios aprendió cada día"
  },
  {
    "time": 43.46,
    "text": "A crecer, reír y amar"
  },
  {
    "time": 48.79,
    "text": "José cuidaba en silencio"
  },
  {
    "time": 53.23,
    "text": "María enseñaba a confiar"
  },
  {
    "time": 58.52,
    "text": "Y Jesús, siendo tan niño"
  },
  {
    "time": 63.36,
    "text": "Aprendió lo que es amar"
  },
  {
    "time": 68.11,
    "text": "En esta casa hay amor"
  },
  {
    "time": 72.93,
    "text": "Hay cuidado y hay perdón"
  },
  {
    "time": 78.63,
    "text": "Dios vive cuando nos queremos"
  },
  {
    "time": 80.72,
    "text": "Con el corazón"
  },
  {
    "time": 88.29,
    "text": "En esta casa hay amor"
  },
  {
    "time": 92.83,
    "text": "Aunque todo no esté bien"
  },
  {
    "time": 98.42,
    "text": "Cuando nos cuidamos juntos"
  },
  {
    "time": 100.43,
    "text": "Dios vive también"
  },
  {
    "time": 108.57,
    "text": "No todo era siempre fácil"
  },
  {
    "time": 113.04,
    "text": "También hubo miedo y dolor"
  },
  {
    "time": 118.46,
    "text": "Pero cuando iban unidos"
  },
  {
    "time": 122.9,
    "text": "Hablaba más fuerte el amor"
  },
  {
    "time": 128.27,
    "text": "Cada gesto pequeño"
  },
  {
    "time": 133.29,
    "text": "Cada abrazo de verdad"
  },
  {
    "time": 138.41,
    "text": "Hace de cualquier familia"
  },
  {
    "time": 143.96,
    "text": "Un lugar donde Dios está"
  },
  {
    "time": 148.35,
    "text": "En esta casa hay amor"
  },
  {
    "time": 153.33,
    "text": "Hay cuidado y hay perdón"
  },
  {
    "time": 158.4,
    "text": "Dios vive cuando nos queremos"
  },
  {
    "time": 160.61,
    "text": "Con el corazón"
  },
  {
    "time": 168.38,
    "text": "En esta casa hay amor"
  },
  {
    "time": 172.84,
    "text": "Aunque todo no esté bien"
  },
  {
    "time": 178.37,
    "text": "Cuando nos cuidamos juntos"
  },
  {
    "time": 180.53,
    "text": "Dios vive también"
  },
  {
    "time": 183.33,
    "text": "Cuidar"
  },
  {
    "time": 184.24,
    "text": "Escuchar"
  },
  {
    "time": 190.75,
    "text": "Amar cada día más"
  },
  {
    "time": 198.35,
    "text": "En esta casa hay amor"
  },
  {
    "time": 203.35,
    "text": "Abre el tuyo también"
  },
  {
    "time": 208.38,
    "text": "Que Jesús crece despacio"
  },
  {
    "time": 211.29,
    "text": "Donde hay hogar y fe"
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
