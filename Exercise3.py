import sys
import os
dir = "./files1"
files = os.listdir(dir)
files_by_size = sorted(files, reverse = True, key=lambda f: os.path.getsize(os.path.join(dir, f)))
nfiles = files_by_size[:5]
print(files)
print('------------------------------------------------------------------------')
print(nfiles)
print('------------------------------------------------------------------------')
for i in range(5):
    print(str(nfiles[i]) + " " + str(os.stat(nfiles[i]).st_size))
a=0
for i in range(len(files)):
    a = a + os.stat(files[i]).st_size
print("Total size:" + str(a) + " " +"Average file: " + str(a/len(files))+ " " + "Total files: " + str(len(files)))