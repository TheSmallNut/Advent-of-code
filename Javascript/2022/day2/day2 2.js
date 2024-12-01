const fs = require("fs");
const CONVERT = { X: 0, Y: 3, Z: 6 };
const SCORES = { A: 0, B: 1, C: 2 };

function scoreToFind(opponentChoice, playerChoice) {
    if (playerChoice == "X") {
        if (opponentChoice == 0) {
            return 3;
        }
        return opponentChoice;
    }
    if (playerChoice == "Y") {
        return opponentChoice + 1;
    }
    toReturn = opponentChoice + 1;
    toReturn %= 3;
    return toReturn + 1;
}

fs.readFile("Javascript/2022/day2/input.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    const lines = data.split("\n").map((line) => line.trim());
    let totalScore = 0;
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const opponentChoice = SCORES[line[0]];
        const playerChoice = line[2];
        totalScore += CONVERT[playerChoice];
        totalScore += scoreToFind(opponentChoice, playerChoice);
        console.log(
            "TOTAL SCORE: " +
                totalScore +
                " | O : P  " +
                opponentChoice +
                " " +
                playerChoice
        );
    }
    console.log(totalScore);
});
