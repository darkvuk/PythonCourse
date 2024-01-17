# FINALLY I ELSE

try:
    9 / 1
except ZeroDivisionError:           # ulazi ako je doslo do errora
    print('EXCEPT')
else:                               # ulazi ako nije doslo do errora
    print('ELSE')
finally:                            # ulazi svakako
    print('FINALLY')

"""
Ako dodje do ZeroDivisionError:
EXCEPT
FINALLY
"""

"""
Ako ne dodje do ZeroDivisionError:
ELSE
FINALLY
"""