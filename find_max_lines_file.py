#!/usr/local/bin/python3
import glob
import subprocess

if __name__ == '__main__':
    counter = []
    for filename in glob.glob('**/*.py', recursive=True):
        child_process = subprocess.Popen(['wc', '-l', filename], stdout=subprocess.PIPE)
        stdout, _stderr = child_process.communicate()
        lines_count = int(stdout.decode('utf-8').strip().split()[0])
        counter.append((lines_count, filename))
    counter.sort(reverse=True)
    for lines_count, filename in counter:
        print(lines_count, filename)
