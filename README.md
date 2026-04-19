# 👻 Ghost in the Machine

Hey! This is a small project I built to practice **Object-Oriented Programming (OOP)** in Python. 

I'm currently a 1st-year student in the **Digital Development** program at **ISTAG Bab Tizimi (OFPPT)**, and I wanted to move beyond basic scripts and build something that actually interacts with my system.

## 💡 The Idea
I call it "Ghost in the Machine." It’s a modular system monitor that watches my PC's hardware. Instead of just looking at boring numbers in a terminal, I programmed it to send me real Windows notifications (using `plyer`) when my CPU or RAM starts to struggle. 

Basically, the computer "talks" to me when it's getting overwhelmed.

## 🛠️ What I practiced with this:
* **Abstraction & Interfaces:** Using the `abc` module to make sure every sensor I build follows the same rules.
* **Polymorphism:** The monitor doesn't care if it's checking CPU or RAM; it just calls the same methods on different objects.
* **System Interfacing:** Using `psutil` to grab real hardware data.
* **Clean Code:** Keeping the "Brain" (Monitor) separate from the "Voice" (Notifier).

## 🚀 How to try it out:
Since I'm still learning, I kept the setup simple:

1.  **Clone it:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ghost-monitor.git](https://github.com/YOUR_USERNAME/ghost-monitor.git)
    ```
2.  **Install the tools:**
    ```bash
    pip install psutil plyer
    ```
3.  **Run it:**
    ```bash
    python main.py
    ```

## 📌 Future Plans
Since I'm just starting my journey at ISTAG, I plan to add more to this as I learn:
- [ ] Move thresholds to a `config.json` file.
- [ ] Add a "Ghost Personality" class for random funny messages.
- [ ] Maybe a simple web dashboard using Flask.

---
**Student:** Ayman  
**Level:** 1st Year Digital Development @ ISTAG Bab Tizimi  
*Just learning and building one script at a time!*