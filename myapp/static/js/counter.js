window.onload = function () {
    let timeEl = document.getElementById('timer')
    let btnReset = document.getElementById('btnReset');

    let storedTime = localStorage.getItem('restTimer');
    if (storedTime) {
        timeEl.textContent = storedTime
        btnReset.hidden = false
    }

}
    

let intervalId;

function startRestTimer(duration, display) {

    let btnStart = document.getElementById('btnStart');
    let btnPause = document.getElementById('btnPause');
    let btnReset = document.getElementById('btnReset');

    btnStart.hidden = true;
    btnPause.hidden = false;
    btnReset.hidden = false;

    if (intervalId) {
        clearInterval(intervalId);
    }

    let storedTime = localStorage.getItem('restTimer');
    if (storedTime) {
        duration = parseInt(storedTime);
    }

    let timer = duration, minutes, seconds;

    intervalId = setInterval(function () {
        minutes = Math.floor(timer / 60);  // Calcular los minutos
        seconds = timer % 60;  // Calcular los segundos

        display.textContent = timer;

        // Guardar el estado del contador en el localStorage
        localStorage.setItem('restTimer', timer);

        if (--timer < 0) {
            display.textContent = duration;
            clearInterval(intervalId);
            intervalId = null;
        }
    }, 1000);  // Cada segundo
}

function pauseRestTimer(duration, display) {
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
    }

    btnPause = document.getElementById('btnPause');
    btnReset = document.getElementById('btnReset');
    btnStart = document.getElementById('btnStart');

    btnPause.hidden = true;
    btnStart.hidden = false;
    btnReset.hidden = true;
}

// reset method
function resetRestTimer(duration, display) {
    btnReset = document.getElementById('btnReset');
    btnStart = document.getElementById('btnStart');
    btnPause = document.getElementById('btnPause');

    btnPause.hidden = true;
    btnStart.hidden = false;
    btnReset.hidden = true;

    clearInterval(intervalId);
    intervalId = null;
    display.textContent = duration;

    localStorage.removeItem('restTimer');
}
