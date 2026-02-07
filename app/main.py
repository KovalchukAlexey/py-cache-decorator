from typing import Callable, TypeVar
ReturnType = TypeVar("ReturnType")


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> ReturnType:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_data.keys():
            cache_data[key] = func(*args, **kwargs)
            print("Calculating new result")
        elif key in cache_data.keys():
            print("Getting from cache")
        return cache_data[key]
    return wrapper

#
# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]
#
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
# #
# from typing import Callable, TypeVar, Any
# ReturnType = TypeVar("ReturnType")
#
#
# def cache(func: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
#     cache_data = {}
#
#     def wrapper(*args: Any, **kwargs: Any) -> ReturnType:
#         key = (args, tuple(sorted(kwargs.items())))
#         if key not in cache_data.keys():
#             cache_data[key] = func(*args, **kwargs)
#             print("Calculating new result")
#         elif key in cache_data.keys():
#             print("Getting from cache_data")
#         return cache_data[key]
#     return wrapper