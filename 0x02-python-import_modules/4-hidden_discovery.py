#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4 as hidden

    for name in dir(hidden):
        # you can use this condition also "if not name.startswith('__'): "
        if name[0:2] != '__':
            print(name)
