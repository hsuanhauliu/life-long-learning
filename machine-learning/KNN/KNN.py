import matplotlib.pyplot as plt

class KNN(object):
    """
        A K-Nearest Neighbor classifier class.
    """
    def __init__(self, filename=""):
        self.data_x = []
        self.data_y = []
        self.data_labels = []
        self.categories = ['g', 'b']

        if filename != "":
            self.train(filename)

        return

    def train(self, filename):
        """
            Read input file.
        """
        with open(filename, 'r') as f:
            for line in f:
                point = line.split()
                self.data_x.append(int(point[0]))
                self.data_y.append(int(point[1]))
                self.data_labels.append(point[2])
            f.close()
        return

    def display_data(self):
        """
            Display a list of training data used and plot them on a scatter graph.
        """
        for i in xrange(len(self.data_x)):
            print self.data_x[i],
            print self.data_y[i],
            print self.data_labels[i]

        # Graph a scatter plot of the training data
        plt.scatter(self.data_x, self.data_y, c = self.data_labels)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Data Plot')
        plt.show()

        return

    def k_nearest_neighbor(self, (x, y), k=1):
        """
            KNN implementation.
        """
        if k > len(self.data_x):
            print "Error: cannot input a k larger than the number of data."
            return

        nearestNeighbors = [] # [(dist, label), (dist, label), (dist, label) ... ]
        neighborLabels = [0, 0] # [number of green, number of blue]

        # calculate distances to each neighbor
        for i in xrange(len(self.data_x)):
            dist_x = abs(x - self.data_x[i])
            dist_y = abs(y - self.data_y[i])
            nearestNeighbors.append( (dist_x + dist_y, self.data_labels[i]) )

        # sort by distance in ascending order
        nearestNeighbors = sorted(nearestNeighbors)[:k]
        for neighbor in nearestNeighbors:
            if neighbor[1] == 'g':
                neighborLabels[0] += 1
            else:
                neighborLabels[1] += 1

        # if there is a tie, consider one more neighbor (k += 1)
        if neighborLabels[0] == neighborLabels[1]:
            if k == len(self.data_x):
                if neighbor[k] == 'g':
                    neighborLabels[0] += 1
                else:
                    neighborLabels[1] += 1
            else:
                return 'g'
        
        if neighborLabels[0] > neighborLabels[1]:
            return 'g'
        return 'b'

def main():
    filename = "sample-inputs/test1.txt"
    k = KNN()
    k.train(filename)

    query_x = input("Enter x: ")
    query_y = input("Enter y: ")
    query_label = k.k_nearest_neighbor( (query_x, query_y) )
    label = ""
    if query_label == 'g':
        label = "green"
    else:
        label = "blue"

    print "This query point is classfied as", label, "\n"
    k.display_data()

    return

if __name__ == "__main__":
    import sys
    main()
