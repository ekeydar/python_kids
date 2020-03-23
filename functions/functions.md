תרגילים בפונקציות
================

# תרגיל ראשון 
כתבו פונקציה שמקבלת 2 מחרוזות ומחזירה את הארוכה מביניהן
אם המחרוזות באותו אורך, החזירו את הפרמטר הראשון

```python
def find_longest(s1, s2):
    pass # COMPLETE
```
 כדי לבדוק את הפונקציה שכתבתם, הריצו את השורות הבאות
 
 אם קיבלתם שגיאה באחת השורות, אז יש לכם טעות בפונקציה
 ```python
assert find_longest("abc", "aa") == "abc"
assert find_longest("aa", "abc") == "abc"
assert find_longest("zz", "") == "zz"
assert find_longest("aaa", "zz") == "aaa"
assert find_longest("aaa", "bbb") == "aaa"
``` 
את הפתרון אפשר לראות כאן

[ex1.py](./ex1.py) 
