## Requirements

- Python 3.x

---

## Run

Place all project files in the same directory:

```text
aStar.py
board.py
main.py
sokoban.py
state.py
lvl1.txt
lvl2.txt
lvl3.txt
```

Open **Command Prompt** or **PowerShell**, navigate to the project directory, and run:

```bash
python main.py
```

---

## Available Levels

The project includes three sample Sokoban levels:

- `lvl1.txt`
- `lvl2.txt`
- `lvl3.txt`

To run a different level, edit the level filename loaded in `main.py`:

```python
board.load("lvl2.txt")   # or "lvl3.txt"
```

Then run the program again:

```bash
python main.py
```
