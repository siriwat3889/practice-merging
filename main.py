def main():
    print("Main function")
    print(hello_thai())
    print(calculate_bmi(70, 180))


def interpret_bmi(bmi):
    """
    AV-JAPAN 777
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_bmi(weight: float, height_cm: float) -> dict:
    # convert height from cm to m
    height_m = height_cm / 100
    bmi = weight / (height_m**2)
    return {
        "bmi": bmi,
        "interpretation": interpret_bmi(bmi),
        "weight": weight,
        "height": height_cm,
    }


def hello_thai():
    # return "สวัสดีชาวโลก"
    return "Hello, World!".center(50, "*")

if __name__ == "__main__":
    main()
