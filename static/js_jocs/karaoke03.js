// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 7.65,
    "text": "¡Alégrate!;"
  },
  {
    "time": 16.51,
    "text": "Hoy la luz brilla más;"
  },
  {
    "time": 19.88,
    "text": "Se nota al caminar;"
  },
  {
    "time": 24.05,
    "text": "Algo bonito está cerca;"
  },
  {
    "time": 27.09,
    "text": "Mi corazón lo sabe ya;"
  },
  {
    "time": 29.8,
    "text": "Las manos quieren aplaudir;"
  },
  {
    "time": 33.34,
    "text": "Los pies quieren saltar;"
  },
  {
    "time": 37.21,
    "text": "Cuando la alegría llega;"
  },
  {
    "time": 41.21,
    "text": "Todo empieza a cantar;"
  },
  {
    "time": 44.43,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 47.56,
    "text": "Jesús está cerca ya;"
  },
  {
    "time": 51.23,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 54.14,
    "text": "La luz no se apagará;"
  },
  {
    "time": 57.53,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 60.75,
    "text": "Abre el corazón así;"
  },
  {
    "time": 64.22,
    "text": "Porque cuando hay alegría;"
  },
  {
    "time": 67.67,
    "text": "Jesús vive aquí;"
  },
  {
    "time": 75.69,
    "text": "No es una alegría ruidosa;"
  },
  {
    "time": 78.99,
    "text": "No es solo reír sin más;"
  },
  {
    "time": 82.67,
    "text": "Es una alegría por dentro;"
  },
  {
    "time": 85.72,
    "text": "Que se aprende a cuidar;"
  },
  {
    "time": 89.18,
    "text": "Nace cuando compartimos;"
  },
  {
    "time": 92.25,
    "text": "Cuando aprendemos a amar;"
  },
  {
    "time": 95.66,
    "text": "Cuando dejamos un hueco;"
  },
  {
    "time": 98.47,
    "text": "Para que Dios pueda entrar;"
  },
  {
    "time": 101.76,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 104.74,
    "text": "Jesús está cerca ya;"
  },
  {
    "time": 108.05,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 111.04,
    "text": "La luz no se apagará;"
  },
  {
    "time": 114.99,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 117.75,
    "text": "Abre el corazón así;"
  },
  {
    "time": 121.41,
    "text": "Porque cuando hay alegría;"
  },
  {
    "time": 125.24,
    "text": "Jesús vive aquí;"
  },
  {
    "time": 126.61,
    "text": "Sonríe;"
  },
  {
    "time": 127.69,
    "text": "Canta;"
  },
  {
    "time": 130.39,
    "text": "La espera ya se ve;"
  },
  {
    "time": 133.52,
    "text": "La alegría nos recuerda;"
  },
  {
    "time": 137.36,
    "text": "Que Dios viene de pie;"
  },
  {
    "time": 140.59,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 143.75,
    "text": "Jesús está cerca ya;"
  },
  {
    "time": 147.16,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 150.28,
    "text": "La luz no se apagará;"
  },
  {
    "time": 153.66,
    "text": "¡Alégrate! ¡Alégrate!;"
  },
  {
    "time": 156.85,
    "text": "Compártelo al pasar;"
  },
  {
    "time": 160.41,
    "text": "Que la alegría verdadera;"
  },
  {
    "time": 163.63,
    "text": "Se contagia al amar;"
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
