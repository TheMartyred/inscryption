# inscryption
A discord bot version of the game inscryption that I am working on

This bot is still a work in progress, but if you'd like to add it to your server, you can use this link
https://discord.com/api/oauth2/authorize?client_id=917175698299441203&permissions=8&scope=bot

Doesn't do much currently in the way of actually playing the game, but can demonstrate functionality that will be needed later when the game is actually functional

**CURRENT FUNCTIONALITY**

!create-channel [name="real-python"] 
  creates a channel with the provided name
  
!Inscrybe [opponent="bot"]
  prints a message responding to the person who triggered it by name
  
!test-cards [card="Stunted_wolf"]
  tests printing a composite image of multiple card images to the chat, the first of which is decided by the name provided
  
!test-boardprint
  tests printing a composite image that represents a boardstate with cards that have sigils added to them dynamically
  
!test-card-class
  tests creating a new card object, printing its info, altering it, then printing it again. Does not support the sigil functionality yet
  
!test-glitch
  tests printing a "glitched" card which is represented by an animated gif
  
!test-cardprint
  tests printing a composite image of a card with added sigils
