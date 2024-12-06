#create Mp class

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