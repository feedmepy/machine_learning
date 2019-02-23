import math
print("\nMean, Differences, Squared Differences, Variance, Standard Deviation, Covariance and Correlation Coefficient!")
# calculating  differences, variable initial_diff will hold the differences
class Make_Differences(object):
	def __init__(self, list, mean):
		self.list = list
		self.mean = mean

	def differences(self):
		initial_diff =[]
		
		for xy in self.list:		
			addx = xy - self.mean
			initial_diff.append(addx)	
			
		return(initial_diff)

# calculating squared differences, variable squared_diff will hold the sqaured differences
class Make_Squared_Differences(object):
	def __init__(self, list, mean):
		self.list = list
		self.mean = mean

	def squared_differences(self):
		squared_diff =[]
		
		for xy in self.list:		
			addx = (xy - self.mean) * (xy - self.mean)
			squared_diff.append(addx)	
			
		return(squared_diff)


print("\n *** Mean, Squared Differences, Variance and Standard Deviation of the weight list  *** ")
weight_list = [85, 85, 90, 100, 110]
mean_weight = sum(weight_list) / len(weight_list)
print("\nYour weight list: ", weight_list)
print("This is the mean for the given weight list: ", mean_weight)


sq_weight = Make_Squared_Differences(weight_list, mean_weight)
sq_diff_weight =  sq_weight.squared_differences()
print("Squared Differences of weight and and mean are: ", sq_diff_weight)


print("The SUM of squared differences for WEIGHT and its mean is: ", sum(sq_diff_weight))


variance =  sum(sq_diff_weight) / len(sq_diff_weight)
print("The Variance of weight list is: ", variance)

print("Standard deviaton of weight list is: ", math.sqrt(variance))

print("\n *** Mean, Squared Differences, Variance and Standard Deviation of the age list *** ")
age_list = [28, 28, 28, 30, 29]
mean_age = sum(age_list) / len(age_list)
print("\nYour age list: ", age_list)
print("This is the mean for the given age list: ", mean_age)


sq_age = Make_Squared_Differences(age_list, mean_age)
sq_diff_age =  sq_age.squared_differences()
print("Squared Differences of age and and mean are: ", sq_diff_age)

print("The SUM of squared differences for AGE and its mean is: ", sum(sq_diff_age))

variance_two =  sum(sq_diff_age) / len(sq_diff_age)
print("The Variance for age list is: ", variance_two)

print("Standard deviaton for age list is: ", math.sqrt(variance_two))

print("\n *** Calculating Differences of weight and age  ***  ")
x = Make_Differences(weight_list, mean_weight)
diff_one_weight =  x.differences()
print("\nDifferences of weight: ", diff_one_weight)


y = Make_Differences(age_list, mean_age)
diff_two_age =  y.differences()
print("Differences of age: ", diff_two_age)


print("\n *** Calculating Covariance and Correlation Coefficient  *** ")
covariance_weight_age = (diff_one_weight[0] * diff_two_age[0], diff_one_weight[1] * diff_two_age[1], diff_one_weight[2] * diff_two_age[2], diff_one_weight[3] * diff_two_age[3], diff_one_weight[4] * diff_two_age[4])
print("\nHere is the covariance list of age and weight before adding together: ", covariance_weight_age)

print("The result after adding: ", sum(covariance_weight_age))

covariance_x_y = sum(covariance_weight_age) / len(covariance_weight_age)
print("Here is the Covariance of weight and age: ", covariance_x_y )

print("\n *** Correlation Coefficient *** ")
print("\nA correlation coefficient will always be between -1 and 1.")
print("The closer the value is to -1 or 1, the strong the relationship, the closer to 0 then the weaker it is.")

r_x_y = covariance_x_y / (math.sqrt(variance) * math.sqrt(variance_two))
print("\n\tAnd finaly your correlation coefficient result is: ", r_x_y)