""" Create a script that take a month price, an annual price and time of use, and tell you if the deal is a good deal or not"""

from setup_calendar import get_credentials, final_time, create_event


def compare_prices(month, annual, time):
    """Given a price by month, annual and and amount of time in months, determine if a deal is good or not"""

    full_month = month * 12
    full_annual = annual * 12
    full_use = month * time

    if full_use < full_annual:
        saving = full_annual - full_use
        saving_months = saving / annual
        print "Buy it by month. You're using %i and saving %i months" % (time, saving_months)
        return 1
    else:
        saving = full_use - full_annual
        saving_months = saving / month
        print "Buy it by annual. You're using %i and saving %i months" % (time, saving_months)
        return -1

if __name__ == "__main__":

    prompt = raw_input("Welcome. Let's see if you're making a good deal")
    month_price = float(raw_input("Please give me the month price of the suscription: "))
    annual_price = float(raw_input("Please give me the annual price of the suscription: "))
    time_in_months = int(raw_input("How much time (in months) do you think you will be using the suscription: "))
    saving = compare_prices(month_price, annual_price, time_in_months)

    if saving == 1:
        months = final_time(time_in_months)
        print "You said that you will use the suscription until %s" % (months)
        ask_user = raw_input("Do you want to save a reminder of this event: Y or N  ")
        if ask_user == 'Y':
            name_suscription = raw_input("Please, give the name of the suscription that you want to save: ")
            start_time = end_time = months
            event = create_event(start_time, end_time, name_suscription)
            print('''*** %r event added:
                    Start: %s
                    End:   %s''' % (event['summary'].encode('utf-8'),
                                    event['start']['dateTime'], event['end']['dateTime'])) 

        elif ask_user == 'N':
            print "Ok. You know that it's a good deal, but you don't want to compromise"

        else:
            print "I don't understand what you're asking me"

    elif saving == -1:
        months = final_time(time_in_months)
        print "You said that you will use the suscription until %s" % (months)
        ask_user = raw_input("Do you want to save a reminder of this event: Y or N  ")
        if ask_user == 'Y':
            name_suscription = raw_input("Please, give the name of the suscription that you want to save: ")
            start_time = end_time = months
            event = create_event(start_time, end_time, name_suscription)
            print('''*** %r event added:
                    Start: %s
                    End:   %s''' % (event['summary'].encode('utf-8'),
                                    event['start']['dateTime'], event['end']['dateTime']))

        elif ask_user == 'N':
            print "Ok. You know that it's a good deal, but you don't want to compromise"

        else:
            print "I don't understand what you're asking me"

