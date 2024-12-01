const fs = require("fs");

fs.readFile("Javascript/2024/day1/input.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    const lines = data.split("\n").map((line) => line.trim());

    let leftList = [];
    let rightList = [];

    for (let i = 0; i < lines.length; i++) {
        let nums = lines[i].split("   ");
        leftList.push(parseInt(nums[0]));
        rightList.push(parseInt(nums[1]));
    }
    leftList.sort();
    rightList.sort();
    let total = 0;
    for (let i = 0; i < leftList.length; i++) {
        total += Math.abs(leftList[i] - rightList[i]);
    }
    console.log(total);
});
