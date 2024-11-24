 const form = document.getElementById('searchForm');


 form.addEventListener('submit', async (event) => {
   event.preventDefault(); // Prevent the default form submission behavior


   const query = document.getElementById('query').value.trim();

   if (!query) {
     console.error('Please enter a valid TV series name.');
     return;
   }


   try {
     const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
     if (!response.ok) throw new Error('Failed to fetch data from TVMaze API');

     const data = await response.json();


     console.log('Search Results:', data);


     if (data.length > 0) {
       data.forEach((result) => {
        console.log(result);

       });
     } else {
       console.log('No results found for your query.');
     }
   } catch (error) {
     console.error('Error:', error.message);
   }
 });