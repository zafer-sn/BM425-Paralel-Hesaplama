import os
from threading import Thread, Lock

# matches neden global değil
# String -> değer tip, referans tip
matches = [] # eslesme callable birinciDegerDegeri
mutex = Lock()
def file_search(root, filename):
    print(f"Searching in {root}")
    child_threads = []
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
    for j in child_threads:
        j.join()
def main():
    t1 = Thread(target=file_search, args=("C:\MUG\Sdk", "tools"))
    t1.start()
    t1.join()
    for m in matches:
        print(f"Matches in {m}")
main()

