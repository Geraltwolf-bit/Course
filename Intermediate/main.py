def get_sum(a: int, b: int) -> int:
    return a + b
    
def show_user_info(name: str, age: int, city: str) -> None:
    print(f'User: {name}\nAge: {age}\nCity: {city}')
    
def get_total(numbers: list[int]) -> int:
    return sum(numbers)
    
def get_user_value(d: dict[int, str], key: int) -> int:
    return d[key]
    
def show_full_name(first: str, last: str, middle=None) -> None:
    if middle:
        print(f"{first} {middle} {last}")
    print(f"{first} {last}")
    
def get_positives(values: list[int]):
    return [v for v in values if v > 0]