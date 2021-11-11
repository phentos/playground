import sys

def main():
  args = [_ for _ in sys.argv[1:]]
  for _ in args:
    print(_)

if __name__ == "__main__":
	main()