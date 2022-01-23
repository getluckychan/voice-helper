from recognize import *
from multiprocessing import *
from listener import *
from ctypes import c_char_p


list_of_processes = [

]


def processes():
    process_open = Process(target=check_open, args=(string,))
    process_sound = Process(target=check_sound, args=(string,))
    process_sys = Process(target=check_sys, args=(string,))
    process_open.start()
    process_sound.start()
    process_sys.start()
    list_of_processes.append(process_open)
    list_of_processes.append(process_sound)
    list_of_processes.append(process_sys)


if __name__ == '__main__':
    while True:
        manager = Manager()
        string = manager.Value(c_char_p, converting())
        processes()
        for process in list_of_processes:
            process.join()

