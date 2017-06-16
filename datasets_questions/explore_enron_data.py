#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Data points:", len(enron_data)
print "Features:", len(enron_data[enron_data.keys()[0]])
poi_count = sum(1 for x in enron_data.values() if x["poi"])
print "POIs:", poi_count
print "James Prentice Total Stock:",  enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Messages from Wesley to POI:",  enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffrey Stock options:",  enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Jeffrey Payments:",  enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Kenneth Payments:",  enron_data["LAY KENNETH L"]["total_payments"]
print "Fastow Payments:",  enron_data["FASTOW ANDREW S"]["total_payments"]
print "Salary Data Count:", sum(1 for x in enron_data.values() if not (x["salary"] == "NaN"))
print "Email Address Count:", sum(1 for x in enron_data.values() if not (x["email_address"] == "NaN"))
missing_total_payments = sum(1 for x in enron_data.values() if (x["total_payments"] == "NaN"))
print "Missing total payments:", missing_total_payments, " [", missing_total_payments*100/len(enron_data), "]%" 
poi_missing_payments = sum(1 for x in enron_data.values() if (x["total_payments"] == "NaN" and x["poi"]))
print "Missing POI payments:", poi_missing_payments, " [", poi_missing_payments*100/poi_count, "]%"
#print "Fastow data:", enron_data["FASTOW ANDREW S"]