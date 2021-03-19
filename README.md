# PyProject

Password Manager made using Python

How to Compile resources.qrc in main.py?

```bash
pyrcc5 resources.qrc -o resources_rc.py
```
then in main.py
```python
import resources_rc
```
