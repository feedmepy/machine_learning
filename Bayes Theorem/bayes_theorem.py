# Bayes' Theorem
print("\nBefore you start looking at the code, keep in mind that idea we use here is 100 = 1.0, thats why we devide everyhting with 100!")

print("\nLet's say that 0.3 percent of the overall population use one drug!")

# P(A) probability of drug users in general
drug_users = 0.003 

# Probability of testing positive if you do use times probability that you are a user, 
# plus the probability of testing positive if you don't use times  probability that you are not a user
# P(B)
probability_B = (0.99*0.003 + 0.01*0.997)
print("\nProbability of testing positvley overall: ", probability_B)

# P(B|A)  Probability of testing positive if you are a user, we know that tests give us 99% accurancy
probability_B_A = 0.99
print("\nProbability of testing positive if you are a user, we know that tests give us 99 percent accurancy: ", probability_B_A)

probability_A_B = ((drug_users*probability_B_A) / probability_B)*100
print("\nThis is probability that you are a user given that you tested positivley: ", probability_A_B)

print("\nLook for the images in the folder and you'll find the complte explenation for this to undertand!")
