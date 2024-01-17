def example(mandatory, default = 'Default', *args, **kwargs):
    print(f"""
        mandatory = {mandatory}
        default = {default}
        args = {args}
        kwargs = {kwargs}
        """)


example(3)

example(3, 45)

# *args - dozvoljava bilo koji broj parametara
example(3, 'String 1', 'String 2', 'String 3')

# **kwargs - rjecnik
example(3, 'String 1', 'String 2', 'String 3', k1='v1', k2='v2')

# mijenjanje redosljeda
example(k1 = 'v1', k2 = 'v2', default='Default', mandatory=5)

#----------------------------------------------------------------

# slanje parametara redom pomocu liste i rjecnika
list1 = [1, 2, 3, 4]
dict1 = {'k1': 'v1', 'k2': 'v2'}
example(*list1, **dict1)
