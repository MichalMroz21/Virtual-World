# Virtual World

Desktop Application of Virtual World Simulation in 3 different versions - Python, Java and C++.\
Each version improves and expands on what was written previously, in this order C++ -> Java -> Python

## Technologies

<img src="https://github.com/user-attachments/assets/23da0c8e-c353-464a-b8f3-13ca77abad9d" alt="drawing" width="75"/>
<img src="https://github.com/user-attachments/assets/77a1189f-d290-47f5-8672-6db4406c109f" alt="drawing" width="75"/>
<img src="https://github.com/user-attachments/assets/4c3e8037-a888-4564-ae68-1dbc9ddef725" alt="drawing" width="75"/>
<img src="https://github.com/user-attachments/assets/cd65f45b-4869-4cd7-8ee3-fdb3a75e5dfe" alt="drawing" width="75"/>

## Demo

It is a virtual world turn based simulation, where different organisms - (plants, animals and human) live together, kill each other and spread (for plants) or breed (for animals).

![Przechwytywanie](https://user-images.githubusercontent.com/125133223/225217787-9397eb83-104d-4e76-b908-fc3827af0ae0.PNG)

When starting the app allows user to specify board size and whether it consists of square tiles or hex

![Przechwytywanie](https://user-images.githubusercontent.com/125133223/225218474-531161fa-63bf-41ba-8bac-f038261d48c5.PNG)

<h3>Each tile has assigned a color which denotes what organism is currently on it. Detailed description of each organism is below.</h3>
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

All plants have initiative = 0.

Whenever a new turn is started some organisms move randomly (animals), some don't move (plants), in case of collision a stronger organism wins by killing a weaker one or driving it away from tile. Order of moves depends on initiative (in case of same initiative life-time is considered). In case of equal strength, the organism which attacked first wins. Human is an exception in terms of movement - direction of movement has to be chosen before the turn (up, down, left, right). Also animals can eat plants.

<h3>Additionaly there are features:</h3>
- New organisms can be added to board by simply clicking the square (the one with color and letter in right down corner), selecting the organism and clicking on tile on board.<br/>
- World can be saved into a text file and loaded.<br/>
- Event Log with paging containing detailed information of what happened during the turn.<br/>

<h3>More detailed description of organisms:</h3>
Fox - will never move to a tile occupied by an organism with higher strength than his.<br/>
Turtle - In 75% of cases doesn't change it's position (doesn't move), Repels attacks from organisms with strength lower than 5, whoever attacked must return to it's previous tile.<br/>
Antilope - Move range is 2 tiles. Has 50% chance to run away from battle, in that case it moves to another not occupied tile.<br/>
Cybersheep - It's goal is to eat Borscht. If there is Borscht it moves to it's direction, if there is not it acts as a normal sheep.<br/>
Dandelion - Makes three attempts to spread in one turn.<br/>
Guarana - Increases strength of animal that ate this by 3.<br/>
Berries - Animal that ate this dies.<br/>
Borscht - Kills all animals next to it, except Cybersheep. If animal eats this, then that animal dies.<br/>

Human has a special ability - shield. When activated it repels animals that move to human's tile. It lasts for 5 turns.




