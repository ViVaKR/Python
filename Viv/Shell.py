import subprocess

list_files = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)

print(list_files.stdout.decode("utf-8"))


age = 35
pi = 3.124159265359

print(f"Hello, I am {age + 1} years old.")
print("Hello, I am {:16.06f} years old.".format(pi))
print("Hello, I am %d years old." % age)
print("Hello, I am " + str(age) + " years old.")
print("Hello, I am", age, "years old.")
