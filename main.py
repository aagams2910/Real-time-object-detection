

from people_detector import PeopleDetector


def main():
    
    versions = ["v5", "v8"]

    detector = PeopleDetector(versions[1])
    detector.process_video()


if __name__ == "__main__":
    main()
