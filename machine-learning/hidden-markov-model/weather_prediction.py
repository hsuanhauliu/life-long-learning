class Solution(object):
    def __init__(self, filename):
        # known data
        self.number_of_states = 0
        self.pis = []
        self.tran_probabilities = []
        self.obs_probabilities = []
        self.observations= []

        # calculated results
        self.deltas =[]
        self.psi = []

        # read input file
        self.read(filename)

    def read(self, filename):
        with open(filename, 'r') as f:
            # read number of states
            self.number_of_states = int(f.readline())

            # state values; S0(s1), S0(s2), ..., S0(sT)
            self.pis = map(float, f.readline().strip("\n").split())

            for i in xrange(self.number_of_states):
                j = map(float, f.readline().strip("\n").split())
                self.tran_probabilities.append(j)

            # observations P(Umbrella | Weather)
            self.obs_probabilities = map(float, f.readline().strip("\n").split())
            temp = f.readline().strip("\n").split()
            for t in temp:
                if t == "True":
                    self.observations.append(True)
                else:
                    self.observations.append(False)

            f.close()

    def print_path(self, t, w):
        t -= 1
        prev_w = self.psi[t][w]
        if t != 0:
            self.print_path(t, prev_w)
        print "Day", t, ": ", self.weather(prev_w)
        return

    def weather(self, w):
        if w == 0:
            return "Rainy"
        return "Sunny"

    def display_data(self):
        print "Pi's:", self.pis
        print "Transition matrix:", self.tran_probabilities
        print "Observation probabilities:", self.obs_probabilities
        print "Observations:", self.observations

    def display_results(self):
        print "deltas:", self.deltas
        print "psi:", self.psi

    def analyze_result(self, t):
        if self.deltas[t-1][0] >= self.deltas[t-1][1]:
            w = 0
        else:
            w = 1
        print "Day", t, "is more likely to be", self.weather(w)
        return w

    def viterbi_algorithm(self):
        # initialize tables deltas
        psi = []
        deltas = []
        deltas.append(self.pis)

        for t in xrange(len(self.observations)):
            psi.append([0] * self.number_of_states)
            deltas.append([0] * self.number_of_states)
            
            umbrella_brought = self.observations[t]
            for s in xrange(self.number_of_states):
                obs_prob = 0
                if umbrella_brought:
                    obs_prob = self.obs_probabilities[s]
                else:
                    obs_prob = 1 - self.obs_probabilities[s]

                max_prob = 0
                best_path = 0
                for prev_s in xrange(self.number_of_states):
                    temp = deltas[t][prev_s] * self.tran_probabilities[prev_s][s] * obs_prob
                    if temp > max_prob:
                        max_prob = temp
                        best_path = prev_s
                deltas[t+1][s] = max_prob
                psi[t][s] = best_path

        self.deltas = deltas
        self.psi = psi

filename = raw_input("Enter filename: ")
s = Solution(filename)
s.display_data()
s.viterbi_algorithm()
s.display_results()
weather = s.analyze_result(len(s.psi))
s.print_path(len(s.psi), weather)
