'use strict';
const names = ['John', 'Paul', 'Jones'];
let listHTML = '<ul>';
for (let i = 0; i < names.length; i++) {
    listHTML += `<li>${names[i]}</li>`;
}

listHTML += '</ul>';
document.getElementById('target').innerHTML = listHTML;
