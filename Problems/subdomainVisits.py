# https://leetcode.com/problems/subdomain-visit-count/description/


def subdomain_visits(cpdomains):
	store = {}

	for item in cpdomains:
		new_item = item.split(" ", 1)
		domain = new_item[1].split(".")
		for i in range(len(domain)):
			item = ".".join(domain[i:])
			if item not in store:
				store[item] = int(new_item[0])
			else:
				store[item] += int(new_item[0])
	res = []
	for item in store:
		res.append(str(store[item]) + " " + item)
	return res




cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print subdomain_visits(cpdomains)

