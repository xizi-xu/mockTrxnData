import csv
import itertools
import random
from faker import Factory

# check length of a value
def numberLenCheck(value, length):
	while value < 10**(length-1):
			value = int(str(value) + str(random.randint(0,9)))

	return value


def fileGenerator():
	fake = Factory.create()

	with open('outputfile', 'wb') as csvfile:
		mywriter = csv.writer(csvfile, delimiter = "\001")
		# schema:
		# 'acct_id', 'stmt_dt', 'trxn_dt', 'dbt_crd_ind', 'mrcht_cat', 'amt_trxn', 'trxn_cd'
		
		for i in range(1, 100):
			seed = random.randint(0, 100)
			fake.seed(seed)
			acct_id = fake.random_number(digits = 11)
			acct_id = numberLenCheck(acct_id, 11)

			stmt_dt = fake.date_time_this_year().strftime("%Y%m%d")
			trxn_dt = fake.date_time_this_month().strftime("%Y%m%d")
			dbt_crd_ind = fake.random_element(['D', 'C'])
			mrcht_cat = numberLenCheck(fake.random_number(digits = 4), 4)
			amt_trxn = fake.random_number(digits = 17)
			trxn_cd = numberLenCheck(fake.random_number(digits = 4), 4)

			mywriter.writerow([acct_id, stmt_dt, trxn_dt, dbt_crd_ind, mrcht_cat, amt_trxn, trxn_cd])

if __name__ == '__main__':
	fileGenerator()