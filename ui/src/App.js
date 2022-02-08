
import './App.css';
import {ApolloProvider} from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import Movies from './components/movies';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql/'
})

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <Movies />
      </div>
    </ApolloProvider>
  );
}

export default App;
