# Puzzle-AI-Evolution-in-Action

The code is a Python program using the Pygame library to create a puzzle game where enemies collect colored foods to gain points. It uses the NEAT algorithm to control the game's behavior. The code initializes the Pygame environment, sets up the game window, and defines classes for text, food, and enemy objects. It also implements the algorithm.

[![Static Badge](https://img.shields.io/badge/random,-blue)](https://pypi.org/project/random,/)
[![Static Badge](https://img.shields.io/badge/neat,-purple)](https://pypi.org/project/neat,/)
[![Static Badge](https://img.shields.io/badge/matplotlib-pink)](https://pypi.org/project/matplotlib/)
[![Static Badge](https://img.shields.io/badge/pygame-orange)](https://pypi.org/project/pygame/)

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 7/10](#Rating)

# About

This Python program uses the Pygame library to create a puzzle game where enemies collect colored foods, earning points based on their color. The game is controlled by a neural network trained using the NEAT algorithm. The code initializes the Pygame environment, sets up the game window, and defines colors and text rendering. It creates classes for text, food, and enemy objects, defines logic functions for adding food, handling collisions, and updating the game state. It also implements the NEAT algorithm for evolving neural networks and defines functions for evaluating genomes and running the NEAT algorithm.

# Features

The Python program for a puzzle game includes initializing the environment, setting up the main display window, defining color and text rendering, class definitions, game logic functions, adding food, handling collisions, updating game state, and implementing the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. The game uses the NEAT algorithm to evolve neural networks controlling enemies, and the game's performance is assessed through genome evaluation. The NEAT execution runs the algorithm to train and improve the neural networks based on their performance. This structure provides a solid foundation for the game, where the challenge comes from the evolving intelligence of enemy characters. The use of NEAT allows for dynamic learning and adaptation, potentially increasing the game's difficulty as the neural networks become more efficient at collecting food. This creative way to combine game development with machine learning is a creative way to combine game development with machine learning.

# Imports

pygame, pygame.sprite, random, sys, pymunk, neat, os, math, matplotlib.pyplot 

# Rating

The code uses a simple neural network-based algorithm using the NEAT library to train and evolve agents to navigate a maze-like environment and collect food. It is easy to read and understand, with clear variable and function names. The code is moderately modular, with components like the `Food` and `Enemies` classes encapsulating their respective functionalities. Important sections of the code are commented for better understanding.
However, the code has some cons, such as the extensive use of global variables, which could lead to issues with variable scope, readability, and maintainability. Refactoring to reduce reliance on global variables is recommended. The code could benefit from further organization and structuring, particularly by separating the main loop logic from the NEAT algorithm evaluation. Define constants for magic numbers, such as screen dimensions, food generation intervals, and enemy speeds, at the beginning of the code or in a separate configuration file for easier modification.
To improve the code, refactor the code to minimize global variables, separate the NEAT algorithm evaluation logic from the main loop logic, define constants for magic numbers, and implement robust error handling mechanisms, such as try-except blocks, to handle potential errors during file I/O operations, library calls, or unexpected conditions.
