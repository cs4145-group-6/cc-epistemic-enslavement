import axios from 'axios';

// Simple API call to get mock data
async function getAndSetApiData(setter): Promise<void> {
    const url = 'https://jsonplaceholder.typicode.com/posts/1';
    const data = (await axios.get(url)).data.title;
    setter(data);
}

export default getAndSetApiData;
