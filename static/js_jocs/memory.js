document.addEventListener("DOMContentLoaded", () => {

    const symbols = ["🕯️","⭐","❤️","🏠","🕊️","🌙"];
    const board = document.getElementById("gameBoard");
    const message = document.getElementById("message");
    const timerDisplay = document.getElementById("timer");
    const scoreDisplay = document.getElementById("score");
    const restartBtn = document.getElementById("restartBtn");

    let cardsArray;
    let firstCard = null;
    let secondCard = null;
    let lockBoard = false;
    let matches = 0;
    let score = 0;
    let time = 0;
    let timerInterval;

    startGame();

    restartBtn.addEventListener("click", startGame);

    function startGame() {

        board.innerHTML = "";
        message.classList.remove("show");

        cardsArray = [...symbols, ...symbols];
        shuffle(cardsArray);

        matches = 0;
        score = 0;
        time = 0;

        scoreDisplay.textContent = score;
        timerDisplay.textContent = time;

        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            time++;
            timerDisplay.textContent = time;
        }, 1000);

        cardsArray.forEach(symbol => {
            const card = document.createElement("div");
            card.classList.add("card");
            card.dataset.symbol = symbol;
            card.innerHTML = "❓";
            board.appendChild(card);

            card.addEventListener("click", () => flipCard(card));
        });
    }

    function flipCard(card) {

        if (lockBoard) return;
        if (card.classList.contains("flipped") || card.classList.contains("matched")) return;

        card.classList.add("flipped");
        card.innerHTML = card.dataset.symbol;

        if (!firstCard) {
            firstCard = card;
            return;
        }

        secondCard = card;
        checkMatch();
    }

    function checkMatch() {

        if (firstCard.dataset.symbol === secondCard.dataset.symbol) {

            firstCard.classList.add("matched");
            secondCard.classList.add("matched");

            matches++;
            addScore();
            resetTurn();

            if (matches === symbols.length) {
                clearInterval(timerInterval);
                setTimeout(() => {
                    message.classList.add("show");
                }, 500);
            }

        } else {
            lockBoard = true;
            setTimeout(() => {
                firstCard.classList.remove("flipped");
                secondCard.classList.remove("flipped");
                firstCard.innerHTML = "❓";
                secondCard.innerHTML = "❓";
                resetTurn();
            }, 800);
        }
    }

    function addScore() {
        let bonus = Math.max(10 - Math.floor(time / 5), 2);
        score += bonus;
        scoreDisplay.textContent = score;
    }

    function resetTurn() {
        [firstCard, secondCard] = [null, null];
        lockBoard = false;
    }

    function shuffle(array) {
        array.sort(() => Math.random() - 0.5);
    }

});
