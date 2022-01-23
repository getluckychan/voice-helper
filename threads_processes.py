from recognize import *
from multiprocessing import *
from listener import *
from ctypes import c_char_p


# def list_to_string(s):
#     str1 = ""
#     return str1.join(s)
#
#
# def f(a):
#     for i in range(len(a)):
#         a[i] = a[i]
#
#
# def recognize_process():
#     arr = Array('i', [ord(c) for c in converting()])
#     p = Process(target=f, args=(arr,))
#     p.start()
#     p.join()
#     voice = list_to_string([chr(c) for c in arr[:]])
#     return voice
#
#
# def opening_process():
#     OpenCommand(recognize_process()).check()
#
#
# if __name__ == '__main__':
#     opening_process()


if __name__ == '__main__':
    manager = Manager()
    string = manager.Value(c_char_p, converting())
    process = Process(target=OpenCommand.check, args=(string,))
    process.start()
    process.join()
    print(string.value)
