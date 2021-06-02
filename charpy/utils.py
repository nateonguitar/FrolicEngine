import os
import time
from typing import Union

if os.name == "nt":
    import ctypes


def clamp(value: Union[float, int], lower: Union[float, int], upper: Union[float, int]) -> Union[float, int]:
    """
    Clamp a number
    Same as min(max((value, lower), higher)

    Args:
        value (Union[float, int]): Value to clamp
        lower (Union[float, int]): min value
        upper (Union[float, int]): max value

    Returns:
        Union[float, int]: clamped value
    """
    return lower if value < lower else upper if value > upper else value


def timestamp() -> float:
    """
    Returns fractional seconds of a performance counter.
    It does include time elapsed during sleep and is system-wide

    Note: The reference point of the returned value is undefined,
    so that only the difference between the results of two calls is valid.

    Returns:
        float: fractional seconds
    """
    return time.perf_counter()


def _time_error(err, func, args):
    """
    Throw exception or error on platform _time_error
    """
    if err:
        if os.name == "posix":
            raise Exception(f"{func.__name__} error {err}")
        if os.name == "nt":
            raise WindowsError(f"{func.__name__} error {err}")
    return args


class PerformanceSleep:
    """
    Needed to abstract away window's ~15ms imprecise over sleep() method.
    """

    def __init__(self, milliseconds: int = 1):
        self.milliseconds = milliseconds

        if os.name == "nt":
            self.winmm = ctypes.WinDLL("winmm")
            self.winmm.timeGetDevCaps.errcheck = _time_error
            self.winmm.timeBeginPeriod.errcheck = _time_error
            self.winmm.timeEndPeriod.errcheck = _time_error

    def __enter__(self):
        if os.name == "nt":

            class TIMECAPS(ctypes.Structure):
                _fields_ = (("wPeriodMin", ctypes.wintypes.UINT), ("wPeriodMax", ctypes.wintypes.UINT))

            caps = TIMECAPS()
            self.winmm.timeGetDevCaps(ctypes.byref(caps), ctypes.sizeof(caps))
            self.milliseconds = clamp(self.milliseconds, caps.wPeriodMin, caps.wPeriodMax)
            self.winmm.timeBeginPeriod(self.milliseconds)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if os.name == "nt":
            self.winmm.timeEndPeriod(self.milliseconds)


def safe_sleep(amount: float):
    """
    Suspend execution of the calling thread for the given number of seconds

    Args:
        amount (float): time to sleep, in fractional seconds
    """
    with PerformanceSleep(milliseconds=1):
        time.sleep(amount)
