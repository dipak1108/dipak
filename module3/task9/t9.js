const calculationInput = document.getElementById('calculation');
const calculateButton = document.getElementById('start');
const resultParagraph = document.getElementById('result');

// Add click event listener to button
calculateButton.addEventListener('click', () => {
    // Get the input value
    const calculation = calculationInput.value.trim();
    let result;

    // Check which operator is included and split the input
    if (calculation.includes('+')) {
        const [num1, num2] = calculation.split('+').map(Number);
        result = num1 + num2;
    } else if (calculation.includes('-')) {
        const [num1, num2] = calculation.split('-').map(Number);
        result = num1 - num2;
    } else if (calculation.includes('*')) {
        const [num1, num2] = calculation.split('*').map(Number);
        result = num1 * num2;
    } else if (calculation.includes('/')) {
        const [num1, num2] = calculation.split('/').map(Number);
        if (num2 === 0) {
            result = "Cannot divide by zero.";
        } else {
            result = Math.floor(num1 / num2); // Integer division
        }
    } else {
        result = "Invalid input. Use +, -, *, or /.";
    }

    // Display the result
    resultParagraph.textContent = `Result: ${result}`;
});