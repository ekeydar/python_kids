<div dir="rtl">

תרגילים בפונקציות
================

# תרגיל ראשון 
כתבו פונקציה שמקבלת 2 מחרוזות ומחזירה את הארוכה מביניהן
אם המחרוזות באותו אורך, החזירו את הפרמטר הראשון

<div dir="ltr">

```python
def find_longest(s1, s2):
    pass # COMPLETE
```

</div>
 
 כדי לבדוק את הפונקציה שכתבתם, הריצו את השורות הבאות
 
 אם קיבלתם שגיאה באחת השורות, אז יש לכם טעות בפונקציה
 
<div dir="ltr"> 

```python
assert find_longest("abc", "aa") == "abc"
assert find_longest("aa", "abc") == "abc"
assert find_longest("zz", "") == "zz"
assert find_longest("aaa", "zz") == "aaa"
assert find_longest("aaa", "bbb") == "aaa"
``` 

</div>

את הפתרון אפשר לראות כאן [ex1.py](./ex1.py) 


# תרגיל שני 
כתבו פונקציה שמקבלת תוצאה של משחק כדורגל ומחזירה שני מספרים שהם הנקודות שכל קבוצה קיבלה

<div dir="ltr">

```python
def get_points(goals1, goals2):
    pass # COMPLETE
```

</div>

 כדי לבדוק את הפונקציה שכתבתם, הריצו את השורות הבאות

 אם קיבלתם שגיאה באחת השורות, אז יש לכם טעות בפונקציה
 
**שימו לב**
בשביל להחזיר 2 מספרים מפונקציה כותבים את שני 
המספרים מופרדים בפסיק. דומה לזה:

<div dir="ltr">

```python
    return 3, 0
```

</div>

<div dir="ltr"> 

 ```python
assert get_points(2, 2) == (1, 1)
assert get_points(1, 0) == (3, 0)
assert get_points(1, 4) == (0, 3)
``` 

</div>

את הפתרון אפשר לראות כאן [ex2.py](./ex2.py) 

</div>