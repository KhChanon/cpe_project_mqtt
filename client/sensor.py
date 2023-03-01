
import csv
import time

def ReadSensor():
    with open('../data/SampleInput.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header row
        headings = next(reader)
        for row in reader:
            
            yield row
            # read sensor every 3 minutes
            time.sleep(180)


if __name__ == "__main__":
    for data in ReadSensor():
        print(data)
    
    