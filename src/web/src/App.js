import logo from './logo.svg';
import './App.css';

export const eel = window.eel
try{
  eel.set_host( 'ws://localhost:8080' )

}catch{

}


async function printOne(){
  let returnValue = await eel.get_one()();
  alert(returnValue, 2);

  //await eel.start_time();

  let dataPoints = await eel.get_random_data_points(300000)();

  await eel.end_time();

  //await eel.start_time();

  let dataPointsJson = JSON.parse(await eel.get_random_data_points_JSON(300000)());

  await eel.end_time();

  //dataPoints = JSON.parse(dataPoints);
  console.log("All data: ", dataPoints);
  
  console.log("Data 0 x: ", dataPoints[0].x, " y: ", dataPoints[0].y);

  console.log("All data JSON: ", dataPointsJson);

}

printOne();

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
