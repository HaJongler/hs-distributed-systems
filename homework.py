import argparse
import hashlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="Choose the link you want to shorten")
    args = parser.parse_args()

    sha = hashlib.sha1()
    sha.update(args.link.encode())
    print(f"Your short link is: https://jonathan-link-shortener.com/{sha.hexdigest()}")


if __name__ == '__main__':
    main()
