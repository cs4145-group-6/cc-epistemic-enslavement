import React from 'react';
// @ts-ignore
import getAndSetApiData from '../api/testApi.ts';

// Test component which fetches data from an API and displays it
const TestApiCallComponent = () => {
    const [data, setData] = React.useState();
  
    // Fetch data from API and set the component text to this
    React.useEffect(() => {
      getAndSetApiData(setData);
    }, []);
  
    return <p>Data from some API: {data}</p>;
};

export default TestApiCallComponent;
