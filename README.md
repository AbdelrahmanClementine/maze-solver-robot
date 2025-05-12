🧱 e-puck Maze Solver using Wall-Following Algorithm
This project demonstrates a simple maze-solving robot using the e-puck robot simulated in Webots. The robot follows the wall-following algorithm to navigate and eventually solve a maze.

🚀 Features
Uses left-wall-following (or configurable for right-wall-following).

Simulated in Webots, a professional robot simulator.

Based on the e-puck robot model, widely used in research and education.

Detects and navigates through walls using proximity sensors.

Modular and easy to modify for alternative navigation strategies.

🧠 Algorithm
The wall-following algorithm works by:

Keeping one side of the robot (left or right) close to a wall.

Continuously adjusting movement based on sensor feedback.

Turning at intersections or dead ends to continue following the chosen wall.

This approach guarantees solving any simply-connected maze (i.e., one without loops).
