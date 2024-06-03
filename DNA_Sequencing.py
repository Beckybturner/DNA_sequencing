
import numpy as np
import math

# this function counts the number of letters in the sequence which are not ACGT
def dna_sequence_check(dna_sequence):
    nucleotides = ["A", "C", "G", "T"]
    non_nucleotides_count = 0
    # loop through each letter in the sequence
    for letter in dna_sequence:
        # if the letter is a nucleotide, continue to the next letter
        if letter in nucleotides:
            continue
        # if the letter is not a nucleotide, increase the 'non_nucleotide_count' and continue to next letter
        else:
            non_nucleotides_count += 1
    return non_nucleotides_count

# this function counts the number of As, Cs, Gs and Ts in the given sequence and works out the %
def count_acgt(dna_sequence, sequence_len):
    acgt_count = [0, 0, 0, 0]
    nucleotides = ["A", "C", "G", "T"]

    # loop through each letter in the sequence and go through the nucleotide list for each letter
    for letter in range(len(dna_sequence)):
        for index in range(4):
            # if the letter is equal to the nucleotide (A, C, G or T), increase the count
            if dna_sequence[letter] == nucleotides[index]:
                acgt_count[index] += 1

    # convert the count of each nucleotide to an array
    acgt_array = np.array(acgt_count)
    # get % by dividing the count of each nucleotide by the total number of letters and multiply by 100
    acgt_percentages = (acgt_array/sequence_len) * 100
    return acgt_count, acgt_percentages

# this function asks the user if they would like to go to the main menu or exit the program
def menu_or_exit():
    menu_or_exit = input("Would you like to go back to the main menu? (Y/N) ").upper()
    while True:
        if menu_or_exit == "Y" or menu_or_exit == "N":
            break
        # if the user doesn't enter 'y' or 'n', ask them to re-enter
        else: 
            menu_or_exit = input("Your answer is invalid. Please re-enter: ")
    return menu_or_exit

# this function splits the sequence by a given letter
def split_seq(dna_sequence, sequence_len):
# create loop which asks user which letter they would like to split their sequence by
    while True:
        letter = input("After which letter would you like to split the sequence? ").upper()
        if letter in ["A", "C", "G", "T"]:
            break
        else:
            continue
# create loop which asks user if they would like to include the letter they split by
    while True:
        incl_letter = input("Would you like to include this letter in each group? (Y/N) ").upper()
        if incl_letter != "N" and incl_letter != "Y":
             print("Error - Y/N not recognised.")
        else:
            break
    # if user does not want to include the letter, split the sequence by that letter
    if incl_letter == "N":
        split_seq = dna_sequence.split(letter)
        print(f"Splitting the sequence by {letter} (and removing) gives: {split_seq}")
    # if the user wants to include the letter, create a list containing the first letter of the sequence
    else:
      dna_sequence_list = [dna_sequence[0]]
      letter_index = 0
      # loop through the letters in the sequence
      for index in range(1, sequence_len):
        # if the letter in the sequence is the given letter to split by, do not include it
        if dna_sequence[index] != letter:
            dna_sequence_list[letter_index] = dna_sequence_list[letter_index] + dna_sequence[index]
        elif dna_sequence[index] == letter:
          letter_index += 1
          dna_sequence_list.insert(letter_index, dna_sequence[index])
      print(f"Splitting the sequence by {letter} (without removing) gives: {dna_sequence_list}")

# this function splits the sequence into groups of a given size
def split_seq_by_size(dna_sequence, sequence_len):
#create loop asking user for size of groups
    while True:
        size_groups = input("What size groups would you like your nucleotides to be split into? ")
        if size_groups.isdigit():
            break
        else:
            print("Error - You must enter a whole number. Please try again.")

    # work out how many groups the letters would be split into
    #add the characters to a new list and keep looping until number of groups met
    size_groups = int(size_groups)
    num_groups = math.ceil(sequence_len / size_groups)
    new_dna_list = []
    while len(new_dna_list) < num_groups:
        new_dna_list.append(dna_sequence[len(new_dna_list)*size_groups : (len(new_dna_list)+1)*size_groups])
    print(f'''
Your sequence split into groups of {size_groups} is:
{new_dna_list}
''')

# this function gives the nucleotide in a given position, also accepting multiple positions
def nucleotide_in_position(dna_sequence, sequence_len):
    while True:
        try:
            position = input("Enter the position number, with 1 being the first position (to enter multiple, separate with comma) : ")
            position = position.replace(" ", "")
            # if the user entered multiple positions, split these into a list
            if "," in position:
                positions = position.split(",")
            else:
                positions = [int(position)]
            # go through each position number, retrieving the nucleotide and adding to a list
            nucleotides = []
            for position in positions:
                nucleotide = dna_sequence[int(position) - 1]
                nucleotides.append(nucleotide)
        # print exception errors
        except ValueError:
            print("Error - You must enter a whole number")
        except Exception as e:
             print(e)
        else:
            break
    print(f'''
The nucleotides in position(s) {positions} are:
{nucleotides}
''')

# function for deleting a specific nucleotide
def acgt_delete(dna_sequence, sequence_len):
    while True:
        try:
            acgt = input("Which letter out of A, C, G, T would you like to delete from the whole sequence?").upper()
            # if the user enters an invalid nucleotide, print error message and loop through again
            if acgt != "A" and acgt != "C" and acgt != "G" and acgt != "T":
                print("Error - You must enter the letter A, C, G or T.")
            else:
                dna_sequence = dna_sequence.replace(acgt, "")
                break
        except Exception as e:
            print(f"Error -  {e}")
        else:
            break
    print(f"The letter {acgt} has been removed from the DNA sequence.")
    return dna_sequence

