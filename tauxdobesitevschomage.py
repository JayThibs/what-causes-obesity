import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

NLObesitystd = np.std([63.2, 69.3, 63.2, 69.2, 67.5])
PEIObesitystd = np.std([56.6, 57.6, 61.3, 64.4, 61.0])
NSObesitystd = np.std([61.1, 61.0, 60.5, 61.0, 62.6])
NBObesitystd = np.std([62.8, 59.4, 60.8, 64.3, 64.0])
QCObesitystd = np.std([51.8, 50.1, 50.8, 53.0, 51.4])
ONObesitystd = np.std([52.6, 52.3, 52.9, 53.2, 54.6])
MNObesitystd = np.std([60.7, 58.4, 56.3, 56.9, 61.5])
SASKObesitystd = np.std([58.9, 59.4, 59.5, 61.1, 58.4])
ABObesitystd = np.std([51.6, 52.2, 53.1, 54.6, 55.0])
BCObesitystd = np.std([44.4, 46.6, 46.5, 46.9, 48.0])
YUObesitystd = np.std([51.8, 55.0, 51.5, 64.2, 57.1])
NTObesitystd = np.std([54.2, 60.7, 61.9, 57.4, 64.7])
NUNObesitystd = np.std([60.1, 58.2, 54.4, 59.5, 49.4])

NLChomagestd = np.std([15.1, 13.8])
PEIChomagestd = np.std([10.5, 9.8])
NSChomagestd = np.std([8.3, 7.7])
NBChomagestd = np.std([9.3, 8.9])
QCChomagestd = np.std([6.5, 6.2])
ONChomagestd = np.std([6.4, 6.4])
MNChomagestd = np.std([6.3, 6.1])
SASKChomagestd = np.std([6.6, 6.4])
ABChomagestd = np.std([8.5, 8.8])
BCChomagestd = np.std([5.8, 5.6])
YUChomagestd = np.std([5.5])
NTChomagestd = np.std([8])
NUNChomagestd = np.std([13.5])

NLObesitymean = np.mean([63.2, 69.3, 63.2, 69.2, 67.5])
PEIObesitymean = np.mean([56.6, 57.6, 61.3, 64.4, 61.0])
NSObesitymean = np.mean([61.1, 61.0, 60.5, 61.0, 62.6])
NBObesitymean = np.mean([62.8, 59.4, 60.8, 64.3, 64.0])
QCObesitymean = np.mean([51.8, 50.1, 50.8, 53.0, 51.4])
ONObesitymean = np.mean([52.6, 52.3, 52.9, 53.2, 54.6])
MNObesitymean = np.mean([60.7, 58.4, 56.3, 56.9, 61.5])
SASKObesitymean = np.mean([58.9, 59.4, 59.5, 61.1, 58.4])
ABObesitymean = np.mean([51.6, 52.2, 53.1, 54.6, 55.0])
BCObesitymean = np.mean([44.4, 46.6, 46.5, 46.9, 48.0])
YUObesitymean = np.mean([51.8, 55.0, 51.5, 64.2, 57.1])
NTObesitymean = np.mean([54.2, 60.7, 61.9, 57.4, 64.7])
NUNObesitymean = np.mean([60.1, 58.2, 54.4, 59.5, 49.4])

NLChomagemean = np.mean([15.1, 13.8])
PEIChomagemean = np.mean([10.5, 9.8])
NSChomagemean = np.mean([8.3, 7.7])
NBChomagemean = np.mean([9.3, 8.9])
QCChomagemean = np.mean([6.5, 6.2])
ONChomagemean = np.mean([6.4, 6.4])
MNChomagemean = np.mean([6.3, 6.1])
SASKChomagemean = np.mean([6.6, 6.4])
ABChomagemean = np.mean([8.5, 8.8])
BCChomagemean = np.mean([5.8, 5.6])
YUChomagemean = np.mean([5.5])
NTChomagemean = np.mean([8])
NUNChomagemean = np.mean([13.5])


tauxDObesiteParProvince = {"Newfoundland and Labrador": NLObesitymean, "Prince Edward Island": PEIObesitymean,
                           "Nova Scotia": NSObesitymean, "New Brunswick": NBObesitymean, "Quebec": QCObesitymean,
                           "Ontario": ONObesitymean,"Manitoba": MNObesitymean, "Saskatchewan": SASKObesitymean,
                           "Alberta": ABObesitymean, "British Columbia": BCObesitymean, "Yukon": YUObesitymean,
                           "Northwest Territories": NTObesitymean, "Nunavut": NUNObesitymean}

tauxDeChomageParProvince = {"Newfoundland and Labrador": NLChomagemean, "Prince Edward Island": PEIChomagemean,
                           "Nova Scotia": NSChomagemean, "New Brunswick": NBChomagemean, "Quebec": QCChomagemean,
                           "Ontario": ONChomagemean,"Manitoba": MNObesitymean, "Saskatchewan": SASKChomagemean,
                           "Alberta": ABChomagemean, "British Columbia": BCChomagemean, "Yukon": YUChomagemean,
                           "Northwest Territories": NTChomagemean, "Nunavut": NUNChomagemean}

tauxDObesite = [NLObesitymean, PEIObesitymean, NSObesitymean, NBObesitymean, QCObesitymean, ONObesitymean, MNObesitymean,
                SASKObesitymean, ABObesitymean, BCObesitymean, YUObesitymean, NTObesitymean, NUNObesitymean]
tauxDeChomage = [NLChomagemean, PEIChomagemean, NSChomagemean, NBChomagemean, QCChomagemean, ONChomagemean, MNChomagemean,
                SASKChomagemean, ABChomagemean, BCChomagemean, YUChomagemean, NTChomagemean, NUNChomagemean]

tauxDObesiteError = [NLObesitystd, PEIObesitystd, NSObesitystd, NBObesitystd, QCObesitystd, ONObesitystd, MNObesitystd,
                SASKObesitystd, ABObesitystd, BCObesitystd, YUObesitystd, NTObesitystd, NUNObesitystd]
tauxDeChomageError = [NLChomagestd, PEIChomagestd, NSChomagestd, NBChomagestd, QCChomagestd, ONChomagestd, MNChomagestd,
                SASKChomagestd, ABChomagestd, BCChomagestd, YUChomagestd, NTChomagestd, NUNChomagestd]

tauxDObesite = np.reshape(tauxDObesite, (13,1))
tauxDeChomage = np.reshape(tauxDeChomage, (13,1))

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(tauxDeChomage, tauxDObesite)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(tauxDeChomage) - tauxDObesite) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(tauxDeChomage, tauxDObesite))

plt.scatter(tauxDeChomage, tauxDObesite)
plt.plot(tauxDeChomage, regr.predict(tauxDeChomage), color='red',
         linewidth=3)
plt.errorbar(tauxDeChomage, tauxDObesite, yerr=tauxDObesiteError, xerr=tauxDeChomageError,
             fmt='o', capsize = 5)
plt.axes().grid()
plt.axes().set_xlim([0, 20])
plt.axes().set_ylim([40, 70])
plt.xlabel('% of people unemployed')
plt.ylabel('% of people who are obese')
plt.title('Relation between unemployment and obesity in Canadian provinces')
plt.show()
