// Karaoke sincronizado con lyrics_sync.json
let lyrics =[
  {
    "time": 21.23,
    "text": "Jesús crecía cada día"
  },
  {
    "time": 30.73,
    "text": "Jesús crecía cada día"
  },
  {
    "time": 35.36,
    "text": "En su casa de Nazaret"
  },
  {
    "time": 38.95,
    "text": "Aprendía con sus padres"
  },
  {
    "time": 46.65,
    "text": "A escuchar y a querer"
  },
  {
    "time": 49.95,
    "text": "Jugaba, reía, ayudaba"
  },
  {
    "time": 53.25,
    "text": "Sabía esperar su momento"
  },
  {
    "time": 58.31,
    "text": "Dios crecía poco a poco"
  },
  {
    "time": 62.7,
    "text": "En un corazón pequeño"
  },
  {
    "time": 69.91,
    "text": "Jesús crecía en sabiduría"
  },
  {
    "time": 76.69,
    "text": "En amor y en verdad"
  },
  {
    "time": 84.74,
    "text": "Crecía delante de Dios"
  },
  {
    "time": 92.1,
    "text": "Y de todos los demás"
  },
  {
    "time": 101.23,
    "text": "Jesús crecía cada día"
  },
  {
    "time": 107.59,
    "text": "Como crezco yo también"
  },
  {
    "time": 116.34,
    "text": "Cuando aprendo a amar despacio"
  },
  {
    "time": 120.41,
    "text": "Y a confiar una vez más"
  },
  {
    "time": 128.2,
    "text": "Aprendió a decir gracias"
  },
  {
    "time": 132.29,
    "text": "A pedir perdón también"
  },
  {
    "time": 136.35,
    "text": "A trabajar con sus manos"
  },
  {
    "time": 140.29,
    "text": "Y a escuchar con atención"
  },
  {
    "time": 143.69,
    "text": "No tenía prisa ninguna"
  },
  {
    "time": 147.62,
    "text": "Ni quería ser mayor"
  },
  {
    "time": 151.98,
    "text": "Sabía que en lo pequeño"
  },
  {
    "time": 156.24,
    "text": "También habla el corazón"
  },
  {
    "time": 164.39,
    "text": "Jesús crecía en sabiduría"
  },
  {
    "time": 171.73,
    "text": "En amor y en verdad"
  },
  {
    "time": 178.29,
    "text": "Crecía delante de Dios"
  },
  {
    "time": 186.78,
    "text": "Y de todos los demás"
  },
  {
    "time": 194.67,
    "text": "Jesús crecía cada día"
  },
  {
    "time": 201.37,
    "text": "Como crezco yo también"
  },
  {
    "time": 209.93,
    "text": "Cuando aprendo a amar despacio"
  },
  {
    "time": 214.21,
    "text": "Y a confiar una vez más"
  },
  {
    "time": 220.85,
    "text": "Yo también quiero crecer"
  },
  {
    "time": 225.61,
    "text": "Como Jesús creció"
  },
  {
    "time": 229.7,
    "text": "Con amor en cada paso"
  },
  {
    "time": 234.37,
    "text": "Y a mi lado siempre Dios"
  },
  {
    "time": 242.95,
    "text": "Jesús crecía en sabiduría"
  },
  {
    "time": 247.21,
    "text": "Yo también quiero crecer"
  },
  {
    "time": 254.84,
    "text": "Si escucho, ayudo y confío"
  },
  {
    "time": 266.97,
    "text": "Sé que voy por buen camino también"
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