# create function that takes in the DNA sequence and sequence length
# asks user for the position of the letter they would like to delete (including multiple positions)
def position_delete(dna_sequence, sequence_len):
    dna_sequence_list = []
    # convert the DNA sequence into a list
    for index in range(sequence_len):
        dna_sequence_list += dna_sequence[index]
    # start loop that asks user for the positions to delete and checks whether the values are within range
    while True:
        try:
            position = input("""Enter the position number that you would like to delete, with 1 being the first position
(to enter multiple, separate with comma): """)
            # remove any spaces from input
            position = position.replace(" ", "")
            # if the user has entered just one position, check whether this is within range
            if "," not in position:
              if int(position) <= 0 or int(position) > sequence_len:
                print("Error - The position you entered is outside of the range.")
                continue
            # if the user has entered multiple positions, convert the positions into a string
            elif "," in position:
                positions = position.split(",")
                # if any of the positions are outside of the range, print an error
                for index in range(len(positions)):
                    if int(positions[index]) < 0 or int(positions[index]) > sequence_len:
                        print("Error - you have entered a position that is outside of the range")
        except ValueError:
          print("Error - you must enter a numerical value.")
        else:
            break

    try:
        # if just one position entered, remove this from the DNA sequence list and return the DNA sequence list
        if "," not in position:
           dna_sequence_list.pop(int(position)-1)
         # convert the positions list to an array so that all the remaining positions shift to the left once one of the positions has been dealt with
        else:
          positions = np.array(positions)
          for value in positions:
            # convert positions to integers
            positions[value] = int(value)
             # remove the letter from the DNA sequence at given position
            dna_sequence_list.pop(value-1)
            # delete this position from the positions array
            positions = positions[1:]
            # shift all the positions to the left by one as the DNA sequence will now have one less letter
            positions = positions - 1

        dna_sequence = ''.join(dna_sequence_list)
        return dna_sequence
    except Exception as e:
        print(e)

# ask user to enter the DNA sequence, convert to upper case and get the length
dna_sequence = input("Please enter the DNA sequence: ").upper()
sequence_len = len(dna_sequence)

# check that letters are ACGT by calling the function which counts how many letters are not ACGTs
non_nucleotides_count = dna_sequence_check(dna_sequence)

# if the sequence contains letters which are not ACGT or no letters, ask user to enter again
while non_nucleotides_count > 0 or sequence_len == 0:
    dna_sequence = input("The DNA sequence should contain letters A, C, T and G. Please re-enter: ").upper()
    sequence_len = len(dna_sequence)
    non_nucleotides_count = dna_sequence_check(dna_sequence)

while True:
    # main menu, ask user what they would like to do
    print('''
    Please select from the following options:
    1 - Nucleotide count and percentages
    2 - Split the sequence by a letter
    3 - Split the sequence into groups of a given size
    4 - Give the nucleotide in a given position
    5 - Delete a given nucleotide
    6 - Delete one or more nucleotide in a given position
    7 - Identify if a given pattern exists
    8 - Give the amount of times a given pattern exists
    9 - Replace all occurrences of a given letter
    10 - Replace a letter in a given position
    11 - Randomly create a DNA sequence of a given length
    12 - Exit
    ''')

    try:
        user_select = int(input("Enter your selection: "))
        # if user selects 1, use the acgt_count function to count occurence of each letter and display percentage as well as total number of letters
        if user_select == 1:
            acgt_count, acgt_percentages = count_acgt(dna_sequence, sequence_len)
            print(f'''
        The DNA sequence contains {sequence_len} nucleotides.
        Number of A's: {acgt_count[0]}      Percentage of total sequence: {round(acgt_percentages[0])} %
        Number of C's: {acgt_count[1]}      Percentage of total sequence: {round(acgt_percentages[1])} %
        Number of G's: {acgt_count[2]}      Percentage of total sequence: {round(acgt_percentages[2])} %
        Number of T's: {acgt_count[3]}      Percentage of total sequence: {round(acgt_percentages[3])} %
        ''')
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        elif user_select == 2:
            split_seq(dna_sequence, sequence_len)
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        elif user_select == 3:
            split_seq_by_size(dna_sequence, sequence_len)
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        elif user_select == 4:
            nucleotide_in_position(dna_sequence, sequence_len)
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        elif user_select == 5:
            dna_sequence = acgt_delete(dna_sequence, sequence_len)
            print(f"""The DNA sequence is now:
        {dna_sequence}
        """) 
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        elif user_select == 6:
            dna_sequence = position_delete(dna_sequence, sequence_len)
            print(f"""The DNA sequence is now:
        {dna_sequence}
        """)
            menu_exit = menu_or_exit()
            if menu_exit == "Y":
                continue
            if menu_exit =="N":
                break

        else:
            print("You have entered an invalid number.")
    except:
        print("You have entered an invalid answer.")



    #if "ACGT" in dna_sequence:
        #print("y")
    #else:
        #print("N")

    #for index in range(sequence_len):
        #dna_sequence_list += dna_sequence[index]
        #print(dna_sequence_list)