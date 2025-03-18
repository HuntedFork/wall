import { useSearchParams } from 'react-router-dom';
import player_games from '../player_games.js';
import './PlayerView.css';

function renderLines(line) {
  const text = line.replace(/(gg)/gi, '<span class="gg">$1</span>');
  return (
    <p className="chatline" dangerouslySetInnerHTML={{__html: text}} />
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
  const [searchParams, setSearchParams] = useSearchParams();
  const search = searchParams.get('player');
  const { number } = props;
  var player = number
  if (search !== null) {
    player = Number(search);
  }
  var lines = player_games[player];
  var title = "Player #" + player;
  return (
    <div className="App">
        <header className="title"><a href={"/wall/?player="+player} style={{color: 'inherit'}}>{title}</a></header>
        <div className="body">
          {lines.map((line, index) => renderGame(line, index+1))}
        </div>
    </div>
  );
}

export default PlayerView;
