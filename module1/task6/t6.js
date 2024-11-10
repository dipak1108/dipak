
        function calculateSquareRoot() {
            const userConfirmed = confirm("Should I calculate the square root?");

            if (userConfirmed) {
                const input = prompt("Please enter a number:");
                const number = parseFloat(input);

                if (isNaN(number)) {
                    document.getElementById("result").innerText = "Please enter a valid number.";
                    return;
                }

                if (number < 0) {
                    document.getElementById("result").innerText = "The square root of a negative number is not defined.";
                } else {
                    const squareRoot = Math.sqrt(number);
                    document.getElementById("result").innerText = `The square root of ${number} is ${squareRoot}.`;
                }
            } else {
                document.getElementById("result").innerText = "The square root is not calculated.";
            }
        }
