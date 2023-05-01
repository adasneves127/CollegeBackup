import sys
import os

def make():
    fileName = sys.argv[-1]
    os.system(f"pdflatex {fileName}")
#    os.system(f"open {fileName[:-3]}pdf")
    os.system(f"rm {fileName[:-3]}log")
    os.system(f"rm {fileName[:-3]}aux")
if __name__ == "__main__":
    make()
