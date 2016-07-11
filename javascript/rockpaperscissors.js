//this code doesn't run properly. ifixit**

var userChoice = prompt ("Rock, paper, or scissors?");
var computerChoice = Math.random();

if (computerChoice <= .33) {
console.log ("rock");
} else if (computerChoice >= .67) {
console.log ("scissors");
} else {
console.log ("paper");
}

console.log ("Computer:" + computerChoice);

var compare = function (userChoice, computerChoice) {
    if (userChoice===computerChoice) {
        return "It's a tie!";
    } else if (userChoice==="rock") {
        if (computerChoice==="scissors") {
            return "Rock wins!";
            } else {
                return "Paper wins!";
            }
    } else if (userChoice==="paper") {
        if (computerChoice==="rock") {
            return "Paper wins!";
        } else {
            return "Scissors wins!";
        }
    } else if (userChoice==="scissors") {
        if (computerChoice==="paper") {
            return "Scissors wins!";
        } else {
            return "Rock wins!";
        }
    } else if (userChoice==="God") {
        return "Alanis Morisette is a babe.";
    }
};

compare (userChoice, computerChoice);