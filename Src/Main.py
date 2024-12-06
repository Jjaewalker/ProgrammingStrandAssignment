import csv

# Class Definitions
class MP:
    def __init__(self, name, party, constituency, votes_received, gender):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes_received = votes_received
        self.gender = gender

class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.number_of_mps = 0
        self.male_mps = 0
        self.female_mps = 0

    def add_mp(self, mp):
        self.number_of_mps += 1
        self.total_votes += mp.votes_received
        if mp.gender.lower() == 'male':
            self.male_mps += 1
        elif mp.gender.lower() == 'female':
            self.female_mps += 1

    def get_gender_percentage(self):
        total = self.male_mps + self.female_mps
        if total > 0:
            male_percent = (self.male_mps / total) * 100
            female_percent = (self.female_mps / total) * 100
            return {'male': male_percent, 'female': female_percent}
        else:
            return {'male': 0, 'female': 0}

class Constituency:
    def __init__(self, name, registered_voters, total_votes_cast, nation):
        self.name = name
        self.registered_voters = registered_voters
        self.total_votes_cast = total_votes_cast
        self.nation = nation
        self.candidates = []
        self.elected_mp = None

    def add_candidate(self, mp):
        self.candidates.append(mp)
        # Determine if this candidate is the elected MP
        if (not self.elected_mp) or (mp.votes_received > self.elected_mp.votes_received):
            self.elected_mp = mp

    def turnout_percentage(self):
        if self.registered_voters > 0:
            return (self.total_votes_cast / self.registered_voters) * 100
        else:
            return 0

# Dictionaries to store data
parties = {}
constituencies = {}
mps = []

def read_election_data(file_name):
    try:
        # Open the file
        with open(file_name, 'r', encoding='cp1252') as csvfile:
            # Read and skip the first two lines
            next(csvfile)
            next(csvfile)
            # Initialize the DictReader with the remaining lines
            reader = csv.DictReader(csvfile)
            # Normalize fieldnames
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            for row in reader:
                # Strip whitespace from each key and value
                row = {key.strip(): value.strip() for key, value in row.items()}
                # Check if the essential field is empty
                if not row.get('Constituency name'):
                    # If 'Constituency name' is empty, we've reached the end of valid data
                    break
                # Process the valid row
                process_row(row)
                print(row)  # For debugging
                process_row(row)
    except FileNotFoundError:
        print(f"File not found: {file_name}")

def process_row(row):
    # Extract data from the row
    try:
        constituency_name = row['Constituency name']
        nation = row['Country name']
        registered_voters = int(row['Electorate'].replace(',', '').strip('"'))
        total_votes_cast = int(row['Valid votes'].replace(',', '').strip('"'))
        candidate_name = f"{row['Member first name']} {row['Member surname']}"
        party_name = row['First party']
        gender = row['Member gender']

        # Votes received by the winning candidate
        # Retrieve the votes from the column corresponding to the 'First party'
        votes_received_str = row.get(party_name, '0')
        votes_received = int(votes_received_str.replace(',', '').strip('"'))

        # Create or get Constituency object
        if constituency_name not in constituencies:
            constituency = Constituency(constituency_name, registered_voters, total_votes_cast, nation)
            constituencies[constituency_name] = constituency
        else:
            constituency = constituencies[constituency_name]

        # Create or get Party object
        if party_name not in parties:
            party = Party(party_name)
            parties[party_name] = party
        else:
            party = parties[party_name]

        # Create MP object
        mp = MP(candidate_name, party_name, constituency_name, votes_received, gender)
        mps.append(mp)

        # Add MP to constituency and party
        constituency.add_candidate(mp)
        party.add_mp(mp)

    except KeyError as e:
        print(f"KeyError: Missing expected column {e}")
    except ValueError as e:
        print(f"ValueError: {e} in row {row}")

def display_menu():
    print("\nElection Data Inquiry System")
    print("1. Candidate Name")
    print("2. Candidate Party")
    print("3. Parliamentary Seat (Constituency Name)")
    print("4. Total Registered Voters in the Seat")
    print("5. Total Votes Cast in the Seat")
    print("6. Votes Cast for the Candidate")
    print("7. Votes for a Given Party as Percentage of Total Votes Cast")
    print("8. Total Number of Female MPs")
    print("9. Exit and Save Statistics")
    choice = input("Enter your choice (1-9): ")
    return choice

def main_menu():
    while True:
        choice = display_menu()
        if choice == '1':
            # Candidate Name
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"{candidate_name} belongs to the {mp.party} party.")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '2':
            # Candidate Party
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency and constituency.elected_mp:
                print(f"The elected MP for {constituency_name} is {constituency.elected_mp.name}.")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '3':
            # Parliamentary Seat (Constituency Name)
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"{candidate_name} contested in the constituency {mp.constituency}.")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '4':
            # Total Registered Voters in the Seat
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency:
                print(f"Total registered voters in {constituency_name}: {constituency.registered_voters}")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '5':
            # Total Votes Cast in the Seat
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency:
                print(f"Total votes cast in {constituency_name}: {constituency.total_votes_cast}")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '6':
            # Votes Cast for the Candidate
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"Votes received by {candidate_name}: {mp.votes_received}")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '7':
            # Votes for a Given Party as Percentage of Total Votes Cast
            party_name = input("Enter party name: ")
            party = parties.get(party_name)
            if party:
                total_votes_cast = sum(c.total_votes_cast for c in constituencies.values())
                if total_votes_cast > 0:
                    percentage = (party.total_votes / total_votes_cast) * 100
                    print(f"{party_name} received {percentage:.2f}% of total votes cast.")
                else:
                    print("Total votes cast is zero.")
            else:
                print(f"Party {party_name} not found.")
        elif choice == '8':
            # Total Number of Female MPs
            female_mps = [mp for mp in mps if mp.gender.lower() == 'female' and mp == constituencies[mp.constituency].elected_mp]
            print(f"Total number of female MPs: {len(female_mps)}")

        elif choice == '9':
            # Exit and Save Statistics
            save_statistics()
            print("Statistics saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def save_statistics():
    # Implement saving of statistics to a file
    # For example, write to a CSV file
    with open('..FullDataFor20241.CSV', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Constituency', 'Elected MP', 'Party', 'Votes Received', 'Percentage of Total Votes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for constituency in constituencies.values():
            if constituency.elected_mp:
                percentage = (constituency.elected_mp.votes_received / constituency.total_votes_cast) * 100
                writer.writerow({
                    'Constituency': constituency.name,
                    'Elected MP': constituency.elected_mp.name,
                    'Party': constituency.elected_mp.party,
                    'Votes Received': constituency.elected_mp.votes_received,
                    'Percentage of Total Votes': f"{percentage:.2f}%"
                })

if __name__ == "__main__":
    #filename = input("Enter the election data filename (with extension): ")
    filename = "../FullDataFor20241.csv"
    read_election_data(filename)
    main_menu()