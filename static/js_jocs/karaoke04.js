// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 16.1,
    "text": "Confío en Ti;"
  },
  {
    "time": 19.58,
    "text": "Todo está casi en silencio;"
  },
  {
    "time": 22.97,
    "text": "La noche empieza a hablar;"
  },
  {
    "time": 26.31,
    "text": "No entiendo todo el camino;"
  },
  {
    "time": 29.24,
    "text": "Pero confío igual;"
  },
  {
    "time": 31.75,
    "text": "Hay preguntas que no digo;"
  },
  {
    "time": 34.87,
    "text": "Hay cosas que no sé ver;"
  },
  {
    "time": 39.51,
    "text": "Pero guardo en mi corazón;"
  },
  {
    "time": 44.12,
    "text": "Lo que está por nacer;"
  },
  {
    "time": 48.02,
    "text": "Confío en Ti;"
  },
  {
    "time": 51.37,
    "text": "Paso a paso aquí;"
  },
  {
    "time": 55.27,
    "text": "Aunque no lo entienda todo;"
  },
  {
    "time": 58.32,
    "text": "Sé que estás junto a mí;"
  },
  {
    "time": 60.87,
    "text": "Confío en Ti;"
  },
  {
    "time": 63.82,
    "text": "Mi miedo dejo ir;"
  },
  {
    "time": 68.09,
    "text": "Abro el corazón despacio…;"
  },
  {
    "time": 71.92,
    "text": "Y me quedo en Ti;"
  },
  {
    "time": 82.01,
    "text": "Como un \"sí\" dicho en silencio;"
  },
  {
    "time": 85.33,
    "text": "Como un gesto de amor;"
  },
  {
    "time": 87.87,
    "text": "Cuando dejo espacio dentro;"
  },
  {
    "time": 90.77,
    "text": "Habla más fuerte Dios;"
  },
  {
    "time": 94.47,
    "text": "No hace falta tener respuestas;"
  },
  {
    "time": 96.93,
    "text": "Ni saber qué vendrá;"
  },
  {
    "time": 100.29,
    "text": "Cuando confío de verdad;"
  },
  {
    "time": 103.23,
    "text": "Todo empieza a encajar;"
  },
  {
    "time": 106.75,
    "text": "Confío en Ti;"
  },
  {
    "time": 110.18,
    "text": "Paso a paso aquí;"
  },
  {
    "time": 114.41,
    "text": "Aunque no lo entienda todo;"
  },
  {
    "time": 117.21,
    "text": "Sé que estás junto a mí;"
  },
  {
    "time": 120.2,
    "text": "Confío en Ti;"
  },
  {
    "time": 122.97,
    "text": "Mi miedo dejo ir;"
  },
  {
    "time": 127.27,
    "text": "Abro el corazón despacio…;"
  },
  {
    "time": 131.8,
    "text": "Y me quedo en Ti;"
  },
  {
    "time": 135.05,
    "text": "Aquí estoy;"
  },
  {
    "time": 138.54,
    "text": "Tal como soy;"
  },
  {
    "time": 146.21,
    "text": "En silencio digo: sí;"
  },
  {
    "time": 150.95,
    "text": "Confío en Ti;"
  },
  {
    "time": 154.43,
    "text": "No tengo prisa hoy;"
  },
  {
    "time": 158.34,
    "text": "Porque cuando Tú llegas;"
  },
  {
    "time": 161,
    "text": "Todo encuentra su voz;"
  },
  {
    "time": 163.76,
    "text": "Confío en Ti;"
  },
  {
    "time": 166.89,
    "text": "Mi hogar eres Tú;"
  },
  {
    "time": 170.79,
    "text": "Abro el corazón despacio…;"
  },
  {
    "time": 176.67,
    "text": "Y naces Tú;"
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
