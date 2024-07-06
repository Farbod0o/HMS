from HMS.model.tools.logger import Logger


def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            output = function(*args, **kwargs)
            if not "find" in function.__name__:
                Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output[1]}")
            else:
                Logger.info(f"{function.__qualname__}{args[1:]}")
            return output
        except Exception as e:
            print(f"**{e}")
            # e.with_traceback()
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : {e}")
            return False, str(e)

    return inner


def log(function):
    def inner(*args, **kwargs):
        output = function(*args, **kwargs)
        if not "find" in function.__name__:
            Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output[1]}")
        else:
            Logger.info(f"{function.__qualname__}{args[1:]}")
        return output

    return inner