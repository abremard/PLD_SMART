import logo from './logo.svg';
import './App.css';

import {Route, Switch} from 'react-router-dom';
import Home from "./pages/Home";
import StudioMenu from "./pages/StudioMenu";

function App() {
  return (
    <>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/studio" component={StudioMenu}/>
      </Switch>
    </>
  );
}

export default App;
