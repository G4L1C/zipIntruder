# zipIntruder
## Description

Python module to crack zipped files. 

## Implementation example

The zipIntruder Module has the classes bellow:
1. zipVictim - Class used to crack the zip file (see __doc__ for further info).

```python
import zipfile as z
import zipIntruder as i

file = z.ZipFile('data.zip')
wordlist_path = 'List.txt'

s = i.zipVictim(file)
if s.wordlistAttack(wordlist_path):
  print("Cracked! Password %s" % s.password)
else:
  print("Failed! Try another wordlist")
```
## Files
1. data.zip - Protected zipped file example
2. List.txt - Wordlist example
3. zipIntruder.py - Module code
