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

Final Code Validation
After addressing these issues, I performed additional tests to validate the final code. For instance, I tested a full scenario involving multiple constituencies, candidates, and parties, ensuring that the calculations for turnout, gender representation, and votes were accurate.


 ```
