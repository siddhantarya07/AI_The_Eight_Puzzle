# AI_The_Eight_Puzzle
**Project Description**</br>
The Eight puzzle is a sliding block puzzle that challenges the player to arrange the numbers in increasing order starting from 1 to 8. 
The last tile is an empty block, which helps the player to arrange the tiles. In our project, the Eight puzzles are generalized into the N * N puzzle where 
we have N * N squared tiles with N * N-1 numbers engraved on them and the last tile is a blank tile. The same row and same positioned tiles can be moved 
horizontally or vertically by sliding them respectively. The aim of the N * N puzzle is to place the tiles in numerical order.

We are going to solve the puzzle using 3 search algorithms.</br>
• Uniform Cost Search</br>
• A* with Misplaced Tile Heuristics</br>
• A* with Manhattan Distance Heuristics</br>
</br>
**Project Structure**</br>
This project structure contains 5 files to increase the modularity of the application.</br>
**Main.py:** This file contains the main method which is the starting point of the application. It will 
accept all the required user inputs and pass the selected algorithms to further solve the puzzle.</br>
**Algorithms.py:** This file consists of all the 3 algorithms that we have implemented to solve our 
puzzle. Misplaced tile and Manhattan heuristics are also calculated in the same file and passed 
the value back to the calling algorithm.</br>
**Node.py:** It contains a Node class that creates the object with the required parameters passed. 
Explored moves method explores all the possible movements of the nodes and if possible, it 
creates a node and adds to the explored set.</br>
**Moves.py:** This file contains all 4 possible moves methods. For any tile movement, it checks 
whether the particular movement of tile is possible is not. These are the generic methods that 
work excellent with a puzzle with any N size.</br>
**DisplayOutput.py:** This file contains the methods that help to display the initial state or the 
intermediate and final output in N * N matrix form.</br>
**PlotGraph.py:** This file is used to plot the graph from the data we received from the comparison
of algorithms.</br>
</br>
**How to install and run the project**</br>
The code has been written in Python 3.9.7 and can be cloned from this repository.
Since Main.py contains the main method which is starting point of the application.
The program can be executed by running the **python Main.py** command in the project folder's command prompt.
</br>

Please find the report and code for more details.
