import weakref
from memory_profiler import profile
from utils import timeit


class VirtualProcessorCore:
    def __init__(self, number):
        self.number = number
        self.power_consumption = 0


class SimpleProgram:
    def __init__(self, core):
        self.core = core


class ProgramWithSlots:
    __slots__ = ("core",)

    def __init__(self, core):
        self.core = core


class ProgramWithWeakRef:
    def __init__(self, core: weakref.ref):
        self.core = core


COUNT_OBJECTS = 1_000_000

all_cores = [
    [VirtualProcessorCore(i) for i in range(COUNT_OBJECTS)],
    [VirtualProcessorCore(i) for i in range(COUNT_OBJECTS)],
    [VirtualProcessorCore(i) for i in range(COUNT_OBJECTS)],
]

weakrefs = [weakref.ref(core) for core in all_cores[2]]


@timeit
def create(cls_type, cores: list):
    return [cls_type(cores[i]) for i in range(len(cores))]


TEST_SIZE = 10


@timeit
def access(programs, refs: bool = False):
    if refs:
        for _ in range(TEST_SIZE):
            for program in programs:
                number = program.core().number
    else:
        for _ in range(TEST_SIZE):
            for program in programs:
                number = program.core.number


@timeit
def change(programs, refs: bool = False):
    if refs:
        for _ in range(TEST_SIZE):
            for program in programs:
                program.core().power_consumption += 1
    else:
        for _ in range(TEST_SIZE):
            for program in programs:
                program.core.power_consumption += 1


@timeit
def delete(programs, refs: bool = False):
    if refs:
        for program in programs:
            del program.core().power_consumption
    else:
        for program in programs:
            del program.core.power_consumption


@profile
def run_all():
    simple_result = create(SimpleProgram, all_cores[0], name="create_simple")
    slots_result = create(ProgramWithSlots, all_cores[1], name="create_slots")
    weakrefs_result = create(ProgramWithWeakRef, weakrefs, name="create_weakrefs")
    print("----------------------------------------------")
    access(simple_result, name="access_simple")
    access(slots_result, name="access_slots")
    access(weakrefs_result, refs=True, name="access_weakrefs")
    print("----------------------------------------------")
    change(simple_result, name="change_simple")
    change(slots_result, name="change_slots")
    change(weakrefs_result, refs=True, name="change_weakrefs")
    print("----------------------------------------------")
    delete(simple_result, name="delete_simple")
    delete(slots_result, name="delete_slots")
    delete(weakrefs_result, refs=True, name="delete_weakrefs")


if __name__ == "__main__":
    run_all()
