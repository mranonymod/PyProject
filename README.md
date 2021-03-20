# PyProject

Password Manager made using Python

How to Compile resources.qrc in app.py?

```bash
pyrcc5 resources.qrc -o resources_rc.py
```
then in app.py
```python
import resources_rc
```
