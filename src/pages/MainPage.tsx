import React from 'react';
// @ts-ignore
import TestApiCallComponent from '../components/TestApiCallComponent.tsx';
// @ts-ignore
import YesNoQuestion from '../components/YesNoQuestion.tsx';

// For now main page contains only test component which makes API call
const MainPage = () => {
  return (
    <div>
      <h1>Welcome to the Main Page</h1>
      <YesNoQuestion question="Do you like React?" />
    </div>
  );
};

export default MainPage;
