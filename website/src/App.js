import { BrowserRouter as Router, Routes, Route, useParams } from 'react-router-dom';
import PlayerView from "./PlayerView/PlayerView";


function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function App() {
  var number = getRandomInt(0,1918);
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PlayerView number={number} />} />
        <Route path="/player/:id" element={<PlayerView number={number} />} />
        <Route path="*" lement={<PlayerView number={number} />} />
      </Routes>
    </Router>
  );
}

export default App;
