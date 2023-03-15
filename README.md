<h2>Virtual World</h2>

Project written with Python using Pygame and Object Oriented Programming concepts.

![Przechwytywanie](https://user-images.githubusercontent.com/125133223/225217787-9397eb83-104d-4e76-b908-fc3827af0ae0.PNG)

It is a virtual world turn based simulation, where different organisms - (plants, animals and human) live together, kill each other and spread (for plants) or breed (for animals).



When starting the app allows user to specify board size and whether it consists of square tiles or hex.

![Przechwytywanie](https://user-images.githubusercontent.com/125133223/225218474-531161fa-63bf-41ba-8bac-f038261d48c5.PNG)


Each tile has assigned a color which denotes what organism is currently on it. Detailed description of each organism is below. <br/>
Red(B) - Borscht - Strength: 10 <br/>
Orange(A) - Antelope - Strength: 4, Initiative: 4 <br/>
Violet(J) - Berries - Strength: 99 <br/>
Green(T) - Grass - Strength: 0 <br/>
Dark Blue(L) - Fox - Strength: 3, Initiative: 7<br/>
Brown(W) - Wolf - Strength: 9, Initiative: 5<br/>
Pink(C) - Human - Strength: 5, Initiative: 4<br/>
Yellow(M) - Dandelion - Strength: 0<br/>
Light Blue(Z) - Turtle - Strength: 2, Initiative: 1<br/>
Gray(G) - Guarana - Strength: 0<br/>
Cyan(O) - Sheep - Strength: 4, Initiative: 4<br/>
Light Gray(o) - Cybersheep - Strength: 11, Initiative: 4<br/>

Whenever a new turn is started some organisms move randomly (animals), some don't move (plants), in case of collision a stronger organism wins by killing a weaker one or driving it away from tile. Order of moves depends on initiative (in case of same initiative life-time is considered). In case of equal strength, the organism which attacked first wins. Human is an exception in terms of movement - direction of movement has to be chosen before the turn (up, down, left, right). Also animals can eat plants.

Additionaly there are features:
- New organisms can be added to board by simply clicking the square (the one with color and letter in right down corner), selecting the organism and clicking on tile on board.
- World can be saved into a text file and loaded
- Event Log with paging containing detailed information of what happened during the turn.


