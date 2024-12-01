const fs = require("fs");
const CONVERT = { X: "A", Y: "B", Z: "C" };
const SCORES = { A: 0, B: 1, C: 2 };

function scoreToFind(opponentChoice, playerChoice) {
    if (opponentChoice == playerChoice) {
        return 3;
    }
    if ((playerChoice + 1) % 3 == opponentChoice) {
        return 0;
    }
    if ((opponentChoice + 1) % 3 == playerChoice) {
        return 6;
    }
    throw new Error("This is an intentional error!");
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
        const playerChoice = SCORES[CONVERT[line[2]]];
        const score = scoreToFind(opponentChoice, playerChoice);
        totalScore += score;
        totalScore += playerChoice + 1;
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
