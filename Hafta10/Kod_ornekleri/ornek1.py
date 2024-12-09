import os
from threading import Thread, Lock

from wait_group import WaitGroup

# matches neden global değil
# String -> değer tip, referans tip
matches = [] # eslesme callable birinciDegerDegeri
mutex = Lock()
def file_search(root, filename, wait_group):
    print(f"Searching in {root}")
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(full_path, filename, wait_group))
            t.start()
    wait_group.done()
def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t1 = Thread(target=file_search, args=("C:\MUG\Sdk", "tools", wait_group))
    t1.start()
    wait_group.wait()
    for m in matches:
        print(f"Matches in {m}")
main()

