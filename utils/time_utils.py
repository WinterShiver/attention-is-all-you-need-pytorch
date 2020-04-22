# -*- coding: utf-8 -*-
# utils/time_decorator.py
# 一个能显示函数执行时间的装饰器。

from functools import wraps
import time

#### time_good_form
#### 返回一个格式很漂亮的当前时间

def time_good_form():
    """返回一个格式很漂亮的当前时间
    @param: None
    @returns: str, showing current time
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



#### time_decorator_with_prompt
#### 装饰一个函数，使这个函数执行结束，就会打印一行提示信息，显示执行时间。

def time_decorator_with_prompt(prompt_infor):
    def time_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            runtime = time.time() - start_time
            print(prompt_infor + ", Time =", round(runtime, 3))
            return result
        return decorated
    return time_decorator


# 使用方式

@time_decorator_with_prompt(prompt_infor = "Calc Successfully")
def foo():
    accu = 0
    for i in range(int(1e6)):
        accu += i
    return 0

# 在调用foo()的时候，执行结束就会打印一行提示信息，显示foo()的执行时间。