from .utils import Comparable
import typing as T
from typing import Any, Optional, Generic, TypeVar

# class TqdmTypeError(TypeError): ...
# class TqdmKeyError(KeyError): ...
#
# class TqdmWarning(Warning):
#    def __init__(
#        self, msg: Any, fp_write: Optional[Any] = ..., *a: Any, **k: Any
#    ) -> None: ...
#
# class TqdmExperimentalWarning(TqdmWarning, FutureWarning): ...
# class TqdmDeprecationWarning(TqdmWarning, DeprecationWarning): ...
# class TqdmMonitorWarning(TqdmWarning, RuntimeWarning): ...
#
# class TqdmDefaultWriteLock:
#    locks: Any = ...
#    def __init__(self) -> None: ...
#    def acquire(self, *a: Any, **k: Any) -> None: ...
#    def release(self) -> None: ...
#    def __enter__(self) -> None: ...
#    def __exit__(self, *exc: Any) -> None: ...
#    @classmethod
#    def create_mp_lock(cls) -> None: ...
#    @classmethod
#    def create_th_lock(cls) -> None: ...
#
# class Bar:
#    ASCII: str = ...
#    UTF: Any = ...
#    BLANK: str = ...
#    frac: Any = ...
#    default_len: Any = ...
#    charset: Any = ...
#    def __init__(
#        self, frac: Any, default_len: int = ..., charset: Any = ...
#    ) -> None: ...
#    def __format__(self, format_spec: Any): ...

_T = TypeVar("_T")

class tqdm(Comparable, Generic[_T]):
    # monitor_interval: int = ...
    # monitor: Any = ...
    # @staticmethod
    # def format_sizeof(num: Any, suffix: str = ..., divisor: int = ...): ...
    # @staticmethod
    # def format_interval(t: Any): ...
    # @staticmethod
    # def format_num(n: Any): ...
    # @staticmethod
    # def ema(x: Any, mu: Optional[Any] = ..., alpha: float = ...): ...
    # @staticmethod
    # def status_printer(file: Any): ...
    # @staticmethod
    # def format_meter(n: Any, total: Any, elapsed: Any, ncols: Optional[Any] = ..., prefix: str = ..., ascii: bool = ..., unit: str = ..., unit_scale: bool = ..., rate: Optional[Any] = ..., bar_format: Optional[Any] = ..., postfix: Optional[Any] = ..., unit_divisor: int = ..., **extra_kwargs: Any): ...
    # def __new__(cls, *args: Any, **kwargs: Any): ...
    @classmethod
    def write(cls, s: Any) -> None: ...
    # @classmethod
    # def external_write_mode(cls, file: Optional[Any] = ..., nolock: bool = ...) -> None: ...
    # @classmethod
    # def set_lock(cls, lock: Any) -> None: ...
    # @classmethod
    # def get_lock(cls): ...
    # @classmethod
    # def pandas(tclass: Any, *targs: Any, **tkwargs: Any): ...
    # iterable: Any = ...
    # disable: Any = ...
    # pos: Any = ...
    # n: Any = ...
    # total: Any = ...
    # leave: Any = ...
    # desc: Any = ...
    # fp: Any = ...
    # ncols: Any = ...
    # nrows: Any = ...
    # mininterval: Any = ...
    # maxinterval: Any = ...
    # miniters: Any = ...
    # dynamic_miniters: Any = ...
    # ascii: Any = ...
    # unit: Any = ...
    # unit_scale: Any = ...
    # unit_divisor: Any = ...
    # lock_args: Any = ...
    # gui: Any = ...
    # dynamic_ncols: Any = ...
    # smoothing: Any = ...
    # avg_time: Any = ...
    # bar_format: Any = ...
    # postfix: Any = ...
    # last_print_n: Any = ...
    # sp: Any = ...
    # last_print_t: Any = ...
    # start_t: Any = ...
    def __init__(
        self,
        iterable: T.Optional[T.Iterable[_T]] = None,
        desc: Optional[str] = None,
        total: Optional[int] = None,
        # leave: bool = ...,
        # file: Optional[Any] = ...,
        # ncols: Optional[Any] = ...,
        # mininterval: float = ...,
        # maxinterval: float = ...,
        # miniters: Optional[Any] = ...,
        # ascii: Optional[Any] = ...,
        # disable: bool = ...,
        # unit: str = ...,
        # unit_scale: bool = ...,
        # dynamic_ncols: bool = ...,
        # smoothing: float = ...,
        # bar_format: Optional[Any] = ...,
        # initial: int = ...,
        position: Optional[int] = None,
        # postfix: Optional[Any] = ...,
        # unit_divisor: int = ...,
        # write_bytes: Optional[Any] = ...,
        # lock_args: Optional[Any] = ...,
        # nrows: Optional[Any] = ...,
        # gui: bool = ...,
        # **kwargs: Any
    ) -> None: ...
    # def __bool__(self): ...
    # def __nonzero__(self): ...
    # def __len__(self): ...
    # def __enter__(self): ...
    # def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    # def __del__(self) -> None: ...
    # def __hash__(self) -> Any: ...
    def __iter__(self) -> T.Iterator[_T]: ...
    def update(self, n: int = ...) -> None: ...
    def close(self) -> None: ...
    # def clear(self, nolock: bool = ...) -> None: ...
    # def refresh(self, nolock: bool = ..., lock_args: Optional[Any] = ...): ...
    # def unpause(self) -> None: ...
    # def reset(self, total: Optional[Any] = ...) -> None: ...
    # def set_description(
    # self, desc: Optional[Any] = ..., refresh: bool = ...
    # ) -> None: ...
    # def set_description_str(
    # self, desc: Optional[Any] = ..., refresh: bool = ...
    # ) -> None: ...
    # def set_postfix(
    # self, ordered_dict: Optional[Any] = ..., refresh: bool = ..., **kwargs: Any
    # ) -> None: ...
    # def set_postfix_str(self, s: str = ..., refresh: bool = ...) -> None: ...
    # def moveto(self, n: Any) -> None: ...
    # @property
    # def format_dict(self): ...
    # def display(self, msg: Optional[Any] = ..., pos: Optional[Any] = ...): ...
    # @classmethod
    # def wrapattr(
    # tclass: Any,
    # stream: Any,
    # method: Any,
    # total: Optional[Any] = ...,
    # bytes: bool = ...,
    # **tkwargs: Any
    # ) -> None: ...

# def trange(*args: Any, **kwargs: Any): ...
