# def country codes from string (need to split twice, once at ', ' and once at '$'. therefore need two new lists)
    # make a new empty list for the end result
    # make a new list that breaks up at ', ' called price_list. Output: new list cc/price cc/price etc
    # iterate through that new price_list
        # create variable and split on '$'. Output: each element from previous list is now in a new list w/ 2 elements: cc | price
        # create variable and select the zero index of the newly created split list country_code, which is cc
        # append cc to empty country_list
    # return and clean up the output 

def get_country_codes(prices):
    country_list = [] # new list for end result
    price_list = prices.split(', ') # start by splitting at ', '. Elements are each of the cc/price
    for item in price_list: # iterate through the newly created list. Each item(element) is cc/price
        dollar_split = item.split('$') # split at the '$'. Each individual item(element) is split into a new list: cc | price (2 elements per "item")
        country_code = dollar_split[0] # identify country_code by selecting the 0-index of the dollar_split list
        country_list.append(country_code) # append the country_code to the empty country_list
        
    return ", ".join(country_list) # join with ", "
