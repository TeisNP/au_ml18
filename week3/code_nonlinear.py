import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import urllib
import time

def load_data():
    """ Simple helper function for downloading and loading data """
    filename = 'nonlinear_data.npz'
    if not os.path.exists(filename):
        print('file not exists - downloading')
        with open(filename, 'wb') as fh:
            path = "http://users-cs.au.dk/jallan/ml/data/{0}".format(filename)
            fh.write(urllib.request.urlopen(path).read())
    D =  np.load(filename)
    return D


class PerceptronClassifier():

    def __init__(self):
        self.w = None
        
    def fit(self, X, y, maxiter=1<<16, w=None):
        """
        Implement Pocket Perceptron learning algorithm - run for at most maxiter iterations and store best w found as well as the training history 
        
        Args:
        X: numpy array shape (n,d) - training data 
        y: numpy array shape (n,) - training labels
        maxiter: int, maximum number of iterations to run
        w: numpy array shape (d,) - inital w if desired
        Saves:
        w: numpy array shape (d,) normal vector of the best hyperplane found for separating X, y 
        may not seperate the data fully
ies)
        
    
        """
        if w is None:
            w = np.zeros(X.shape[1])       
        bestw = w
        ### YOUR CODE
        ### END CODE
        self.w = bestw

    def predict(self, X):
        """ predict function for classifier
        Args:
          X (numpy array,  shape (n,d))
        Returns
          pred (numpy array,  shape(n,))
        """
        pred = None
        ### YOUR CODE HERE 1-2 lines
        ### END CODE
        return pred

    def score(self, X, y):
        """ Return accuracy of model on data X with labels y
        
        Args:
          X (numpy array shape n, d)
        returns
          score (float) classifier accuracy on data X with labels y
        """
        score = 0 
        ### YOUR CODE HERE 1-3 lines
        ### END CODE
        return score
    
        


def test_pla_train(n_samples=10):
    """ Test function for pla train """
    from sklearn.datasets import make_blobs
    print('Test perceptron classifier on random blobs - should be very linearly separable')
    centers = [(-50, -50), (50, 50)]
    X, y = make_blobs(n_samples=n_samples, n_features=2, cluster_std=1.0,
                  centers=centers, shuffle=False, random_state=42)
    y = y * 2 - 1
    classifier = PerceptronClassifier()
    classifier.fit(X, y)
    assert np.all(classifier.predict(X) == y), 'all predictions should be correct'
    print('test completed')
    

def plot_hyperplane(w, ax, *args, **kwargs):
    """ COPY FROM EARLIER EXERCISE 
    Plot the hyperplane (line) w0 + w1*x1 + w2*x2 = 0 in the range R = [xmin,xmax] times [ymin,ymax] for a generic w = (w0, w1, w2).
    
    We will proceed in a similar fashion as we did in the previous task.
    There we had xmin = ymin = 0 and xmax = ymax = 1 (i.e. the range was [0,1]x[0,1]), and we just found the intersection points of the hyperplane with the two vertical lines x1=0 and x1=1. 
    How can we find these two points for a generic w = (w0,w1,w2) and a generic range ([xmin,xmax] x [ymin,ymax])?
 
    Remember to handle possible special cases! 
    
    Notice how we pass along optional arguments to the plot function, which allows us to change color, etc. of the hyperplanes.

    Args:
    w: numpy array shape (d,)
    ax: matplotlib axes object to plot on
    args: extra arguments to plot (ignore)    
    kwargs: extra keyword arguments to plot (ignore)    
    
    """
    
    if w[1]==0 and w[2]==0: raise ValueError('Invalid hyperplane')
    # Notice that w1 and w2 are not allowed to be 0 simultaneously, but it may be the case that one of them equals 0
    
    xmin, xmax, ymin, ymax = plt.axis()
    
    # Write the code here to create two NumPy arrays called x and y.
    # The arrays x and y will contain the x1's and x2's coordinates of the two endpoints of the line, respectively.
    
    x = np.array((0, 1))
    y = np.array((0, 1))
    
    ### YOUR CODE HERE 
    ### END CODE
    
    # plot the hyperplane
    ax.plot(x, y, *args, **kwargs)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    

