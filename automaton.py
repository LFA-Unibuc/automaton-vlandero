class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.Sigma = []
        self.States = []
        self.Transitions = []
        self.mat = []
        self.State_dict = {}
        self.Word_dict = {}
        self.Final_states = []
        self.Start_state = ''
        print("Hi, I'm an automaton!")

    def graph_creation(self, input_str):
        def dfs(node):
            nonlocal self
            visited = [False] * len(self.States)
            v = []

            def backt(node):
                nonlocal v
                nonlocal visited
                nonlocal self
                v.append(node)
                visited[node] = True
                for i in range(len(self.States)):
                    if self.mat[node][i] > 0 and not visited[i]:
                        backt(i)
            backt(node)
            return v

        if not self.validate_input(input_str):
            return False
        self.mat = [[0] * len(self.States) for _ in self.States]
        for t in self.Transitions:
            self.mat[self.State_dict[t[0]]
                     ][self.State_dict[t[2]]] = self.Word_dict[t[1]]
        print(self.mat)
        print(dfs(self.State_dict[self.Start_state]))

        return True

    def validate_input(self, input_str):
        input_str = input_str.split('\n')
        lineNum = 0
        while input_str[lineNum][0] == '#':
            lineNum += 1

        if input_str[lineNum] != 'Sigma :':
            return False
        lineNum += 1
        cnt = 1
        while input_str[lineNum] != 'End':
            if(lineNum == len(input_str)):
                return False
            if input_str[lineNum][0] != '#':
                if len(input_str[lineNum].split()) > 1:
                    return False
                self.Sigma.append(input_str[lineNum].strip())
                self.Word_dict[input_str[lineNum].strip()] = cnt
                cnt += 1
            lineNum += 1
        lineNum += 1
        print(f"Sigma: {self.Sigma}")

        while input_str[lineNum][0] == '#':
            lineNum += 1
        if input_str[lineNum] != 'States :':
            return False
        lineNum += 1
        cnt = 0
        while input_str[lineNum] != 'End':
            if(lineNum == len(input_str)):
                return False
            if input_str[lineNum][0] != '#':
                s = [x.strip() for x in input_str[lineNum].split(',')]
                if len(s) > 2:
                    return False
                if len(s) == 2:
                    try:
                        if s[1] not in "FS":
                            return False
                    except:
                        return False
                    if s[1] == 'F':
                        self.Final_states.append(s[0])
                    if s[1] == 'S':
                        if self.Start_state != '':
                            return False
                        self.Start_state = s[0]
                self.States.append(s[0])
                self.State_dict[s[0]] = cnt
                cnt += 1
            lineNum += 1
        lineNum += 1
        print(f"States: {self.States}")

        while input_str[lineNum][0] == '#':
            lineNum += 1

        if input_str[lineNum] != 'Transitions :':
            return False
        lineNum += 1
        while input_str[lineNum] != 'End':
            if(lineNum == len(input_str)):
                return False
            if input_str[lineNum][0] != '#':
                try:
                    stateX, wordY, stateZ = [
                        x.strip() for x in input_str[lineNum].split(',')]
                except:
                    return False
                if stateX not in self.States or wordY not in self.Sigma or stateZ not in self.States:
                    return False
                self.Transitions.append((stateX, wordY, stateZ))
            lineNum += 1
        print(f"Transitions: {self.Transitions}")
        return True

    def read_input(self):
        fin = open(self.config_file)
        return fin.read()

    def print_details(self):
        print("\nStates:")
        for key, value in self.State_dict.items():
            print(f"{key} -> {value}")
        print("\nWords:")
        for key, value in self.Word_dict.items():
            print(f"{key} -> {value}")


if __name__ == "__main__":
    a = Automaton('file.txt')
    print(a.graph_creation(a.read_input()))
    a.print_details()
