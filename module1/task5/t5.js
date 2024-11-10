
        const year = parseInt(prompt("Enter Year"));

        // Check if the input is a valid year
        if (isNaN(year)) {
            alert("Please enter a valid year.");
            return;
        }

        // Determine if the year is a leap year
        let isLeapYear = false;

        if (year % 4 === 0) {
            if (year % 100 === 0) {
                if (year % 400 === 0) {
                    isLeapYear = true;
                }
            } else {
                isLeapYear = true;
            }
        }

        // Display the result
        if (isLeapYear) {
             alert(`${year} is a leap year!`);
            } else {
            alert(`${year} is not a leap year.`);
        }

