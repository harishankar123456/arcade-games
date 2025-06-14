# Arcade Games 🎮

A simple collection of classic arcade-style games implemented in Python using the Turtle graphics module. This repository is ideal for learning.

## Games Included

### 🏓 Ping Pong
- Two-player paddle game.
- Dynamic bouncing ball with edge detection.
- Real-time scoreboard and game-over conditions.
- Modularized codebase for easy understanding and extension.

### 🐍 Snake Game
- Classic snake mechanics: grow after eating food.
- Wall and self-collision detection for challenging gameplay.
- Persistent scoring system and restart functionality.
- Clean, object-oriented code structure.

### 🚦 Turtle Crossing
- Navigate your turtle across a busy road filled with moving cars.
- Increasing difficulty as you advance levels.
- Score tracking and progression system.
- Clear separation of game logic components.

## Getting Started

### Prerequisites
- Python 3.10 or later installed on your system.

### Running the Games

1. **Clone the repository:**
   ```sh
   git clone https://github.com/j-harishankar/arcade-games.git
   cd arcade-games
   ```

2. **Install dependencies:**
   - The games use only the Python standard library (`turtle`). No additional packages are required.

3. **Run a Game:**

   - **Ping Pong**
     ```sh
     cd ping-pong
     python main.py
     ```

   - **Snake Game**
     ```sh
     cd snake-game
     python main.py
     ```

   - **Turtle Crossing**
     ```sh
     cd turtle-crossing-start
     python main.py
     ```

## Folder Structure

```
arcade-games/
│
├── ping-pong/
│   ├── main.py
│   ├── ball.py
│   ├── paddle.py
│   └── scoreboard.py
│
├── snake-game/
│   ├── main.py
│   ├── snake.py
│   ├── food.py
│   └── scoreboard.py
│
├── turtle-crossing-start/
│   ├── main.py
│   ├── player.py
│   ├── car_manager.py
│   └── scoreboard.py
│
└── README.md
```

## Contributing

Contributions, suggestions, and improvements are welcome! Please open an issue or submit a pull request.


---

**Enjoy playing and learning with these classic games!**
