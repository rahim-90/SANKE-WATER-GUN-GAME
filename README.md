# SANKE-WATER-GUN-GAME
Snake-Water-Gun Game - Python

This is a simple command-line Python game based on the classic "Snake, Water, Gun" logic.

---

🎮 Game Rules:
1 = Snake  
2 = Water  
3 = Gun

User inputs:
- 's' for Snake  
- 'w' for Water  
- 'g' for Gun

---

🛠️ How It Works:
- The computer randomly chooses one option: Snake, Water, or Gun.
- The player inputs their choice using a single letter: 's', 'w', or 'g'.
- The program compares both choices and displays who wins based on the rules.

---

⚔️ Game Logic:
- Snake drinks water → Snake wins
- Water drowns gun → Water wins
- Gun kills snake → Gun wins

All other scenarios are handled to determine win, lose, or draw.

---

📦 Requirements:
- Python 3.x
- No external libraries required (only built-in `random` module)

---

💻 How to Play:
1. Run the Python script.
2. Input your choice when prompted (s, w, or g).
3. The computer makes a random choice.
4. The result is printed on the screen.

---

🚫 Invalid Input:
If the user enters anything other than 's', 'w', or 'g', an error message is shown.

---

📌 Example:
Enter your choice: g  
you chose: gun  
computer chose: snake  
you win

