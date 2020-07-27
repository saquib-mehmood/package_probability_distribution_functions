import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
                
    """
    
     
    
    def __init__(self, prob=.5, size=20):
        
        self.p = prob
        self.n = size
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev()) # provide arguments in lieu of mu and sigma to Superclass constructor
                    
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        
        
                
        self.mean = self.p*self.n
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        
        
        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
        
    def plot_bar(self):
        """Function to output a bar chart of the outcomes using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
            
        plt.bar(x=['o','1'], height = [(1 - self.p) * self.n, self.p * self.n]) 
        plt.title('Bar Chart of Outcomes')
        plt.xlabel('outcome')
        plt.ylabel('count')
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
               
        X = (math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n-k))) * (self.p**k)*((1-self.p)**(self.n-k))
        return X

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
          
        x = []
        y = []
        
        for i in range(self.n+1):
            x.append(i)
            y.append(self.pdf(i))
            
        plt.bar(x=x, height=y)
        plt.title('Probability Distribution of Outcomes')
        plt.xlabel('Outcomes')
        plt.ylabel('Probability')
        
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal' # assuming p values of the two distributions are the same.
        except AssertionError as error:
            raise  # raise an exception if the p values are not equal
        
        
                
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p # assuming p of both binomial distributions to be the same else raise exception above
        result.calculate_mean
        result.calculate_stdev
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
            
        return "mean {}, standard deviation {}, p {}, n{}".format(self.mean, self.stdev, self.p, self.n)