def square_transform(X):
    """
    Implement the square transform including the bias variable 1 in the first column i.e 
    phi(x_1,x_2) = (1, x_1^2, x_2^2). 
    We will prepend a column of ones for the bias variable
    
    np.c_, np.transpose may be useful
    To raise a number to second power use operator ** i.e. 3**2 is 9
    
    As an example of what the function should do:
    >>> X = np.array([[1,2],[3,4]])
    >>> square_transform(X)
    array([[  1.,   1.,   4.],
       [  1.,   9.,  16.]])

    Args:
      X: np.array of shape (n, 2)

    Returns
      Xt: np.array of shape(n, 3) 
    """
    # Insert code here to transform the data - aim to make a vectorized solution!
    Xt = X

    ### YOUR CODE HERE 2-4 lines
    ### END CODE 
    
    return Xt
    
def plot_contour(w, phi, ax):
    """
    At first make a solution with for loops. 
       
    Then if you have time, aim to make a vectorized solution! There are different approaches to obtain this. 
    If you have built coordinate grids as above using meshgrid, then xm and ym are 100x100 arrays. 
    
    You can  build a dx100x100 array where the first index is indexing the d coordinates of phi(x,y)
    (together with the dummy 1) and the other two indices are x and y. 
    Here the NumPy command array is useful. 
    
    You can now either:    
    
    Reshape the array to a dx10000 array, make a vector matrix product with w_{pla} 
    obtaining a 1x10000 array and reshaping back to a 100x100 array
    (for this the NumPy command reshape is useful)
       
    If this does not work or you are pressed for time you can try the naive version.

    Args: 
     w: np.array shape (d,) the decision boundary vector
     phi: function, the transform phi to contour plot (function from (n, 2) array to (n, d) array
     ax: matplotlib Axes, to plot the contour on     
    """

    nsize = 100
    xs = ys = np.linspace(-1, 1, nsize)
    xm, ym = np.meshgrid(xs, ys)
    img = np.zeros((nsize, nsize)) # makes a 100 x 100 2d array
    ### YOUR CODE
    ### END CODE
    cont = ax.contour(xs, ys, img, [0], colors='r', linewidths=3)
    return cont

    
def poly_transform(X):
    """
    Compute the polynomial transform [x_1^i * x_i^j] for 0 <= i+j <=3
    List comprehensions may be very useful
    Also, np.c_ or np.transpose could be useful
    
    Args:
     X: numpy array shape (n, 2)

    Returns: 
      numpy arrays shape (n, d) 
    """
    Xt = X
    ### YOUR CODE HERE
    ### END CODE
    return Xt



def plot_data():
    """
    Insert code to plot the data sets here
    
    plot_data using scatter plots in xrange and yrange set to [-1, 1] and set title to Data Set i for the i'th data set.
    We have created the 4 axes for you to plot on. ie axes[0] should contain data set 1 and so on.
    Plot the data on these 4.

     ax.scatter, ax.set_title may come in usefull
    """
    D = load_data()

    fig, axes = plt.subplots(1, 4, figsize=(20, 20))
    
    ### YOUR CODE 
    ### END CODE
    plt.show()

    
def plot_square_transform():
    """ Visualize the square transform """
    D = load_data()
    X = D['X1']
    y = D['y1']
    Xt = square_transform(X)
    cls = PerceptronClassifier()
    cls.fit(Xt, y)
    w_pla = cls.w 
    print('Hyperplane:', w_pla)
    fig, axes = plt.subplots(1, 2, figsize=(16, 13))
    axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, s=20)
    axes[0].set_title('Data Set 1')
    axes[1].scatter(Xt[:,1], Xt[:, 2], c=y, cmap=plt.cm.Paired, s=20)
    plot_hyperplane(w_pla, axes[1], 'r--', linewidth=4)    
    axes[1].set_title('Data Set 1 - transformed - and decision boundary learned')    
    plt.show()

    
