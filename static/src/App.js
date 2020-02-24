import React, { Component } from 'react';
import './App.css';
import Appbar from './Appbar';
import withFirebaseAuth from 'react-with-firebase-auth'
import * as firebase from 'firebase/app';
import 'firebase/auth';
import firebaseConfig from './firebaseConfig';
import HomePage from './HomePage';
import Container from '@material-ui/core/Container';


const firebaseApp = firebase.initializeApp(firebaseConfig);

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      isLoggedIn : true,
    }
  }
  render() {
    // const {
    //   user,
    //   signOut,
    //   signInWithGoogle,
    // } = this.props;
    //if(this.props.isLoggedIn){
      return(
        <Container>
          <Appbar/>
          <HomePage/>
        </Container>
      );
    //}
    // else{
    //   return (
    //     <div className="App">
    //       <h2>Data Manager</h2>
    //       <header className="App-header">
    //         {
    //           user
    //             ? <p>Hello, {user.displayName}</p>
    //             : <p>Please sign in.</p>
    //         }
    //         {
    //           user
    //             ? <button onClick={signOut}>Sign out</button>
    //             : <button onClick={signInWithGoogle}>Sign in with Google</button>
    //         }
    //       </header>
    //     </div>
    //   );
    // }
  }
}

const firebaseAppAuth = firebaseApp.auth();

const providers = {
  googleProvider: new firebase.auth.GoogleAuthProvider(),
};

export default withFirebaseAuth({
  providers,
  firebaseAppAuth,
})(App);