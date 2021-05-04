#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        except TypeError:
            print("size must be an integer")
            raise
        except ValueError:
            print("size must be >= 0")
            raise
