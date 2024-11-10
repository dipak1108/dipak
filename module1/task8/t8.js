'use strict';

const startYear= prompt('enter starting year');
const endYear = prompt('enter ending year');

/*
year % 4 === 0
year % 100 === 0
year % 400 === 0

year % 4 === 0 && year % 100 !== 0 || year % 400 === 0
 */

for (let i = startYear; i < endYear; i++) {
  if (i  % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)){
    //add <li> to the page
    document.querySelector('#target').innerHTML += `<li>${i}</li>`;
  }

}

