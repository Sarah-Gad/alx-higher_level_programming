#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thelen = len(sys.argv) - 1
    if thelen == 0:
        print(f"0")
    else:
        total = int(sys.argv[1])
        for idx in range(2, thelen + 1):
            total = total + int(sys.argv[idx])
        print(f"{total}")
