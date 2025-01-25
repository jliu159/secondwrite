import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import { Provider } from 'react-redux';
import store from './utils/store.ts';

// Get the root element where you want to render your App component
const rootElement = document.getElementById('app');

// Create a root for the React application
const root = ReactDOM.createRoot(rootElement!); // Use non-null assertion operator (!) to tell TypeScript it's not null

// Render the App component
root.render(
    <React.StrictMode>
        <Provider store={store}>
            <App />
        </Provider>
    </React.StrictMode>
);