def contour_test():
    """ Test contour algorithm """
    D = load_data()
    fig, axes = plt.subplots(1, 2, figsize=(20, 16))
    print('Contour for data set {0}'.format(1))
    X = D['X1']
    y = D['y1']
    Xt = square_transform(X)
    cls = PerceptronClassifier()
    cls.fit(Xt, y)
    w_pla = cls.w    
    ax = axes[0]        
    ax.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired, s=20)
    plot_contour(w_pla, square_transform, ax)
    ax.set_xlim([-1, 1])
    ax.set_title('Data set {0}: Score: {1}'.format(0, cls.score(Xt, y)))

    fe = axes[1]
    fe.scatter(Xt[:, 1], Xt[:, 2], c=y, cmap=plt.cm.Paired, s=20)
    fe.set_xlim([0, 1])
    fe.set_title('Data set {0}: Feature Space')
    plot_hyperplane(w_pla, fe, 'r--', linewidth=4)

    plt.show()
    

def run():
    """
    For each data set
        # (1) apply the degree 3 polynomial transform.
        # (2) runs the perceptron learning algorithm.
        # (3) computes and prints the in sample error and plots the results including contour plots
    
    """
    D = load_data()
    fig, axes = plt.subplots(1, 4, figsize=(20, 16))
    for i in range(1, 5):
        X = D['X%d' % i]
        y = D['y%d' % i]
        Xt = poly_transform(X)
        cls = PerceptronClassifier()
        cls.fit(Xt, y)
        w_pla = cls.w
        ax = axes[i-1]
        ax.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired, s=20)
        plot_contour(w_pla, poly_transform, ax)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_title("Nonlinear Perceptron - D{0}: Score: {1}".format(i, cls.score(Xt, y)))

        
    plt.show()

def run_linreg():
    """
    For each data set
        # (1) apply the degree 3 polynomial transform.
        # (2) runs the perceptron learning algorithm.
        # (3) computes and prints the in sample error and plots the results including contour plots
    
    """
    D = load_data()
    fig, axes = plt.subplots(1, 4, figsize=(20, 16))
    for i in range(1, 5):
        X = D['X%d' % i]
        y = D['y%d' % i]
        Xt = poly_transform(X)
        cls = LinRegClassifier()
        cls.fit(Xt, y)
        w_pla = cls.w
        ax = axes[i-1]
        ax.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired, s=20)
        plot_contour(w_pla, poly_transform, ax)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_title("Nonlinear LinReg - D{0}: Score: {1}".format(i, cls.score(Xt, y)))
        
    plt.show()


class LinRegClassifier():

    def __init__(self):
        self.w = None
    
    def fit(self, X, y):
        """ 
        Linear Regression Learning Algorithm
        
        For this we compute the parameter vector         
        wlin = argmin ( sum_i (w^T x_i -y_i)^2 )    
        The pseudo-inverse operator pinv in numpy.linalg package may be useful, i.e. np.linalg.pinv

        Args:
        X: numpy array shape (n,d)
        y: numpy array shape (n,)
            
        Computes and stores w: numpy array shape (d,) the best weight vector w to linearly approximate the target from the features.

        """  
        w = np.zeros(X.shape[1])
        #YOUR CODE HERE 1-3 lines
        #END CODE
        self.w =  w

    def predict(self, X):
        """ predict function for classifier
        Args:
          X (numpy array,  shape (n,d))
        Returns
          pred (numpy array,  shape(n,))
        """
        pred = None
        ### YOUR CODE HERE 1-2 lines
        ### END CODE
        return pred

    def score(self, X, y):
        """ Return accuracy of model on data X with labels y
        
        Args:
          X (numpy array shape n, d)
        returns
          score (float) classifier accuracy on data X with labels y
        """
        score = 0 
        ### YOUR CODE HERE 1-3 lines
        ### END CODE
        return score

        
        

        
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-platest', action='store_true', default=False)
    parser.add_argument('-plot', action='store_true', default=False)
    parser.add_argument('-square', action='store_true', default=False)
    parser.add_argument('-contour', action='store_true', default=False)
    parser.add_argument('-run', action='store_true', default=False)
    parser.add_argument('-animation', action='store_true', default=False)
    parser.add_argument('-linreg', action='store_true', default=False)
    
    
    args = parser.parse_args()
    if args.platest:
        test_pla_train()
    if args.plot:
        plot_data()
    if args.square:
        plot_square_transform()
    if args.contour:
        contour_test()
    if args.run:
        run()
    if args.linreg:
        run_linreg()
