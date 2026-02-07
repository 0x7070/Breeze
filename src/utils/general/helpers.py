__all__ = [
    'hr',
    'hrx'
]

def hr(char: str = None, size: int = None) -> None:
    if char is None:
        char = '-'
    if size is None:
        size = 30
    print(f'{char*size}')
    
def hrx() -> None:
    """
    `hrx` -- Horizontal Rule 2.

    Large horizontal rule

    Args:
        NA

    Returns:
        NA
    
    Raises:
        NA

    Example:
        >>> hrx()
        expected_output:
        ```
        
        ====================
        
        ```
    """
    print()
    hr(
        char='=',
        size=80
    )    
    print()
    
def _title(string: str = None, char: str = None, width: int = None,
           spaces: int = None, return_val: bool = None) -> str:
    if char is None:
        char = '~'
    if width is None:
        width = 80
    if spaces is None:
        spaces = 5
    if string is None:
        string = 'default'
    if return_val is None:
        return_val = False

    formatting = [
        str.strip,
        #str.title
    ]
    for func in formatting:
        #print(f'PRE  {func.__name__}: `{string}`')
        string = func(string)
        #print(f'POST {func.__name__}: `{string}`')
        #_hr()

    string = f'{' '*spaces}{string}{' '*spaces}'
    string = f'{string:{char}^{width}}'

    if return_val:
        return string
    else:
        print(string)

if __name__ == '__main__':
    print('helpers package LOADED')