import csv


# Dictionaries to store data
parties = {}
constituencies = {}
mps = []


def readfile(filename):
    try:
        #Opens and closes File
        with open("FullDataFor20241.csv", "r", encoding='cp1252') as csvFile:
            reader = csv.DictReader(csvFile)
    #Skip two rows
            next(reader)
            next(reader)
            for row in reader:
                process_row(row)

    except FileNotFoundError:
        print(f"File not found: {filename}")

def process_row(row):
    #Extract data from the row
    try:
        constituency_name = row['Constituency name']
        nation = row['Country name']
        registered_voters = int(row['electorate'].replace(',', '').strip('"'))
        total_votes_cast = int(row['Valid votes'].replace(',', '').strip('"'))
        candidate_name = f"{row['Member First Name']} {row['Member surname']}"
        party_name = row['First party']
        gender = row['Member Gender']

        # Votes received by the winning candidate
        # Retrieve the votes from the column corresponding to the 'First party'
        votes_received_str = row[party_name]
        votes_received = int(str(votes_received_str).replace(',', '').strip('"'))

        #create or get constituency object
        if constituency_name not in constituencies:
            constituency = constituency(constituency_name, registered_voters, total_votes_cast,nation)
            constituencies[constituency_name] = constituency
        else:
            constituency = constituencies[constituency_name]

# Create or get Party object
        if party_name not in parties:
            party = party(party_name)
            parties[party_name] = party
        else:
            party = parties[party_name]

# Create Mp object
        mp = MP(candidate_name, party_name, constituency_name, votes_received,gender)
        #append adds an element to the end of a list
        mps.append(mp)

# Add MP to constituency
        constituency.add_candidate(mp)
        party.add_mp(mp)
    except KeyError as e:
        print(f"KeyError:Missing expected column {e}")
    except ValueError as e:
        print(f"ValueError: {e}in row{row}")