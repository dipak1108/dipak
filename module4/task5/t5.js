
 async function fetchChuckNorrisJoke() {
  try {
    // Send a request to the API
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    if (!response.ok) throw new Error('Failed to fetch the joke');


    const data = await response.json();

    console.log('Random Chuck Norris Joke:', data.value);
  } catch (error) {
    console.error('Error fetching the Chuck Norris joke:', error.message);
  }
}


fetchChuckNorrisJoke();