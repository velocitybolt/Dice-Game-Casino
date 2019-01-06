pragma solidity ^0.4.17;
// Author: Murtaza Meerza
contract Craps {
  //Owner, Player, State of Game, Player Tracker, Wager, Sum of Two Die, Control Bool
  address public creator;
  address[4] public played;
  uint256 wager;
  uint256 dice;
  uint256 dice_sum;
  bool control = false;
  uint public num_played = 0;
  event Played (address player);
  
  // Establish's Owner as the House
  function Craps () public {
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
    if (num_played == played.length){
        playCraps();
    }
  }
  // Function that rolls two die generated using block timestamp; returns dicesum to ensure it works
  function dice_roll () returns (uint256 dice_sum){
      uint dice_one = uint(keccak256(block.timestamp))%6 +1;
      uint dice_two = uint(keccak256(block.timestamp))%6 +1;
      dice_sum = dice_one + dice_two;
  }
  // Function that sets up that bet
  function play () external payable{
    require (msg.value <= 500 finney);
    require (num_played < played.length);
    add_player (msg.sender);
    wager = this.balance; // < -- the eth stored within contract 
  }
  
  // function thats pays the winner 
  function payout () external payable{
      msg.sender.transfer(wager * 2);
  }
  // Function that plays craps and determines winner
  function playCraps() public returns (bool result){
      assert (num_played == played.length);
      uint256 dice = uint(keccak256(block.timestamp))%6 +1 + uint(keccak256(block.timestamp))%6 +1;
      if(dice == 2 || dice == 3 || dice == 12){
          control = true;
          result = false;
      } 
      if(dice == 7 || dice == 11){
          control = true;
          result = true;
      }
      while(!control){
          if(dice_sum == dice){
              control = true;
              result = true;
          }
          if(dice_sum == 7){
              control = true;
              result = false;
          }
      }
  }


}
