# SVM_CAPP
# (Support Vector Machine Cyber Attack Prediction Project)
# 
# Th SVM CAPP project takes both the Center for Strategic and Internation Studies (CSIS) cyber event data and The World Bank data 
concerning global events (source data), and then processes that data using the Support Vector Machine (SVM) algorithm to predict a 
target cyber event (target data).  The project has  been implemented utilizing the programming language Python, version 3.7, on the Pycharm 
IDE (Integrated Development Environment), as well as the Scikit Learn library SVM algorithm.  Other libraries utilized the SVM CAPP
project include:
# 
# - tkinter
# - numpy
# - pandas
# - xlrd
# 
# The SVM algorithm is a supervised machine learning (ML) algorithm often used for classification and regression purposes.  The term 
# 'supervised' indicates a referenced set of data for set training is involved within the algorithmic process. 
# The Scikit Learn SVM algorithm appeared, per this author's experience, only to work utilizing floats.  Therefore, all strings
# within the dataset had to be transformed into float format. 
# 
# The referenced datasets are in the project files, and include:
# CSIS:
# Significant Cyber Incidents Since 2006
# https://csis-prod.s3.amazonaws.com/s3fs-public/200306_Significant_Cyber_Events_List.pdf?qRZXF65CUUOKTOl9rLVBMJhXfXtmJZMj
# 
# The World Bank:
# Gross PSD (Quarterly Public Sector Debt), Central Gov., All maturities, Debt securities, Nominal Value, % of GDP
# https://databank.worldbank.org/source/quarterly-public-sector-debt#
# World Development Indicator, Global access to clean fuels and technologies for cooking (% of population)# 
# World Development Indicator, Global access to electricity (% of population)
# https://databank.worldbank.org/source/world-development-indicators
#
# The CSIS dataset was referenced.  For regions or timelines not mentioned within the dataset, the project author either 
# showed within the dataset as 'Unlisted', or performed research of public websites to determine the eventual likely 
# attack origin or target entity or location that could be included within the dataset.  Similarly, for data missing within the 
# World Bank dataset, the author calculated average growth of previous data, in order to include likely future data.  For instance, 
# the author had to do this for years 2017 - 2020 in the 'Access to clean fuels and technologies for cooking (% of population)'
# and years 2018 - 2020 in the Access to electricity (% of population)  World Bank Datasets. In summary, the dataset utilized for 
# this project is a supervised dataset that is a hybrid of referenced and calculated data, combined and hand-created by the author
# into a cumulative format, in excel. 
# 
# Consideration to take into account concerning the project:
# 
# - Some of the data within the dataset could be considered subjective, as some of the referenced data was periodically vague.
# If an organization was listed within an event dataset as being the victim of a cyber attack, the author attempted to maintain 
# dataset consistence by listing the country or region of the company's headquarters, unless an specific location was mentioned as that # company's particular attack location. However, if an organization is known widely to the global public, the author would
# sometimes list that company, group, or organization (i.e. Al Quaida, CSIS, and the Decentralized_International_Hacktivist_Group).
#
# When multiple regions were involved, they were listed in alphabetical order within the same data entry. The author was
# hoping to be able to associate multiple regions being involved together within events, during attempts at correlation or prediction. 
# 
# Limits within the dataset:
# 
# - The dataset only allows for limited choice of targets that have already acted as origins or targets, so only those targets can be # # # # included in the prediction at this time 
# - The strings Unlisted and Multiple used for unknown holes in the data could cause limits in accurate prediction abilty  
# - Some of the dates the author referenced were extended, lasting sometime for years. This was not always shown across the
# newly created dataset due to time constraints of the author
# 
# Recommendations for project continuence in the future:
# 
# - The project currently shows an algorithmic accuracy of 31% for the Attack Target Prediction page (to predict a target attack location)
# The author concludes that this might be due to the less variable event origin data utilized within the source data for that 
# algorithm.  The Attack Origin prediction page does have a slightly higher prediction accuracy of 37%.  This is shown when 
# clicking on the Prediction Accuracy buttons within the program, at the bottom of the prediction pages.  
# 
# - With more time or manpower, an improved dataset could be created and cross-checked professionally for accuracy.  Corporate or 
# locational proprietary boundaries might also be challenge faced upon improving the dataset (not all locations would want to 
# publicize that they were involved in a cyber attack, so an attack or its details might not become publicely available).
# 
# - The scrollbar within the dataset would also need to be corrected.  At this time it works, but is very small.  It is located on the
# bottom-left corner of each prediction page. 
# 
# - Legal issues of dataset utilization would need taken into account.  Permissions may be required for application publication
# and sharing. 
# 
# The author's wish for this program is that it might assist the cyber community with correlating data of cyber event prediction,
# with data that has not been involved or utilized to do so prior.  Although only the future would present if such correlations
# could be proven as accurate, the SVM CAPP might make that possible. 
"# PowerPredictionAZ" 
"# PowerBallAZ" 
