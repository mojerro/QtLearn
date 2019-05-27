# QtLearn
learn Qt with python
```bash
# generate Qt UI file in python
pyside2-uic ./UI/main.ui > ./UI/ui_main.py
pyside2-uic ./UI/josephus_circle.ui > ./UI/ui_josephus_circle.py
pyside2-uic ./UI/nine_patch.ui > ./UI/ui_nine_patch.py
pyside2-uic ./UI/a_star.ui > ./UI/ui_a_star.py

# generate Qt resource control file in python
pyside2-rcc -o ./UI/static_rc.py ./UI/static.qrc
```
