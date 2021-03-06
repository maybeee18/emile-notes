#####STATISTICAL THINKING IN PYTHON#####

'''Graphical Exploratory Data Analysis'''

    # Plotting a histogram

        import matplotlib.pyplot as plt
        _ = plt.hist(df_swing['dem_share'])
        _ = plt.xlabel('percent of vote for Obama')
        _ = plt.ylabel('number of counties')
        plt.show()

        # plt.hist() returns 3 arrays we are not interested in
        # using dummy variables _ lets us just focus on the plot

        # Setting bins

            # Specifying bin edges
            bin_edges = [0, 10, 20, 30, 40, 50,
                        60, 70, 80, 90, 100]
            _ = plt.hist(df_swing['dem_share'], bins=bin_edges)
            plt.show()

            # Setting number of bins
            _ = plt.hist(df_swing['dem_share'], bins=20)
            plt.show()

            # Binning bias - the same data may be interpreted differently depending on choice of bins

        # Setting Seaborn styling

        import seaborn as sns
        sns.set()
        _ = plt.hist(df_swing['dem_share'])
        _ = plt.xlabel('percentage of vote for Obama')
        _ = plt.ylabel('number of counties')
        plt.show()

    # Bee swarm plots

        _ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
        _ = plt.xlabel('state')
        _ = plt.ylabel('percent of vote for Obama')
        plt.show()

    # Empirical cumulative distribution functions (ECDF)

        # Example
            import numpy as np

            x = np.sort(df_swing['dem_share'])

            y = np.arange(1, len(x)+1) / len(x)

            _ = plt.plot(x, y, marker='.', linestyle='none')
            _ = plt.xlabel('percent of vote for Obama')
            _ = plt.ylabel('ECDF')
            plt.margins(0.02)
            plt.show()

        # Function to calculate ECDF
            def ecdf(data):
                """Compute ECDF for a one-dimensional array of measurements."""
                # Number of data points: n
                n = len(data)

                # x-data for the ECDF: x
                x = np.sort(data)

                # y-data for the ECDF: y
                y = np.arange(1, n+1) / n

                return x, y

'''Quantitative Exploratory Data Analysis'''

    # Mean
        np.mean(dem_share_PA)

        # Heavily influenced by outliers

    # Median
        np.median(dem_share_PA)

        # Not influenced by outliers

    # Percentiles
        np.percentile([df_swing['dem_share'], [25, 50, 75])
        # Returns 25th, 50th, 75th percentiles

    # Box plot
        import matplotlib.pyplot as plt
        import seaborn as sns

        _ = sns.boxplot(x='east_west', y='dem_share',
                        data=df_all_states)
        _ = plt.xlabel('region')
        _ = plt.ylabel('percent of vote for Obama')
        plt.show()

    # Variance 
        # Mean squared distance of data from mean
        # Measure of spread

        np.var(dem_share_FL)

    # Standard Deviation
        # Square root of variance
        # Same units as quantity

        np.std(dem_share_FL)

    # Covariance and Pearson correlation coefficient

        # Scatter plot

            _ = plt.plot(total_votes/1000, dem_share,
                         marker='.', linestyle='none')
            _ = plt.xlabel('total votes (thousands)')
            _ = plt.ylabel('percent of vote for Obama')

        # Covariance

            # 1/n sum[ (x-x_mean)*(y-y_mean)]

            np.cov(x, y)
            # Returns covariance matrix
            # [0,0] --> variance in x
            # [1,1] --> variance in y
            # [0,1] and [1,0] --> covariance

        # Pearson correlation coefficient

            # p = covariance / (x_std * y_std)
            #   = variability due to codependence / independent variability
            # Dimensionless [-1, 1]

            np.corrcoef(x, y)
            # Returns 2x2 matrix
            # [0,0] and [1,1] neccesarily 1 (self-correlation)
            # [0,1] and [1,0] --> correlation coefficient
    
'''Thinking probabilistically - Discrete variables'''

    # Random number generators and hacker statistics

        # Hacker statistics - Uses simulated repeat measurements to compute probabilities
            
            # Determine how to simulate data
            # Simulate many times
            # Compute fraction of trials with outcome of interest


        # np.random module - suite of functions based on random number generation

        # Simulating a coin flip
        np.random.random() # draws random number [0,1], equal prob
        # Heads < 0.5
        # Tails >= 0.5
        
        # Bernouli trial - 
            # experiment with two options, success (True) and failure (False)

            def perform_bernoulli_trials(n, p):

                """Perform n Bernoulli trials with success probability p
                and return number of successes."""

                # Initialize number of successes: n_success
                n_success = 0

                # Perform trials
                for i in range(n):
                    # Choose random number between zero and one: random_number
                    random_number = np.random.random()

                    # If less than p, it's a success so add one to n_success
                    if random_number < p:
                        n_success += 1

                return n_success

        # Random number seed - integer fed into random number generating algorithm
        # Manually seed random number generator for reproducability
        np.random.seed()

        # Simulating 4 coin flips
            import numpy as np
            np.random.seed(42)
            random_numbers = np.random.random(size=4)

            heads = random_numbers < 0.5
            np.sum(heads)

        # Calculating the probability of 4 heads

            n_all_heads = 0 # Initialise no. trials with 4 heads

            # Simulate 10000 trials of 4 flips
            for _ in range(10000):
                heads = np.random.random(size=4) < 0.5
                n_heads = np.sum(heads)
                if n_heads == 4:
                    n_all_heads += 1

        # Predicting probability of defaults on a loan

            # 100 loans, p = 0.05 prob of default
            # Predicting probability of number of defaults from batch of 100 loans
            
            # Seed random number generator
            np.random.seed(42)

            # Initialize the number of defaults: n_defaults
            n_defaults = np.empty(1000)

            # Compute the number of defaults
            for i in range(1000):
                n_defaults[i] = perform_bernoulli_trials(100, 0.05)


            # Plot the histogram with default number of bins; label your axes
            _ = plt.hist(n_defaults, normed=True)
            _ = plt.xlabel('number of defaults out of 100 loans')
            _ = plt.ylabel('probability')

            # Show the plot
            plt.show()

        # Probability of bank losing money
            
            # Compute ECDF: x, y
            x, y = ecdf(n_defaults)

            # Plot the ECDF with labeled axes
            plt.plot(x,y, marker='.', linestyle='none')
            plt.xlabel('no. deafaults')
            plt.ylabel('ecdf')
            plt.show()

            # Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
            n_lose_money = np.sum(n_defaults >= 10)

            # Compute and print probability of losing money
            print('Probability of losing money =', n_lose_money / len(n_defaults))

    # Probability distributions

        # Probability mass function - set of probabilities of discrete outcomes
        # Probability distribution - mathematical description of outcomes

        # Discrete Uniform Distribution
            # The outcome of rolling a single fair die is discrete, uniformly distributed.

        # Binomial distribution
            # The number r of successes in n Bernoulli trials,
            # with probability p of success is Binomially distributed.

            samples = np.random.binomial(n, p, size=no_samples)

            # Binomial CDF
                import matplotlib.pyplot as plt
                import seaborn as sns
                
                sns.set()

                x, y = ecdf(samples)
                _ = plt.plot(x, y, marker='.', linestyle='none')
                plt.margins(0.02)
                _ = plt.xlabel('number of successes')
                _ = plt.ylabel('CDF')
                plt.show()

        # Poisson distribution

            # Poisson process - The timing of the next event is completely independent
            #                   of when the previous event happened.

            # Examples of Poisson proccesses:
                # Natural births in a given hospital
                # Hits on a website in a given hour
                # Meteor strikes
                # Molecular collisions in a gas
                # Aviation accidents

            # The number r of arrivals of a Poisson process in a given time
            # with an average rate of l arrivals per interval, is Poisson distributed.

            # Poisson distribution is the limit of the Binomial distribution
            # for low prob of success p (rare events) and large number of trials n.
            
            samples = np.random.poisson(mean, size=no_samples)

            # Poisson CDF

                samples = np.random.poisson(6,size=10000)
                x, y = ecdf(samples)
                plt.margins(0.02)
                _ = plt.xlabel('number of successes')
                _ = plt.ylabel('CDF')
                plt.show()

'''Thinking probabilistically - Continuous variables'''
    
    # Probability density functions

        # Continuous analogue to the PMF.
        # Mathematical description of the relative likelihood of observing a value of a continous variable.
        # Consider areas under curve to represent probabilites, as it doesn't make sense to consider probability of a single value

    # Normal distribution

        # Describes a continous variable whose PDF has a single symmetric peak
        # Parameterised by mean, st. dev.

        samples = np.random.normal(mean, std, size=no_samples)

        # Checking normality of Michaelson data

            import numpy as np

            mean = np.mean(michaelson_speed_of_light)
            std = np.stsd(michaelson_speed_of_light)

            samples = np.random.normal(mean, std, size=10000)

            x, y = ecdf(michaelson_speed_of_light)
            x_theor, y_theor = ecdf(samples)

'''Parameter estimation by optimization'''

    # Optimal parameters
        # Parameters that bring the model in closest agreement with the data
        # Not always the case that the mean and standard deviation of the data will match the optimal model parameters
    
    # Linear Regression by least squares
        # The process of finding the parameters for which the sum of the squares of the residuals is minimal

        np.polyfit() # Least squares with polynomials

        slope, intercept = np.polyfit(x, y, deg) # deg = degree of polynomial we want to fit

'''Bootstrap confidence intervals'''

    # Generating bootstrap replicates

        # We are not interested in the summary statistics of an individual experiment,
        # rather the summary statistics if we repeated the experiment many times.
        
        # We can simulate many experiments by resampling the results of our experiment

        # Bootstrapping - The use of resampled data to perform statistical inference

            # Bootstrap sample - A resampled array of data
            # Bootstrap replicate - Value of statistic computed from resampled array
        
        import numpy as np

        bs_sample = np.random.choice(array, size=sample_size)

    # Bootstrap confidence intervals

        # Bootstrap replicate function

            def boostrap_replicate_1d(data, func):
                '''Generate bootsrap replicate of 1D data'''
                bs_sample = np.random.choice(data, len(data))
                return(func(bs_sample))

        # Generate many bootstrap replicates

            bs_replicates = np.empty(10000)

             for i in range(10000):
                 bs_replicates[i] = boostrap_replicate_1d(
                                        michelson_speed_of_light, np.mean)

            # General function to generate many bootstrap replicates

                def draw_bs_reps(data, func, size=1):
                    """Draw bootstrap replicates."""

                    # Initialize array of replicates: bs_replicates
                    bs_replicates = np.empty(size)

                    # Generate replicates
                    for i in range(size):
                        bs_replicates[i] = bootstrap_replicate_1d(data, func)

                    return bs_replicates

        # Plot histogram of bootstrap replicates

            _ = plt.hist(bs_replicates, bins=30, normed=True)
            _ = plt.xlabel('mean_speed of light (km/s)')
            _ = plt.ylabel('PDF')
            plt.show()

            # Shows distribution of values likely on repeating the experiment many times
            # Normalisation means that we can see the relative probability of different values

        # Example

            # Take 10,000 bootstrap replicates of the mean
            bs_replicates = draw_bs_reps(rainfall, np.mean, 10000)

            # Compute and print SEM (standard error of the mean)
            sem = np.std(rainfall) / np.sqrt(len(rainfall))
            print(sem)

            # Compute and print standard deviation of bootstrap replicates
            bs_std = np.std(bs_replicates)
            print(bs_std)

            # Make a histogram of the results
            _ = plt.hist(bs_replicates, bins=50, normed=True)
            _ = plt.xlabel('mean annual rainfall (mm)')
            _ = plt.ylabel('PDF')

            # Show the plot
            plt.show()

            # Results
            # Notice that the SEM we got from the known expression and the bootstrap replicates
            # is the same and the distribution of the bootstrap replicates of the mean is Normal.
            
        # Confidence interval of a statistic

            # If we repeated measurements many times,
            # p% of the observed values would lie within the p% confidence interval

            # Since we simulated repeated experiments using boostrapping,
            # we may calculated a bootstrap confidence interval from out replicates

            # E.g. 95% confidence interval
            conf_int = np.percentile(bs_replicates, [2.5, 97.5])

    # Pairs bootstrap

        # Nonparametric inference - Make no assumptions about the model or probability distribution of underlying data

        # Pairs bootstrap for linear regression

            # Resample data in pairs
            # Compute slope and intercept from resampled data
            # Each slope and intercept is a bootstrap replicate
            # Compute confidence intervals from percentiles of bootstrap replicates

            # Generating a pairs bootstrap sample

                ind = np.arange(len(total_votes))
                bs_inds = np.random.choice(inds, len(inds))

                bs_total_votes = total_votes[bs_inds]
                bs_dem_share = dem_share[bs_inds]

                bs_slope, bs_intercept = np.polyfit(bs_total_votes,
                                                    bs_dem_share, 1)

                def draw_bs_pairs_linreg(x, y, size=1):
                    
                    """Perform pairs bootstrap for linear regression."""

                    # Set up array of indices to sample from: inds
                    inds = np.arange(len(x))

                    # Initialize replicates: bs_slope_reps, bs_intercept_reps
                    bs_slope_reps = np.empty(size)
                    bs_intercept_reps = np.empty(size)

                    # Generate replicates
                    for i in range(size):
                        bs_inds = np.random.choice(inds, size=len(inds))
                        bs_x, bs_y = x[bs_inds], y[bs_inds]
                        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y,1)

                    return bs_slope_reps, bs_intercept_reps

                # Example

                    # Generate array of x-values for bootstrap lines: x
                    x = np.array([0,100])

                    # Plot the bootstrap lines
                    for i in range(100):
                        _ = plt.plot(x, 
                                    bs_slope_reps[i]*x + bs_intercept_reps[i],
                                    linewidth=0.5, alpha=0.2, color='red')

                    # Plot the data
                    _ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

                    # Label axes, set the margins, and show the plot
                    _ = plt.xlabel('illiteracy')
                    _ = plt.ylabel('fertility')
                    plt.margins(0.02)
                    plt.show()

'''Introduction to Hypothesis Testing'''

    # Hypothesis Testing - Assessment of how reasonable the observed data are, assuming a hypothesis is true

        # Pipeline for hypothesis testing
            
            # Clearly state the null hypothesis
            # Define test statistic
            # Generate many sets of simulated data assuming the null hypothesis is true
            # Compute the test statistic for each simulated data set
            # p-value is fraction of simulated data sets for which test stat is at least as extreme as for the observed data

    # Permutation sampling
        # Comparing two probability distributions
        # Null hypothesis - two samples distributed exactly the same
        # Concatenate two samples and scramble data, as if they were exactly the same
        # Compare individual distributions to permutation sample distributions

        # Example

            def permutation_sample(data1, data2):
                """Generate a permutation sample from two data sets."""

                # Concatenate the data sets: data
                data = np.concatenate((data1, data2))

                # Permute the concatenated array: permuted_data
                permuted_data = np.random.permutation(data)

                # Split the permuted array into two: perm_sample_1, perm_sample_2
                perm_sample_1 = permuted_data[:len(data1)]
                perm_sample_2 = permuted_data[len(data1):]

                return perm_sample_1, perm_sample_2

            for i in range(0,50):
                # Generate permutation samples
                perm_sample_1, perm_sample_2 = permutation_sample(rain_june, rain_november)

                # Compute ECDFs
                x_1, y_1 = ecdf(perm_sample_1)
                x_2, y_2 = ecdf(perm_sample_2)

                # Plot ECDFs of permutation sample
                _ = plt.plot(x_1, y_1, marker='.', linestyle='none',
                            color='red', alpha=0.02)
                _ = plt.plot(x_2, y_2, marker='.', linestyle='none',
                            color='blue', alpha=0.02)

            # Create and plot ECDFs from original data
            x_1, y_1 = ecdf(rain_june)
            x_2, y_2 = ecdf(rain_november)
            _ = plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
            _ = plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')

            # Label axes, set margin, and show plot
            plt.margins(0.02)
            _ = plt.xlabel('monthly rainfall (mm)')
            _ = plt.ylabel('ECDF')
            plt.show()

            # Since ecdfs of original data do not overlap with the band of permutation sample ecdfs
            # we can conclude that the two datasets do not have identical distributions

    # Test statistics and p-values

        # Test statistic - A single number that can be computed form observed data and from data you simulate under the null hypothesis
        # Basis as comparison of two

        # Here, as we assume the two datasets are distributed equally, we would expect the means to be equal - i.e. their difference to be 0
        # Choose test statistic as difference between means

        # Permutation replicate - value of test statistic calculated from permutation sample
        np.mean(perm_sample_PA) - np.mean(perm_sample_OH)

        # We can simulate many permutation samples and calculate the permutation replicates
        # and then plot a histogram (PDF) of these values

        # p-value - The probability of obtaining a value of your test statistic at least as
        # extreme as what was observed, under assumption that null hypothesis is true
        # NOT probability of H0 being true

        # p-value can be calculated from area to right of observed value

        # Small p-value - statistically significantly different to H0

        # Example

            def draw_perm_reps(data_1, data_2, func, size=1):
                """Generate multiple permutation replicates."""

                # Initialize array of replicates: perm_replicates
                perm_replicates = np.empty(size)

                for i in range(size):
                    # Generate permutation sample
                    perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)

                    # Compute the test statistic
                    perm_replicates[i] = func(perm_sample_1, perm_sample_2)

                return perm_replicates

            def diff_of_means(data_1, data_2):
                """Difference in means of two arrays."""

                # The difference of means of data_1, data_2: diff
                diff = np.mean(data_1) - np.mean(data_2)

                return diff

            # Compute difference of mean impact force from experiment: empirical_diff_means
            empirical_diff_means = diff_of_means(force_a, force_b)

            # Draw 10,000 permutation replicates: perm_replicates
            perm_replicates = draw_perm_reps(force_a, force_b,
                                            diff_of_means, size=10000)

            # Compute p-value: p
            p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

            # Print the result
            print('p-value =', p)

    # Bootstrap hypothesis tests

        # Difference between boostrap sampling and permutation sampling

            # Permutation sampling --> Resampling without replacement
                # E.g. array([0,1,2,3]) --> array([1,3,0,2])

            # Bootstrap sampling --> Resampling with replacement
                # E.g. array([0,1,2,3]) --> array([2,1,2,3])

        # One sample test - comparing one set of data to a single number

            # Example
                # Context
                    # Michelson and Newcomb's independent experiments to calculate the speed of light
                    # Investigation whether the results are significantly different
                
                # Null hypothesis
                    # True mean speed of light of Michelson's experiment was actually Newcomb's reported value

                # Shift Michelson's data such that mean matches Newcomb's value
                    
                    newcomb_value = 299860 # km/s
                    michelson_shifted = michelson_speed_of_light - np.mean(michelseon_speed_of_light) + newcomb_value

                # Calculating the test statistic
                    
                    def diff_from_newcomb(data, newcomb_value=299860):
                        return np.mean(data) - newcomb_value

                    diff_obs = diff_from_newcomb(michelson_speed_of_light)

                # Computing the p-value
                    
                    bs_replicates = draw_bs_reps(michelson_shifted,
                                                diff_from_newcomb, 10000)
                    
                    p_value = np.sum(bs_replicates <= diff_observed) / 10000

                # Results
                    # p-value of 0.16 suggests that the two did not have significant differences in their measurements

        # Two sample test - comparing two sets of data

            # Example

                # Context -  Testing hpyothesis that Frog A anad Frog B have the same mean impact force

                # Compute mean of all forces: mean_force
                mean_force = np.mean(forces_concat)

                # Generate shifted arrays
                force_a_shifted = force_a - np.mean(force_a) + mean_force
                force_b_shifted = force_b - np.mean(force_b) + mean_force

                # Compute 10,000 bootstrap replicates from shifted arrays
                bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, size=10000)
                bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, size=10000)

                # Get replicates of difference of means: bs_replicates
                bs_replicates = bs_replicates_a - bs_replicates_b

                # Compute and print p-value: p
                p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
                print('p-value =', p)

'''Hypothesis Test Examples'''

    # A/B testing

        # Used by organisations to see if a strategy change gives a better result
        # Generally H0 is that test statistic is impervious to the change
        # Low p-value indicates change in strategy lead to improvement in performance 

        # Null hypothesis - click through rate not affected by redesign

        import numpy as np

        # clickthrough_A, clickthrough_B: array of 1s, 0s

        # Function to calculate test statistic - clickthrough rate
        def diff_frac(data_A, data_B):
            frac_A = np.sum(data_A) / len(data_A)
            frac_B = np.sum(data_B) / len(data_B)
            return frac_B - frac_A

        # Calculate test statistic for observed datasets
        diff_frac_obs = diff_frac(clickthrough_A, clickthrough_B)

        # Permutation test of clickthrough
        perm_replicates = np.empty(10000)
        
        for i in range(10000):
            perm_replicates[i] = permutation_replicate(clickthrough_A,
                                                       clickthrough_B
                                                       diff_frac)
        
        p_value = np.sum(perm_replicates >= diff_frac_obs) / 10000

    # Test of correlation

        # Null hypothesis - two variables are uncorrelated
        # Simulate data assuming null hypothesis true
        # Use Pearson correlation coefficient (ρ) as test statistic
        # Compute p-value as fract of replicates with ρ as large as observed

        # Case when no simulated values as extreme as test statistic
            # => p-value very very small, would have to generate and enormous number of replicates
            # to have even one as extreme as observed

        # Example - Testing siginificance of female illiteracy, fertility correlation

            # Compute observed correlation: r_obs
            r_obs = pearson_r(illiteracy, fertility)

            # Initialize permutation replicates: perm_replicates
            perm_replicates = np.empty(10000)

            # Draw replicates
            for i in range(10000):
                # Permute illiteracy measurments: illiteracy_permuted
                illiteracy_permuted = np.random.permutation(illiteracy)

                # Compute Pearson correlation
                perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

            # Compute p-value: p
            p = np.sum(perm_replicates > r_obs) / len(perm_replicates)
            print('p-val =', p)

