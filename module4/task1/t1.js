
    const form = document.getElementById('searchForm');


    form.addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevent the default form submission behavior


      const query = document.getElementById('query').value;


      try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Failed to fetch data from TVMaze API');

        const data = await response.json();

        // Display the results in the console
        console.log('Search Results:', data);

        if (data.length === 0) {
          console.log('No shows found for your query.');
        } else {
          data.forEach((result) => {
            console.log(result);


          });
        }
      } catch (error) {
        console.error('Error:', error.message);
      }
    });
