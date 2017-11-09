pragma solidity ^0.4.17;

contract Craps {
  //Owner, Player, State of Game, Player Tracker
  address public creator;
  address[4] public played;
  uint public num_played = 0;
  string state;
  event Played (address player);
  
  // Establish's Owner as the House
  function craps () public {
    creator = msg.sender;
    add_player (msg.sender);
  }
  
  // Adds Players while making sure there aren't duplicates
  function add_player (address player) private {
    for (uint i = 0; i < num_played; i++) {
      require (player != played[i]);
    }
    assert (played[num_played] == 0);
    played[num_played] = player;
    num_played = num_played + 1;
    Played (player);
    if (num_played == played.length) {
      play ();
    }
  }
  
  // Bet and Craps Function with a max bet of .05 eth allowed
  function play () payable{
    require (msg.value <= 500 finney);
    require (num_played < played.length);
    add_player (msg.sender);
    uint128 wager = uint128(msg.value);
    assert (num_played == played.length);
    uint dice = uint(block.blockhash(block.number-1))%6 + 1 + uint(block.blockhash(block.number-1))%6 + 1;
    if(dice == 2 || dice == 3 || dice == 12){
        state = "Defeat"; // They Lost, return nothing 
        return;
    }
    if(dice == 7 || dice == 11){
        state = "Victory"; // They Won, send wager * 2
        msg.sender.transfer(wager * 2);
    }
    while(true){
        state = "ReRoll";
        uint reroll_d = uint(block.blockhash(block.number-1))%6 + 1 + uint(block.blockhash(block.number-1))%6 + 1;
        if(reroll_d == dice){
            state = "Victory";
            msg.sender.transfer(wager * 2);
        }
        if(reroll_d == 7){
            state = "Defeat"; 
            return;
        }
    }
  }
}

      
  
