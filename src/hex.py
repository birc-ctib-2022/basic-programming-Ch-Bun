import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        y = []
        for i in x:
            y.append(hex(ord(i)))
        encoding = ''.join(y)

        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        hexList = []
        hexList = x.split('0x')
        hexList.pop(0)
        for j in hexList:
            decoding = decoding + chr(int(j, base = 16))
        print(decoding)
