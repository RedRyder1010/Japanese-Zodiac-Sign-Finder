import textwrap

def get_japanese_zodiac(birth_year):
    """ Determine the Japanese zodiac sign of the user based off the birth year.  Return the Japanese zodiac sign and its description."""
    
    # Dictionary containing each zodiac sign and its description
    zodiac_dict = {
        "Rat (Nezumi)": "People born in the year of the Rat are charming, honest, ambitious, and have a tremendous capacity for pursuing a course to its end. They will work hard for their goals. They are easily angered but maintain an outward show of control.",
        "Ox (Ushi)": "People born in the year of the Ox are patient, mentally alert and when required to speak are skillful. They have a gift for inspiring confidence in others. This allows them to achieve a great deal of success.",
        "Tiger (Tora)": "People born in the year of the Tiger are sensitive, stubborn, short-tempered, courageous, selfish and slightly mean ... yet they are deep thinkers and are capable of great sympathy for those they are close to and love.",
        "Rabbit (Usagi)": "People born in the year of the Rabbit are the most fortunate. They are smooth talkers, talented, ambitious, virtuous and reserved. They have exceedingly fine taste and are regarded with admiration and trust.",
        "Dragon (Tatsu)": "People born in the year of the Dragon are healthy, energetic, excitable, short-tempered and stubborn. However, they are honest, sensitive, brave and can inspire trust in most anyone. They are the most peculiar of the 12 signs of the Zodiac cycle.",
        "Snake (Hebi)": "People born in the year of the Snake are deep thinkers, speak very little and possess tremendous wisdom. They are fortunate in money matters and will always be able to obtain it. They are determined in what they do and hate to fail.",
        "Horse (Uma)": "People born in the year of the Horse are skillful in paying compliments and talk too much. They are skillful with money and handle finances well. They are quick thinkers, wise and talented. Horse people anger easily and are very impatient.",
        "Sheep (Hitsuji)": "People born in the year of the Sheep are elegant, highly accomplished in the arts, passionate about nature. At first glance, they seem to be better off than the people born in other years. They are deeply religious and passionate in whatever they do and believe in.",
        "Monkey (Saru)": "People born in the year of the Monkey are the erratic geniuses of the Zodiac cycle. They are clever and skillful in grand-scale operations and are smart when making financial deals. They are inventive, original and are able to solve the most difficult problems with ease.",
        "Rooster (Tori)": "People born in the year of the Rooster are deep thinkers and are always busy and devoted to their work. They always want to do more than they are able, and if they undertake a task beyond their abilities, they are disappointed. Rooster people have a habit of speaking out directly whenever they have something on their minds.",
        "Dog (Inu)": "People born in the year of the Dog have all the fine qualities of human nature. They have a sense of duty and loyalty, they are extremely honest and always do their best in their relationship with other people. Dog people inspire confidence in others and know how to keep secrets.",
        "Boar (Inoshishi)": "People born in the year of the Boar are brave. They have tremendous inner strength which no one can overcome. They display great honesty. They are short-tempered, yet hate to quarrel or have arguments. They are affectionate and kind to their loved ones."
        }
    
    # Calculate the index of the zodiac sign based on the birth year
    zodiac_index = (birth_year -4) % 12
    
    # Retrieve the zodiac sign and its description
    zodiac_sign = list(zodiac_dict.keys())[zodiac_index]
    description = zodiac_dict[zodiac_sign]
    
    return zodiac_sign, description

def main():
    """ Prompt user to input birth year. Determine their Japanese zodiac sign and display the sign along with its description."""
    
    while True:
        try:
            # Get user input for birth year
            birth_year_str = input("Enter your 4-digit birth year: ")
            # Ensure birth year entered is a 4 digit number
            if not birth_year_str.isdigit() or len(birth_year_str) != 4:
                raise Exception("Please enter a 4-digit number.")
            # Convert entered birth year from string to integer
            birth_year = int(birth_year_str)
            # Check that birth year is within a reasonable range
            if not (1900 <= birth_year <= 2100):
                raise Exception("Please enter a birth year between 1900 and 2100.")
            break
        except Exception as e:
            print(e)
            
    # Get the Japanese zodiac sign and its description
    zodiac_sign, description = get_japanese_zodiac(birth_year)        
    
    # Display the Japanese zodiac sign and its description
    print(f"Your Japanese zodiac sign is {zodiac_sign}.")
    print("Description:")
    # Set width to 80 characters
    wrapper = textwrap.TextWrapper(width=80)
    for line in wrapper.wrap(description):
        print(line)
              
# If the script is run directly, call the main function to execute the program.
if __name__=="__main__":
    main()