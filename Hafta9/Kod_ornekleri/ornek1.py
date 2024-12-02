import os
# matches neden global değil
matches = [] # eslesme callable birinciDegerDegeri
def file_search(root, filename):
    print(f"Searching in {root}")
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if filename in file:
            matches.append(full_path)
        if os.path.isdir(full_path):
            file_search(full_path, filename)
def main():
    file_search("C:\MUG\Sdk", "tools")
    for m in matches:
        print(f"Matches in {m}")
main()
