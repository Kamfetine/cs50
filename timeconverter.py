def main():
    global input_time
    input_time = input("What time is it? ")

    time = convert(input_time)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    if minutes[-4:] == "a.m." and hours == "12":
        return float("0") + float(minutes[:-4]) / 60
    elif minutes[-4:] == "a.m.":
        return float(hours) + float(minutes[:-4]) / 60
    elif minutes[-4:] == "p.m." and hours == "12":
        return float(hours) + float(minutes[:-4]) / 60
    elif minutes[-4:] == "p.m.":
        return float(str(int(hours) + 12)) + float(minutes[:-4]) / 60
    else:
        return float(hours) + float(minutes) / 60



if __name__ == "__main__":
    main()