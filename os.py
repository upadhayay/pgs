import os
import subprocess

compile_cmd=["gcc", "-o","m","m.c"]
execute_cmd=["m.exe"]

abc= subprocess.Popen(compile_cmd)
compileM = subprocess.Popen(execute_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("\n----PROGRAM WITH THE OUTPUT---\n")

output, errors = compileM.communicate(input="q")
print("First Program output--->>",output)
print("First Program errors---->>",errors)

print("\n----PROGRAM WITH THE ERROR---\n")

compileC_C=subprocess.Popen(["gcc", "-o","l","l.c"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
compileC_C=subprocess.Popen(["l","abc","xyz"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output,errors=compileC_C.communicate()


output, errors = compileC_C.communicate()
print("Second Program output--->>",output)
print("Second Program errors---->>",errors)
