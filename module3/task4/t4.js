'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];


// Get the target element by ID
const targetElement = document.getElementById('target');

students.forEach(element => {
  console.log(element.id);
  console.log(element.name);
  const option = document.createElement('option');
  option.textContent = element.name;
  option.value = element.id;
  targetElement.appendChild(option);
});

// Loop through the array and create <option> elements
for (let i = 0; i < students.length; i++) {


}