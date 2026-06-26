from typing import Optional, Tuple, Dict, List

class State:
    def __init__(self, name: str):
        self.name = name

unauthorized = State("unauthorized")
authorized = State("authorized")

def check_login(param: Optional[str], password: str, balance: int) -> Tuple[bool, int, Optional[any]]:
    if param == password:
        return True, balance, None
    return False, balance, None

def check_logout(param: Optional[any], password: str, balance: int) -> Tuple[bool, int, Optional[any]]:
    return True, balance, None

def check_deposit(param: Optional[int], password: str, balance: int) -> Tuple[bool, int, Optional[any]]:
    amount = int(param) if param is not None else 0
    return True, balance + amount, None

def check_withdraw(param: Optional[int], password: str, balance: int) -> Tuple[bool, int, Optional[any]]:
    amount = int(param) if param is not None else 0
    if balance >= amount:
        return True, balance - amount, None
    return False, balance, None

def check_balance(param: Optional[any], password: str, balance: int) -> Tuple[bool, int, Optional[any]]:
    return True, balance, balance

transition_table: Dict[State, List[Tuple[str, callable, State]]] = {
    unauthorized: [
        ("login", check_login, authorized)
    ],
    authorized: [
        ("logout", check_logout, unauthorized),
        ("deposit", check_deposit, authorized),
        ("withdraw", check_withdraw, authorized),
        ("balance", check_balance, authorized)
    ]
}
