// Import the File System module
const fs = require("fs");

// Read the file asynchronously
fs.readFile("Javascript/2022/day1/input.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    const lines = data.split("\n").map((line) => line.trim());
    console.log("Lines:", lines);
    let elves = [];

    let carryingElf = 0;
    for (let i = 0; i < lines.length; i++) {
        let currentElf = lines[i];
        if (currentElf == "") {
            elves.push(carryingElf);
            carryingElf = 0;
            continue;
        }
        console.log(parseInt(currentElf));
        carryingElf += parseInt(currentElf);
        console.log("whole elf: " + carryingElf);
    }
    elves.push(carryingElf);
    const MAX_VALUES = 3;
    let maximums = [];
    for (let i = 0; i < MAX_VALUES; i++) {
        const maxValue = Math.max(...elves);
        const maxIndex = elves.indexOf(maxValue);
        maximums.push(elves[maxIndex]);
        console.log(elves[maxIndex]);
        elves.splice(maxIndex, 1);
    }
    console.log(maximums);
    console.log(maximums[0] + maximums[1] + maximums[2]);
});
