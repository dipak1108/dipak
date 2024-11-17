const form = document.getElementById('searchForm');
const resultsContainer = document.getElementById('results');

form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission
  resultsContainer.innerHTML = ''; // Clear previous results

  const query = document.getElementById('query').value.trim();

  if (!query) {
    console.error('Please enter a valid search term.');
    return;
  }

  try {
    // Send a request to the API with the search term
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error('Failed to fetch jokes');

    const data = await response.json();

    if (data.result.length > 0) {

      data.result.forEach((joke) => {
        const article = document.createElement('article');
        const jokeText = document.createElement('p');
        jokeText.textContent = joke.value; // Add joke text
        article.appendChild(jokeText);
        resultsContainer.appendChild(article);
      });
    } else {

      const noResults = document.createElement('p');
      noResults.textContent = 'No jokes found for your search.';
      resultsContainer.appendChild(noResults);
    }
  } catch (error) {
    console.error('Error fetching jokes:', error.message);
  }
});