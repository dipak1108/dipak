
        function rollDice() {

            const input = prompt("How many dice would you like to roll?");
            const numRolls = parseInt(input);

            if (isNaN(numRolls) || numRolls <= 0) {
                document.getElementById("result").innerText = "Please enter a valid positive number.";
                return;
            }

            let sum = 0;

            for (let i = 0; i < numRolls; i++) {
                const roll = Math.floor(Math.random() * 6) + 1;
                sum += roll;
            }

            document.getElementById("result").innerText = `The sum of rolling ${numRolls} dice is ${sum}.`;
        }

