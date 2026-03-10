// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 5.89,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 13.54,
    "text": "Junto al río en silencio"
  },
  {
    "time": 18.76,
    "text": "Jesús se acerca a orar"
  },
  {
    "time": 23.25,
    "text": "El agua toca su cuerpo"
  },
  {
    "time": 28.52,
    "text": "El cielo se quiere abrir ya"
  },
  {
    "time": 33.35,
    "text": "No trae palabras grandes"
  },
  {
    "time": 39.05,
    "text": "Ni busca llamar la atención"
  },
  {
    "time": 44.48,
    "text": "Pero en el gesto sencillo"
  },
  {
    "time": 50.75,
    "text": "Habla fuerte el amor"
  },
  {
    "time": 53.39,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 56.22,
    "text": "Se escucha decir a Dios"
  },
  {
    "time": 59.46,
    "text": "En Ti tengo puesta mi alegría"
  },
  {
    "time": 61.89,
    "text": "En Ti vive mi amor"
  },
  {
    "time": 65.1,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 67.73,
    "text": "Y al escucharlo hoy aquí"
  },
  {
    "time": 72.5,
    "text": "Dios me dice en silencio"
  },
  {
    "time": 78.61,
    "text": "Yo también te elegí"
  },
  {
    "time": 82.85,
    "text": "El agua cae despacio"
  },
  {
    "time": 88.02,
    "text": "Como lluvia de paz"
  },
  {
    "time": 93.94,
    "text": "Y el Espíritu desciende"
  },
  {
    "time": 99.59,
    "text": "Como luz al pasar"
  },
  {
    "time": 103.04,
    "text": "Jesús comienza su camino"
  },
  {
    "time": 105.55,
    "text": "No está solo al andar"
  },
  {
    "time": 108.85,
    "text": "Sabe quién es, sabe a quién ama"
  },
  {
    "time": 113.22,
    "text": "Y al mundo va a anunciar"
  },
  {
    "time": 115.57,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 118.42,
    "text": "Se escucha decir a Dios"
  },
  {
    "time": 121.75,
    "text": "En Ti tengo puesta mi alegría"
  },
  {
    "time": 124.27,
    "text": "En Ti vive mi amor"
  },
  {
    "time": 126.89,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 129.9,
    "text": "Y al escucharlo hoy aquí"
  },
  {
    "time": 134.77,
    "text": "Dios me dice en silencio"
  },
  {
    "time": 140.77,
    "text": "Yo también te elegí"
  },
  {
    "time": 145.78,
    "text": "Soy hijo"
  },
  {
    "time": 156.16,
    "text": "Soy amado"
  },
  {
    "time": 159.34,
    "text": "Dios me llama por mi nombre"
  },
  {
    "time": 170.76,
    "text": "Tú eres mi Hijo amado"
  },
  {
    "time": 173.36,
    "text": "No lo voy a olvidar"
  },
  {
    "time": 176.45,
    "text": "Si confío y doy cada paso"
  },
  {
    "time": 183.66,
    "text": "Sé que Dios me guiará"
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
