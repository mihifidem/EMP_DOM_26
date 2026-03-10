// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 2.94,
    "text": "Sigue la Estrella"
  },
  {
    "time": 10.16,
    "text": "Una estrella en el cielo brilló"
  },
  {
    "time": 13.72,
    "text": "No se guarda su luz, se mostró"
  },
  {
    "time": 17.46,
    "text": "Marca un camino nuevo al andar"
  },
  {
    "time": 22.96,
    "text": "Invita a salir y buscar"
  },
  {
    "time": 25.23,
    "text": "Tres viajeros se ponen en pie"
  },
  {
    "time": 27.6,
    "text": "No lo saben todo, pero creen"
  },
  {
    "time": 30.24,
    "text": "Cuando sigues la luz con verdad"
  },
  {
    "time": 33.26,
    "text": "El corazón aprende a mirar"
  },
  {
    "time": 36.84,
    "text": "Sigue la estrella, déjate guiar"
  },
  {
    "time": 41.71,
    "text": "La luz de Dios no es solo para unos más"
  },
  {
    "time": 47.34,
    "text": "Sigue la estrella, no mires atrás"
  },
  {
    "time": 55.12,
    "text": "Jesús es regalo para la humanidad"
  },
  {
    "time": 67.61,
    "text": "No llegaron con prisas ni poder"
  },
  {
    "time": 71.24,
    "text": "Ttrajeron lo mejor de su ser"
  },
  {
    "time": 75.17,
    "text": "Oro, incienso y mirra al llegar"
  },
  {
    "time": 77.99,
    "text": "Pero el mayor regalo es amar"
  },
  {
    "time": 82.75,
    "text": "Cuando compartes lo que hay en ti"
  },
  {
    "time": 88.1,
    "text": "La luz se hace grande al salir"
  },
  {
    "time": 93.85,
    "text": "Dios se revela al mundo entero"
  },
  {
    "time": 98.89,
    "text": "En un niño pequeño y sincero"
  },
  {
    "time": 103.5,
    "text": "Sigue la estrella, déjate guiar"
  },
  {
    "time": 108.69,
    "text": "La luz de Dios no es solo para unos más"
  },
  {
    "time": 113.58,
    "text": "Sigue la estrella, no mires atrás"
  },
  {
    "time": 121.58,
    "text": "Jesús es regalo para la humanidad"
  },
  {
    "time": 124.55,
    "text": "La luz no se esconde"
  },
  {
    "time": 126.45,
    "text": "La luz se da"
  },
  {
    "time": 129.11,
    "text": "Cuando la compartes"
  },
  {
    "time": 131.55,
    "text": "Crece mucho más"
  },
  {
    "time": 136.83,
    "text": "Sigue la estrella, sal a buscar"
  },
  {
    "time": 142.06,
    "text": "Que Dios se muestra donde hay verdad"
  },
  {
    "time": 147.36,
    "text": "Sigue la estrella, aprende a dar"
  },
  {
    "time": 150.97,
    "text": "Jesús es la luz"
  },
  {
    "time": 155.25,
    "text": "Para todos igual"
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
