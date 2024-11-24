
const form = document.getElementById('searchForm');
const resultsContainer = document.getElementById('results');


form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission

  resultsContainer.innerHTML = '';

  const query = document.getElementById('query').value.trim();

  if (!query) {
    console.error('Please enter a valid TV series name.');
    return;
  }

  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error('Failed to fetch data from TVMaze API');

    const data = await response.json();

    if (data.length > 0) {
      data.forEach((result) => {
        const tvShow = result.show;


        const article = document.createElement('article');


        const title = document.createElement('h2');
        title.textContent = tvShow.name;
        article.appendChild(title);


        const link = document.createElement('a');
        link.href = tvShow.url
        link.textContent = 'View Details';
        link.target = '_blank'; // Open in a new tab
        article.appendChild(link);


        if (tvShow.image?.medium) {
          const img = document.createElement('img');
          img.src = tvShow.image.medium;
          img.alt = tvShow.name;
          article.appendChild(img);
        }


        if (tvShow.summary) {
          const summary = document.createElement('div');
          summary.innerHTML = tvShow.summary; // Safe because TVMaze provides sanitized HTML
          article.appendChild(summary);
        }


        resultsContainer.appendChild(article);
      });
    } else {

      const noResults = document.createElement('p');
      noResults.textContent = 'No TV shows found for your search.';
      resultsContainer.appendChild(noResults);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
});