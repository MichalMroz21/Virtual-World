<h2>Virtual World</h2>

Project written in C++ using Object Oriented Programming concepts.

It is a virtual world turn based simulation, where different organisms - (plants, animals and human) live together, kill each other and spread (for plants) or breed (for animals).

![Przechwytywanie](https://user-images.githubusercontent.com/125133223/225514099-44d8689a-edfa-4e6b-9738-c3546a2bd5d2.PNG)


After starting the app user can specify board size.


<h4>Each tile has assigned an ASCII character which denotes what organism is currently on it. Detailed description of each organism is below.</h3>
'B' - Borscht - Strength: 10 <br/>
'A' - Antelope - Strength: 4, Initiative: 4 <br/>
'J' - Berries - Strength: 99 <br/>
'T' - Grass - Strength: 0 <br/>
'L' - Fox - Strength: 3, Initiative: 7<br/>
'W' - Wolf - Strength: 9, Initiative: 5<br/>
'C' - Human - Strength: 5, Initiative: 4<br/>
'M' - Dandelion - Strength: 0<br/>
'Z' - Turtle - Strength: 2, Initiative: 1<br/>
'G' - Guarana - Strength: 0<br/>
'O' - Sheep - Strength: 4, Initiative: 4<br/>

All plants have initiative = 0.

Whenever a new turn is started some organisms move randomly (animals), some don't move (plants), in case of collision a stronger organism wins by killing a weaker one or driving it away from tile. Order of moves depends on initiative (in case of same initiative life-time is considered). In case of equal strength, the organism which attacked first wins. Human is an exception in terms of movement - direction of movement has to be chosen before the turn (up, down, left, right) using arrows. Also animals can eat plants.

<h3>More detailed description of organisms:</h3>
Fox - will never move to a tile occupied by an organism with higher strength than his.<br/>
Turtle - In 75% of cases doesn't change it's position (doesn't move), Repels attacks from organisms with strength lower than 5, whoever attacked must return to it's previous tile.<br/>
Antilope - Move range is 2 tiles. Has 50% chance to run away from battle, in that case it moves to another not occupied tile.<br/>
Dandelion - Makes three attempts to spread in one turn.<br/>
Guarana - Increases strength of animal that ate this by 3.<br/>
Berries - Animal that ate this dies.<br/>
Borscht - Kills all animals next to it. If animal eats this, then that animal dies.<br/>

Human has a special ability - shield. When activated it repels animals that move to human's tile. It lasts for 5 turns.




