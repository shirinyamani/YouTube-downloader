import argparse

def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description= 'Youtube Downloader'
    )

    parser.add_argument('-u', '--url',help='youtube video URL')
    parser.add_argument('-q', '--quality', help='enter your desired quality', default='highest')

    args = parser.parse_args()
    print(args)