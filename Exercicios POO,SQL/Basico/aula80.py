import os

print(os.getcwd() )
os.chdir('..')
print(os.getcwd())
os.chdir('pypro')
print(os.getcwd())
print(os.name)