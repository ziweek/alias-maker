import sys
import os

inp = list(sys.argv)
str_dir = inp[1]
li_dir = os.listdir(str_dir)
result = [e for e in li_dir if e[0] != "."]

print()
print("--- alias maker ---")
print(f'Detected Folders : \n{result}')
print()
for e in result:
    print(f'alias {e}="cd {str_dir}/{e}; ls -l"')
print("---             ---")
print()