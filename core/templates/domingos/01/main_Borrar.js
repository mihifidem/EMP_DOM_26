// Toggle popup reto
document.addEventListener("DOMContentLoaded", () => {
    const retoIcon = document.querySelector('.reto-icon');
    const retoPopup = document.getElementById('retoPopup');
    retoIcon.addEventListener('click', () => {
        retoPopup.classList.toggle('active');
        if (retoPopup.classList.contains('active')) {
            retoPopup.style.animation = 'retoPopIn 0.5s';
        }
    });
    // Cerrar popup al hacer click fuera
    document.addEventListener('click', (e) => {
        if (retoPopup.classList.contains('active') && !retoPopup.contains(e.target) && e.target !== retoIcon) {
            retoPopup.classList.remove('active');
        }
    });
});
// Reto de 7 días: marcar estrellas y mostrar mensaje al completar
document.addEventListener("DOMContentLoaded", () => {
    const retoChecks = document.querySelectorAll('.reto-chk');
    const retoCompletado = document.getElementById('reto-completado');
    retoChecks.forEach(chk => {
        chk.addEventListener('change', () => {
            // Cambia estrella
            const star = chk.parentElement.querySelector('.star');
            star.textContent = chk.checked ? '★' : '☆';
            // Si todos están marcados, mostrar mensaje
            if ([...retoChecks].every(c => c.checked)) {
                retoCompletado.style.display = 'block';
            } else {
                retoCompletado.style.display = 'none';
            }
        });
    });
});

// ======================================
// HERO I DOMINGO - ESPERANZA (FINAL)
// ======================================

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("lightBtn");
    const candle = document.getElementById("candle");
    const hero = document.getElementById("hero");
    const music = document.getElementById("music");
    const bell = document.getElementById("bell");
    let isLit = false;

    button.addEventListener("click", () => {
            // Botón para pausar/reanudar música
            const toggleMusicBtn = document.getElementById("toggleMusicBtn");
            if (toggleMusicBtn && music) {
                toggleMusicBtn.addEventListener("click", () => {
                    if (music.paused) {
                        music.play();
                        toggleMusicBtn.innerHTML = "⏸️ Pausar música";
                    } else {
                        music.pause();
                        toggleMusicBtn.innerHTML = "▶️ Reanudar música";
                    }
                });
            }
        if (isLit) return;
        isLit = true;

        // 🔔 Campanita
        try {
            bell.currentTime = 0;
            bell.play();
        } catch (e) {}

        // 📳 Vibración móvil
        if (navigator.vibrate) {
            navigator.vibrate(150);
        }

        // 🕯️ Encender vela
        candle.classList.add("lit");

        // 🎥 Zoom + desenfoque
        hero.classList.add("zoomed");

        // 🌌 Iluminar cielo (SE MANTIENE)
        hero.classList.add("litSky");

        // ✨ Explosión mágica
        createMagicBurst();

        // 🎵 Música
        if (music) {
            music.volume = 0;
            music.play().then(() => {
                fadeInMusic(music, 0.4, 2500);
            }).catch(() => {});
        }

        // 🔘 Botón
        button.disabled = true;
        button.innerText = "✨ La luz está encendida";

        // 🎥 REGRESO MUY LENTO DESPUÉS DE 6 SEGUNDOS
        setTimeout(() => {
            hero.classList.remove("zoomed");
        }, 6000);

        // 💛 Mostrar mensaje final después del regreso
        setTimeout(() => {
            const finalMessage = document.getElementById("finalMessage");
            finalMessage.classList.add("show");
        }, 9000);
    });
});



    /* ===============================
       EXPLOSIÓN DE ESTRELLITAS
    ============================== */

    function createMagicBurst() {

        for (let i = 0; i < 15; i++) {

            const star = document.createElement("span");
            star.classList.add("magic-star");

            const angle = Math.random() * 360;
            const distance = 80 + Math.random() * 40;

            star.style.left = "50%";
            star.style.top = "45%";

            star.style.setProperty("--x", `${Math.cos(angle) * distance}px`);
            star.style.setProperty("--y", `${Math.sin(angle) * distance}px`);

            hero.appendChild(star);

            setTimeout(() => {
                star.remove();
            }, 1200);
        }
    }



/* ===============================
   FADE IN MÚSICA
================================ */

function fadeInMusic(audio, targetVolume, duration) {

    const steps = 50;
    const stepTime = duration / steps;
    const volumeStep = targetVolume / steps;

    let currentStep = 0;

    const fade = setInterval(() => {
        currentStep++;
        audio.volume = Math.min(volumeStep * currentStep, targetVolume);

        if (currentStep >= steps) {
            clearInterval(fade);
        }
    }, stepTime);
}

