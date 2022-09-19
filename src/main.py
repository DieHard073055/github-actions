from option import Result, Ok, Err
from typing import Type

class NumberTooSmallException(Exception):
    pass


def add(a: int, b: int) -> Result[int, Type[NumberTooSmallException]]:
    if a < 10 or b < 10:
        return Err(NumberTooSmallException)
    else:
        return Ok(a + b)

def sub(a: int, b: int) -> Result[int, Type[NumberTooSmallException]]:
    if a < 10 or b < 10:
        return Err(NumberTooSmallException)
    else:
        return Ok(a - b)



def main():
    result = add(10, 20)
    print(result.unwrap_or(-1))
    result = sub(10, 20)
    print(result.unwrap_or(-1))

if __name__ == '__main__':
    main()
