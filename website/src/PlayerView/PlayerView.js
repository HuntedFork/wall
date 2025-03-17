import { useParams } from 'react-router-dom';
import player_games from '../player_games.js';
import './PlayerView.css';

function renderLines(line) {
  return (
    <p className="chatline">{line}</p>
  )
}

function renderGame(game, number) {
   return (
    <div className="game">
      <header className="App-header">
        Game {number}
      </header>
      {game.map(line => renderLines(line))}
    </div>
   );
}

function PlayerView(props) {
  const { number } = props;
  const { id } = useParams();
  const player = id ? id : number;
  var lines = player_games[player];
  var title = "Player #" + player;
  return (
    <div className="App">
        <header className="title"><a href={"/player/"+player} style={{color: 'inherit'}}>{title}</a></header>
        <div className="body">
          {lines.map((line, index) => renderGame(line, index+1))}
        </div>
    </div>
  );
}

export default PlayerView;
