pragma solidity ^0.4.17;


contract craps {
  address public owner;
  address[4] public played;
  uint public num_played = 0;
  
     enum GameState {
      Started,
      Victory,
      Defeat,
      ReRoll
  }
  GameState state;
  event Played (address player);
  event Won (address player);
  event Lost(address player);
  

  function craps () public {
    owner = msg.sender;
    add_player (msg.sender);
    state = GameState.Started;
  }

  function bet () external payable {
    require (msg.value == 100 finney);
    require (num_played < played.length);
    add_player (msg.sender);
  }

  function add_player (address player) private {
    for (uint i = 0; i < num_played; i++) {
      require (player != played[i]);
    }
    assert (played[num_played] == 0);
    played[num_played] = player;
    num_played = num_played + 1;
    Played (player);
    if (num_played == played.length) {
      playCraps ();
    }
  }
  function playCraps () private {
    assert (num_played == played.length);
    uint player_index = (uint (keccak256 (block.timestamp))) % played.length;
    address player = played[player_index];
    uint dice = uint(block.blockhash(block.number-1))%6 + 1 + uint(block.blockhash(block.number-1))%6 + 1;
    if(dice == 2 || dice == 3 || dice == 12){
        state = GameState.Defeat;
        Lost(player);
        selfdestruct(player);
    }
    if(dice == 7 || dice == 11){
        state = GameState.Victory;
        Won (player);
        selfdestruct (player);
    }
    while(true){
        state == GameState.ReRoll;
        uint reroll_d = uint(block.blockhash(block.number-1))%6 + 1 + uint(block.blockhash(block.number-1))%6 + 1;
        if(reroll_d == dice){
            state = GameState.Victory;
            Won (player);
            selfdestruct (player);
        }
        if(reroll_d == 7){
            state = GameState.Defeat;
            Lost(player);
            selfdestruct(player);
        }
    }
  }
    
  function getState() private constant returns(string) {
    if(state == GameState.Started) return "The Game Has Begun!";
    if(state == GameState.Victory) return "You Won!";
    if(state == GameState.Defeat) return "You Lost!";
    if(state == GameState.ReRoll) return "ReRolling the Dice!";
    
  }
}