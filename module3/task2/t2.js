// Get the target element by ID
const targetElement = document.getElementById('target');

// Create an <h1> element
const heading = document.createElement('h1');
heading.textContent = 'Welcome to createElement and appendChild Demo';

// Create a <p> element
const paragraph = document.createElement('p');
paragraph.textContent = `<li>First item</li>
<li>Second item</li>
<li>Third item</li>`;

// Append the elements to the target element
targetElement.appendChild(heading);
targetElement.appendChild(paragraph);