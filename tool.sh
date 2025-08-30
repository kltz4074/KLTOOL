python3 -c "import tkinter; print('Tkinter is installed.')" &> /dev/null

if [ $? -eq 0 ]; then
  echo "Tkinter is available."
  source venv/bin/activate
  python files/scripts/main.py
else
  sudo pacman -S tk
  source venv/bin/activate
  python files/scripts/main.py
fi