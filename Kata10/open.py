def main():
    try:
        open("/path/to/mars.jpg")
    except OSError as err:
     if err.errno == 2:
         print("Couldn't find the file!", err)
     elif err.errno == 13:
         print("Found the file but couldn't read it", err)
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
if __name__ == '__main__':
    main()
