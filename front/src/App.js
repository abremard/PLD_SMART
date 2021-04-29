import logo from './logo.svg';
import './App.css';

import {Route, Switch} from 'react-router-dom';
import Home from "./pages/Home";
import StudioMenu from "./pages/StudioMenu";
import Scratch5 from "./pages/Scratch5";
import Scratch1 from "./pages/Scratch1";
import Match from "./pages/Match";
import Together from "./pages/Together";

function App() {
  return (
    <>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/studio" component={StudioMenu}/>
        <Route exact path="/scratch5" component={Scratch5}/>
        <Route exact path="/scratch1" component={Scratch1}/>
        <Route exact path="/match" component={Match}/>
        <Route exact path="/together" component={Together}/>
      </Switch>
    </>
  );
}

export default App;
