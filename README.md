Week 1: FileIo
Tasks:
Set up the project structure.
Plan initial classes: MP, Party, and Constituency.
researched functions and reference self and init constructor (still a bit confusing but i learned how to use it)

Created project folder with necessary files (e.g., main.py, classes.py).
exported the 'FuLLDATAFOR20241' Csv into appropriate folder at first i was looking to use matplot lib and pandas
but was informed i didnt need to use it, my first file was fileio.

FileIo 

i have dictionaries (parties, constituencies and mps that are saved within {} brackets.

I started by defining my readfiles that open and closes the files and skipping rows and processing and handling the data for each row
I defined process_row and extracted data form the rows in the file and used key phrases such as nation, registred voters, candidate name etc which wi;; be the staple throught my project.

I added if statementsa and else statements so for example if the party name 
party = Party(party_name)
            parties[party_name] = party
        else:
            party = parties[party_name]
  This would check if the party name is within the parties dictionary and the dictionary acts as a central collection where Party objects are stored, with the party_name as the key.
and if the party doesnt exist A new Party object is created using the line party = Party(party_name). This initializes a new instance of the Party class with the given party_name. f the Party Already Exists:
The else block is executed, which retrieves the existing Party object from the parties dictionary: party = parties[party_name].
  
And this is done to make sure there are no duplicate party objects and keeps everything organised

finally, i added  except KeyError as e:
        print(f"KeyError: Missing expected column {e}")
    except ValueError as e:
        print(f"ValueError: {e} in row {row}")
 to catch any errors thats may occur when converting data or accessing data that doesnt exist and whenever there is an error 
 Both: 
 print(f"ValueError: {e} in row {row}") and (f"KeyError: Missing expected column {e}"
 Will be printed

 I also had my classes folder set up with just def MP, Constituency, Party set up but with no code in them as id work on that a nother day

 Week 2 Classes

This week, my primary task was to create and test a Python implementation for handling a simplified electoral system. This involved developing three classes: MP, Party, and Constituency. After writing the code, I identified and fixed several issues to ensure accurate functionality. Here’s an overview of the development process, including examples of errors encountered and how I corrected them.

Development Overview
The MP class represents Members of Parliament and stores information such as name, party, constituency, votes received, and gender. The Party class tracks party-level data like total votes, number of MPs, and gender statistics. The Constituency class represents a geographical area with registered voters and candidates, calculating voter turnout and determining the elected MP.

Error Testing and Resolution
Error 1: Handling Case Sensitivity in Gender
Initially, the add_mp method in the Party class handled gender counting incorrectly. For example, when I tested the code with mixed-case inputs such as "Male" or "FEMALE", these were not recognized properly, leading to incorrect gender counts.

Failing Test:

```
mp1 = MP("Alice", "Green Party", "Greenfield", 5000, "Female")
mp2 = MP("Bob", "Green Party", "Greenfield", 4000, "MALE")
party = Party("Green Party")
party.add_mp(mp1)
party.add_mp(mp2)
print(party.male_mps, party.female_mps)  # Expected output: 1, 1; Actual output: 0, 1

```
Fix: I added .lower() to standardize gender inputs:
```
if mp.gender.lower() == 'male':
    self.male_mps += 1
elif mp.gender.lower() == 'female':
    self.female_mps += 1
```
Now the code handles mixed-case inputs correctly.

Error 2: Incorrect Turnout Percentage Calculation
In the Constituency class, the turnout_percentage method did not account for edge cases where registered_voters was zero. This caused a division by zero error during testing.

Failing Test:


constituency = Constituency("Bluefield", 0, 3000, "Nation A")
print(constituency.turnout_percentage())  # Expected output: 0; Actual output: ZeroDivisionError
Fix: I added a condition to return 0 if registered_voters is zero:

```
if self.registered_voters > 0:
    return (self.total_votes_cast / self.registered_voters) * 100
else:
    return 0
This ensured robust handling of edge cases.

Error 3: Incorrect Candidate Addition Logic
While testing candidate addition in the Constituency class, I realized the logic for determining the elected MP was flawed. If two candidates had the same number of votes, the code always chose the second one due to overwriting the previous result.
```


if (not self.elected_mp) or (mp.votes_received > self.elected_mp.votes_received):
    self.elected_mp = mp
This resolved the tie-handling issue.



Defined foundational classes: MP, Party, and Constituency.
Developed read_election_data to read a CSV file containing election data.
Implemented error handling for FileNotFoundError to ensure robust file input handling.
Key Errors Encountered:

FileNotFoundError:
Occurred when the program couldn't locate the file.
Solution: Added a try-except block to catch the error and provide an informative message:
python
Copy code
except FileNotFoundError:
    print(f"File not found: {file_name}")

Work Done:

Parsed and cleaned constituency-specific data like Constituency name, Country name, Electorate, and Valid votes.
Implemented the Constituency class to store and manage constituency details.
Linked constituencies to the election data pipeline in process_row.
Key Errors Encountered:

KeyError:
Triggered when some CSV columns were missing or misnamed.
Solution: Added checks and error handling for missing columns:
python
Copy code
except KeyError as e:
    print(f"KeyError: Missing expected column {e}")
Work Done:

Implemented the MP class to represent candidates and their election results.
Linked MPs to their respective constituencies.
Added the Party class to track votes and MPs by party.
Key Errors Encountered:

ValueError When Parsing Numbers:
Some numeric fields in the CSV contained unexpected characters.
Solution: Used replace and strip to clean data:
python
Copy code
registered_voters = int(row['Electorate'].replace(',', '').strip('"'))

Work Done:

Created the add_candidate method in the Constituency class to determine the elected MP for each seat.
Implemented the add_mp method in the Party class to track MPs and votes by gender.
Established links between MP, Party, and Constituency.
Key Errors Encountered:

Empty Data Rows:
Encountered blank rows at the end of the file.
Solution: Added a check to skip invalid rows:
python
Copy code
if not row.get('Constituency name'):
    break

Work Done:

Developed a text-based menu for querying election data.
Added options to search for data by candidate, party, constituency, and overall statistics.
Implemented functionality to calculate turnout percentages and gender breakdowns.
Key Errors Encountered:

Invalid User Input:
Some invalid options caused crashes.
Solution: Added input validation and default cases:
python
Copy code
else:
    print("Invalid choice. Please try again.")
Day 6: Output and Reporting
Work Done:

Implemented a function to save processed election data to a CSV file (save_statistics).
Included detailed statistics such as total votes, elected MPs, and gender breakdowns.
Key Errors Encountered:

File Encoding Issues:
Errors occurred when saving special characters in constituency names.
Solution: Set the file encoding to utf-8 during output:
python
Copy code
with open('output.csv', 'w', encoding='utf-8') as csvfile:

Work Done:

Conducted end-to-end testing with sample election data.
Fixed edge cases such as constituencies with no valid votes or multiple candidates with identical vote counts.
Improved performance by optimizing data parsing.
Key Errors Encountered:

Duplicate MP Entries:

Some MPs were added multiple times due to duplicate rows.
Solution: Added checks to avoid re-adding MPs:
python
Copy code
if candidate_name not in [mp.name for mp in mps]:
    mps.append(mp)
Division by Zero:

Occurred when calculating percentages for constituencies with zero registered voters.
Solution: Added a safeguard:
python
Copy code
if self.registered_voters > 0:
    return (self.total_votes_cast / self.registered_voters) * 100
 ```
Testing Process
Initial Testing of display_menu
The display_menu function was tested first to ensure the user interface was clear and the input was captured correctly. The function printed a list of options and returned the user's selection.

Initial Observation:

Menu displayed correctly.
The input returned the choice as expected.
Error 1: Invalid User Input Handling
Scenario: When users entered inputs outside the expected range (e.g., letters instead of numbers), the program did not respond gracefully.

Cause: The display_menu function directly returned user input without validating it.

Error Example: When input was "abc" instead of a number between 1 and 9, the program printed "Invalid choice" repeatedly.

Solution: A validation check was added in the main_menu function:

python
Copy code
else:
    print("Invalid choice. Please try again.")
Testing Menu Options
I systematically tested each menu option to ensure accurate data retrieval and appropriate error handling.

Error 2: Candidate Not Found (Option 1)
Scenario: When entering a candidate's name not present in the dataset, the program failed to handle it gracefully.

Cause: The next function in the code did not handle cases where no matching candidate was found.

Error Example: Input: "John Doe" (not in dataset).
Output: Program raised a StopIteration error.

Solution: A default None value was provided to the next function:

python
Copy code
mp = next((mp for mp in mps if mp.name == candidate_name), None)
if mp:
    print(f"{candidate_name} belongs to the {mp.party} party.")
else:
    print(f"Candidate {candidate_name} not found.")
Error 3: Constituency Not Found (Option 2)
Scenario: Entering a constituency name not present in the dataset caused the program to return incorrect results.

Cause: The get method for the constituencies dictionary did not include error handling for missing keys.

Error Example: Input: "Nonexistent Constituency".
Output: No output or an error.

Solution: An explicit check was added to handle missing constituency data:

python
Copy code
if constituency and constituency.elected_mp:
    print(f"The elected MP for {constituency_name} is {constituency.elected_mp.name}.")
else:
    print(f"No data for constituency {constituency_name}.")
Error 4: Division by Zero in Percentage Calculation (Option 7)
Scenario: Calculating the percentage of votes for a party when the total votes cast was zero caused a ZeroDivisionError.

Cause: The calculation did not account for constituencies where no votes were cast.

Error Example: Input: Party name "Nonexistent Party" in a constituency with zero votes.
Output: ZeroDivisionError.

Solution: Added a condition to check for zero votes:

python
Copy code
if total_votes_cast > 0:
    percentage = (party.total_votes / total_votes_cast) * 100
    print(f"{party_name} received {percentage:.2f}% of total votes cast.")
else:
    print("Total votes cast is zero.")
Error 5: Incorrect Gender Filtering (Option 8)
Scenario: The total number of female MPs was not calculated correctly, as it included all female MPs, not just the elected ones.

Cause: The filter for elected MPs did not ensure that the MP was the winner in their constituency.

Error Example: Input: Option 8
Output: Count included all female MPs, not just elected ones.

Solution: Filtered MPs to include only those who were the elected representatives:

python
Copy code
female_mps = [mp for mp in mps if mp.gender.lower() == 'female' and mp == constituencies[mp.constituency].elected_mp]
print(f"Total number of female MPs: {len(female_mps)}")
Error 6: File Save Error (Option 9)
Scenario: When saving statistics, the program failed if special characters (e.g., accents) were present in constituency names.

Cause: The file encoding was not compatible with the dataset.

Error Example: Input: Option 9
Output: Encoding error during file write operation.

Solution: Changed the file encoding to UTF-8:

python
Copy code
with open('..FullDataFor20241.CSV', 'w', newline='', encoding='utf-8') as csvfile:
