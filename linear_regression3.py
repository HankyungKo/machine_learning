import statsmodels.api
import numpy

def main():
    (N, X, Y) = read_data()

    results = do_multivariate_regression(N, X, Y)
    print(results.summary())

    effective_variables = get_effective_variables(results)
    print(effective_variables)

def read_data():
    # 1
    f = open("students.dat", "r")
    f.readline()
    N = 30
    X = numpy.zeros((30, 5))
    Y = numpy.zeros((30, 1))
    for i in range(0, 30):
        temp = f.readline().strip().split(" ")
        X[i] = [float(each) for each in temp[0:5]]
        Y[i] = temp[5]
        
    return (N, X, Y)

def do_multivariate_regression(N, X, Y):
    # 2
    return statsmodels.api.OLS(Y, X).fit()

def get_effective_variables(results):
    eff_vars = []
    pvals = results.pvalues
	# 3
    for i in range(len(pvals)):
        if pvals[i] < 0.05:
            eff_vars.append("x%d"%(i+1))
            
    return eff_vars

if __name__ == "__main__":
    main()