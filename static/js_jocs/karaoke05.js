// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 2.87,
    "text": "Esta noche nace el Amor;"
  },
  {
    "time": 8.11,
    "text": "En el silencio de la noche;"
  },
  {
    "time": 11.28,
    "text": "Una estrella se encendió;"
  },
  {
    "time": 14.84,
    "text": "En un portal tan pequeño;"
  },
  {
    "time": 18.17,
    "text": "Dios al mundo llegó;"
  },
  {
    "time": 21.93,
    "text": "No trae corona ni oro;"
  },
  {
    "time": 25.19,
    "text": "Ni riquezas que mostrar;"
  },
  {
    "time": 28.85,
    "text": "Solo un niño entre paja;"
  },
  {
    "time": 32.03,
    "text": "Y un mensaje de paz;"
  },
  {
    "time": 37.11,
    "text": "Esta noche nace el Amor;"
  },
  {
    "time": 40.54,
    "text": "Nace Dios en un portal;"
  },
  {
    "time": 44.26,
    "text": "Canta el cielo, ríe el mundo;"
  },
  {
    "time": 51.51,
    "text": "Es Navidad, es Navidad;"
  },
  {
    "time": 54.86,
    "text": "Esta noche nace el Amor;"
  },
  {
    "time": 58.21,
    "text": "Todo empieza a brillar;"
  },
  {
    "time": 61.83,
    "text": "Abre el corazón, hermano;"
  },
  {
    "time": 68.74,
    "text": "Es Navidad, es Navidad;"
  },
  {
    "time": 72.46,
    "text": "María lo mira en silencio;"
  },
  {
    "time": 75.77,
    "text": "José cuida sin hablar;"
  },
  {
    "time": 79.41,
    "text": "Y los ángeles cantan;"
  },
  {
    "time": 82.79,
    "text": "Que ya hay luz en la oscuridad;"
  },
  {
    "time": 86.43,
    "text": "Los pastores van corriendo;"
  },
  {
    "time": 89.69,
    "text": "No se quieren quedar atrás;"
  },
  {
    "time": 93.22,
    "text": "Cuando Dios se hace pequeño;"
  },
  {
    "time": 98.45,
    "text": "Todos quieren llegar;"
  },
  {
    "time": 101.69,
    "text": "Esta noche nace el Amor;"
  },
  {
    "time": 105.31,
    "text": "Nace Dios en un portal;"
  },
  {
    "time": 108.85,
    "text": "Canta el cielo, ríe el mundo;"
  },
  {
    "time": 115.85,
    "text": "Es Navidad, es Navidad;"
  },
  {
    "time": 119.2,
    "text": "Esta noche nace el Amor;"
  },
  {
    "time": 122.48,
    "text": "Todo empieza a brillar;"
  },
  {
    "time": 126.34,
    "text": "Abre el corazón, hermano;"
  },
  {
    "time": 131.6,
    "text": "Es Navidad, es Navidad;"
  },
  {
    "time": 133.19,
    "text": "Tan pequeño;"
  },
  {
    "time": 134.79,
    "text": "Tan cercano;"
  },
  {
    "time": 137.19,
    "text": "Dios con nosotros ya está;"
  },
  
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