'''Case Study'''

    '''Investigation of G.scandens beak depth'''

        # EDA of beak depths 1975 and 2012

            # Bee swarm plot

                # Create bee swarm plot
                _ = sns.swarmplot(x='year', y='beak_depth', data=df)

                # Label the axes
                _ = plt.xlabel('year')
                _ = plt.ylabel('beak depth (mm)')

                # Show the plot
                plt.show()

            #ECDFs

                # Compute ECDFs
                x_1975, y_1975 = ecdf(bd_1975)
                x_2012, y_2012 = ecdf(bd_2012)

                # Plot the ECDFs
                _ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
                _ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

                # Set margins
                plt.margins(0.02)

                # Add axis labels and legend
                _ = plt.xlabel('beak depth (mm)')
                _ = plt.ylabel('ECDF')
                _ = plt.legend(('1975', '2012'), loc='lower right')

                # Show the plot
                plt.show()

        # Parameter estimates of mean beak depth

            # Compute the difference of the sample means: mean_diff
            mean_diff = np.mean(bd_2012) - np.mean(bd_1975)

            # Get bootstrap replicates of means
            bs_replicates_1975 = draw_bs_reps(bd_1975, np.mean, 10000)
            bs_replicates_2012 = draw_bs_reps(bd_2012, np.mean, 10000)

            # Compute samples of difference of means: bs_diff_replicates
            bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

            # Compute 95% confidence interval: conf_int
            conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])

            # Print the results
            print('difference of means =', mean_diff, 'mm')
            print('95% confidence interval =', conf_int, 'mm')

        # Hypothesis test: did the beaks get deeper?

            # Compute mean of combined data set: combined_mean
            combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

            # Shift the samples
            bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
            bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

            # Get bootstrap replicates of shifted data sets
            bs_replicates_1975 = draw_bs_reps(bd_1975_shifted, np.mean, 10000)
            bs_replicates_2012 = draw_bs_reps(bd_2012_shifted, np.mean, 10000)

            # Compute replicates of difference of means: bs_diff_replicates
            bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

            # Compute the p-value
            p = (np.sum(
                bs_diff_replicates
                >= np.mean(bd_2012)
                - np.mean(bd_1975))
                / len(bs_diff_replicates))

            # Print p-value
            print('p =', p)

    '''Variation in beak shapes'''

        # EDA of beak length and depth

            # Make scatter plot of 1975 data
            _ = plt.scatter(bl_1975, bd_1975, marker='.',
                        linestyle='None', color='blue', alpha='0.5')

            # Make scatter plot of 2012 data
            _ = plt.scatter(bl_2012, bd_2012, marker='.',
                        linestyle='None', color='red', alpha=0.5)

            # Label axes and make legend
            _ = plt.xlabel('beak length (mm)')
            _ = plt.ylabel('beak depth (mm)')
            _ = plt.legend(('1975', '2012'), loc='upper left')

            # Show the plot
            plt.show()

        # Linear regression bootstrap confidence intervals

            # Compute the linear regressions
            slope_1975, intercept_1975 = np.polyfit(bl_1975, bd_1975, 1)
            slope_2012, intercept_2012 = np.polyfit(bl_2012, bd_2012, 1)

            # Perform pairs bootstrap for the linear regressions
            bs_slope_reps_1975, bs_intercept_reps_1975 = \
                    draw_bs_pairs_linreg(bl_1975,
                                        bd_1975,
                                        size=1000)
                                        
            bs_slope_reps_2012, bs_intercept_reps_2012 = \
                    draw_bs_pairs_linreg(bl_2012,
                                        bd_2012,
                                        size=1000)

            # Compute confidence intervals of slopes
            slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
            slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])

            intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])
            intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])


            # Print the results
            print('1975: slope =', slope_1975,
                'conf int =', slope_conf_int_1975)
            print('1975: intercept =', intercept_1975,
                'conf int =', intercept_conf_int_1975)
            print('2012: slope =', slope_2012,
                'conf int =', slope_conf_int_2012)
            print('2012: intercept =', intercept_2012,
                'conf int =', intercept_conf_int_2012)
                
        # Displaying linear regression results

            # Make scatter plot of 1975 data
            _ = plt.plot(bl_1975, bd_1975, marker='.',
                        linestyle='none', color='blue', alpha=0.5)

            # Make scatter plot of 2012 data
            _ = plt.plot(bl_2012, bd_2012, marker='.',
                        linestyle='none', color='red', alpha=0.5)

            # Label axes and make legend
            _ = plt.xlabel('beak length (mm)')
            _ = plt.ylabel('beak depth (mm)')
            _ = plt.legend(('1975', '2012'), loc='upper left')

            # Generate x-values for bootstrap lines: x
            x = np.array([10, 17])

            # Plot the bootstrap lines
            for i in range(100):
                plt.plot(x, bs_slope_reps_1975[i]*x + bs_intercept_reps_1975[i],
                        linewidth=0.5, alpha=0.2, color='blue')
                plt.plot(x, bs_slope_reps_2012[i]*x + bs_intercept_reps_2012[i],
                        linewidth=0.5, alpha=0.2, color='red')

            # Draw the plot again
            plt.show()

        # Beak length to depth ratio -  confidence intervals

            # Compute length-to-depth ratios
            ratio_1975 = bl_1975 / bd_1975
            ratio_2012 = bl_2012 / bd_2012

            # Compute means
            mean_ratio_1975 = np.mean(ratio_1975)
            mean_ratio_2012 = np.mean(ratio_2012)

            # Generate bootstrap replicates of the means
            bs_replicates_1975 = draw_bs_reps(ratio_1975, np.mean, 10000)
            bs_replicates_2012 = draw_bs_reps(ratio_2012, np.mean, 10000)

            # Compute the 99% confidence intervals
            conf_int_1975 = np.percentile(bs_replicates_1975, [0.5, 99.5])
            conf_int_2012 = np.percentile(bs_replicates_2012, [0.5, 99.5])

            # Print the results
            print('1975: mean ratio =', mean_ratio_1975,
                'conf int =', conf_int_1975)
            print('2012: mean ratio =', mean_ratio_2012,
                'conf int =', conf_int_2012)

    '''Calculation of heritability'''

        # Heredity - The tendancy for parental traits to be inherited by offspring

        # EDA of heritability

            # Make scatter plots
            _ = plt.plot(bd_parent_fortis, bd_offspring_fortis,
                        marker='.', linestyle='none', color='blue', alpha=0.5)
            _ = plt.plot(bd_parent_scandens, bd_offspring_scandens,
                        marker='.', linestyle='none', color='red', alpha=0.5)

            # Label axes
            _ = plt.xlabel('parental beak depth (mm)')
            _ = plt.ylabel('offspring beak depth (mm)')

            # Add legend
            _ = plt.legend(('G. fortis', 'G. scandens'), loc='lower right')

            # Show plot
            plt.show()

        # Correlation of offsrping and parental data

            def draw_bs_pairs(x, y, func, size=1):
                """Perform pairs bootstrap for a single statistic."""

                # Set up array of indices to sample from: inds
                inds = np.arange(len(x))

                # Initialize replicates: bs_replicates
                bs_replicates = np.empty(size)

                # Generate replicates
                for i in range(size):
                    bs_inds = np.random.choice(inds, len(inds))
                    bs_x, bs_y = x[bs_inds], y[bs_inds]
                    bs_replicates[i] = func(bs_x, bs_y)

                return bs_replicates

            # Compute the Pearson correlation coefficients
            r_scandens = pearson_r(bd_parent_scandens, bd_offspring_scandens)
            r_fortis = pearson_r(bd_parent_fortis, bd_offspring_fortis)

            # Acquire 1000 bootstrap replicates of Pearson r
            bs_replicates_scandens = draw_bs_pairs(bd_parent_scandens,
                                                bd_offspring_scandens,
                                                pearson_r, size=1000)

            bs_replicates_fortis = draw_bs_pairs(bd_parent_fortis,
                                                bd_offspring_fortis,
                                                pearson_r, size=1000)

            # Compute 95% confidence intervals
            conf_int_scandens = np.percentile(bs_replicates_scandens, [2.5, 97.5])
            conf_int_fortis = np.percentile(bs_replicates_fortis, [2.5, 97.5])

            # Print results
            print('G. scandens:', r_scandens, conf_int_scandens)
            print('G. fortis:', r_fortis, conf_int_fortis)

        # Measuring heritability

            def heritability(parents, offspring):
                """Compute the heritability from parent and offspring samples."""
                covariance_matrix = np.cov(parents, offspring)
                return(covariance_matrix[1,0] / covariance_matrix[0,0])

            # Compute the heritability
            heritability_scandens = heritability(bd_parent_scandens, bd_offspring_scandens)
            heritability_fortis = heritability(bd_parent_fortis, bd_offspring_fortis)

            # Acquire 1000 bootstrap replicates of heritability
            replicates_scandens = draw_bs_pairs(
                    bd_parent_scandens, bd_offspring_scandens, heritability, size=1000)
                    
            replicates_fortis = draw_bs_pairs(
                    bd_parent_fortis, bd_offspring_fortis, heritability, size=1000)


            # Compute 95% confidence intervals
            conf_int_scandens = np.percentile(replicates_scandens, [2.5, 97.5])
            conf_int_fortis = np.percentile(replicates_fortis, [2.5, 97.5])

            # Print results
            print('G. scandens:', heritability_scandens, conf_int_scandens)
            print('G. fortis:', heritability_fortis, conf_int_fortis)

        # Is beak depth heritable at all in G.scandens?

            # Initialize array of replicates: perm_replicates
            perm_replicates = np.empty(10000)

            # Draw replicates
            for i in range(10000):
                # Permute parent beak depths
                bd_parent_permuted = np.random.permutation(bd_parent_scandens)
                perm_replicates[i] = heritability(bd_parent_permuted, bd_offspring_scandens)


            # Compute p-value: p
            p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

            # Print the p-value
            print('p-val =', p)
