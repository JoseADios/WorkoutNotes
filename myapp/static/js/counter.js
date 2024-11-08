let intervalId;
let startDate;


window.onload = function () {
    let inputTime = document.getElementById('input-time');
    let restime = localStorage.getItem('restTime');
    let timeEl = document.getElementById('timer')

    if (localStorage.getItem('counterInProgress') === 'true') {

        if (localStorage.getItem('counterPaused') === 'true') {

            timeEl.textContent = restime;
            inputTime.value = restime;

        } else {

            startDate = new Date(parseInt(localStorage.getItem('startDateTime')));
            let currentTime = new Date();
            let difference = (currentTime - startDate) / 1000;

            let remainingTime = restime - difference;

            if (remainingTime > 0) {
                inputTime.value = remainingTime;
                startRestTimer(timeEl);
            } else {
                resetRestTimer(timeEl);
            }
        }

    }
}


function startRestTimer(display) {

    inputTime = document.getElementById('input-time');
    startDate = new Date();
    localStorage.setItem('startDateTime', startDate.getTime());
    localStorage.setItem('counterInProgress', true);
    duration = parseInt(inputTime.value);

    localStorage.setItem('restTime', duration);

    if (localStorage.getItem('counterPaused') === 'true') {
        localStorage.setItem('counterPaused', false);
        duration = parseInt(inputTime.value) - (new Date() - startDate) / 1000;
    }

    counterEditMode(false)

    if (intervalId) {
        clearInterval(intervalId);
    }

    let timer = duration, minutes, seconds;

    intervalId = setInterval(function () {

        display.textContent = timer;

        // Guardar el estado del contador en el localStorage
        localStorage.setItem('restTimer', timer);

        if (--timer < 0) {
            display.textContent = duration;
            clearInterval(intervalId);
            intervalId = null;
            inputTime.value = duration;
            counterEditMode(true)

            localStorage.setItem('counterInProgress', false);
        }
    }, 1000);  // Cada segundo
}

function pauseRestTimer() {
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
        let display = document.getElementById('timer')

        localStorage.setItem('restTime', display.textContent);
        localStorage.setItem('counterPaused', true);
        inputTime.value = display.textContent;
    }

    let btnPause = document.getElementById('btnPause');
    let btnStart = document.getElementById('btnStart');

    btnPause.hidden = true;
    btnStart.hidden = false;
}

// reset method
function resetRestTimer(display) {
    inputTime = document.getElementById('input-time');
    duration = parseInt(localStorage.getItem('default_restTimer'))

    counterEditMode(true)

    clearInterval(intervalId);
    intervalId = null;
    
    display.textContent = duration;
    inputTime.value = duration;

    // localStorage.removeItem('restTimer');
    localStorage.removeItem('startDateTime');
    localStorage.setItem('counterInProgress', false);
}

function minTime() {
    inputTime = document.getElementById('input-time');
    inputTime.value = inputTime.value - 10
}

function addTime() {
    inputTime = document.getElementById('input-time');
    inputTime.value = parseInt(inputTime.value) + 10
}

function counterEditMode(actived) {
    btnStart = document.getElementById('btnStart');
    btnPause = document.getElementById('btnPause');
    btnReset = document.getElementById('btnReset');
    inputTimeBase = document.getElementById('base-input-time');
    baseTimer = document.getElementById('base-timer');

    inputTimeBase.hidden = !actived;
    baseTimer.hidden = actived;
    btnStart.hidden = !actived;
    btnPause.hidden = actived;
    btnReset.hidden = actived;
}

function setDefaultTIme() {
    let inputTime = document.getElementById('input-time');
    localStorage.setItem('default_restTimer', inputTime.value)

}