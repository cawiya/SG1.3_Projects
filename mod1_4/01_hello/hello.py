#!/usr/bin/env python3
# Purpose: Say hello
    
"""
Author: Ken You <wiyac@yahoo.com>
Purpose: Say Hello
"""

import argparse

#parser = argparse.ArgumentParser(description="Say hello")
#parser.add_argument("name", help="name to greet")
#args = parser.parse_args()
#print("Hello, " + args.name + "!")

def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n", "--name", metavar="name", default="World", help="name to greet")
    return parser.parse_args()

def main():
    """Make a jazz noise here"""

    args = get_args()
    print("Hello, " + args.name + "!")

if __name__ == "__main__":
    main()