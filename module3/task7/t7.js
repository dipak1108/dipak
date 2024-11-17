const triggerElement = document.getElementById('trigger');
const targetImage = document.getElementById('target');

// Add mouseover event listener
triggerElement.addEventListener('mouseover', () => {
    targetImage.src = 'img/picB.jpg'; // Change the image to picB.jpg
});

// Add mouseout event listener
triggerElement.addEventListener('mouseout', () => {
    targetImage.src = 'img/picA.jpg'; // Revert the image back to picA.jpg
});