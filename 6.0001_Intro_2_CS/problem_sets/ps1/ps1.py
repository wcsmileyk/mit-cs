def no_raise_calc(salary, saving, cost, s_rate):
    '''
    Calculate months it will take to save based on a fixed salary and investment rate
    :param salary: Annual salary
    :param saving: Percent of monthly salary saving
    :param cost: Total cost of house
    :param s_rate: Investment rate on savings
    :return: Months to save
    '''
    monthly_salary = salary / 12
    current_savings = 0
    portion_down_payment = cost * 0.25

    months_to_save = 0

    while current_savings < portion_down_payment:
        months_to_save += 1
        current_savings += current_savings * s_rate/12
        current_savings += monthly_salary * saving

    return months_to_save


def with_raise_calc(salary, saving, cost, r_rate, s_rate):
    '''
    Calculate months it will take to save based on an expected semi-annual raise rate and a fixed investment rate
    :param salary: Annual salary
    :param saving: Percent of monthly salary saving
    :param cost: Total cost of house
    :param r_rate: Semi-annual raise percentage, as a float
    :param s_rate: Investment rate on savings
    :return:
    '''
    annual_salary = salary
    current_savings = 0
    portion_down_payment = cost * 0.25

    months_to_save = 0

    while current_savings < portion_down_payment:
        monthly_salary = annual_salary / 12
        months_to_save += 1
        current_savings += current_savings * s_rate/12
        current_savings += monthly_salary * saving
        if months_to_save % 6 == 0:
            annual_salary += annual_salary * r_rate

    return months_to_save, current_savings


def find_savings(salary):
    '''
    Determine ideal savings rate to meet savings goal on house purchase in desired timeline
    :salary: Annual salary (float)
    :return: ideal savings percentage
    '''
    raise_rate = .07
    invest_rate= .04
    saving_amt = 250000
    epsilon = 100
    low = 0
    high = 10000
    guess = int((low + high) / 2)
    steps = 0
    total_savings = 0
    while abs(saving_amt - total_savings) >= epsilon:
        annual_salary = salary
        saving_rate = guess / 10000
        current_savings = 0
        for month in range(1, 37):
            monthly_salary = annual_salary / 12
            current_savings += current_savings * invest_rate / 12
            current_savings += monthly_salary * saving_rate
            if month % 6 == 0:
                annual_salary += annual_salary * raise_rate
        if current_savings < saving_amt:
            low = guess
        else:
            high = guess
        guess = int((low + high) / 2)
        steps += 1
        total_savings = current_savings






    return saving_rate, steps




if __name__ == '__main__':

    r = 0.04

    calc = input('Which calculation? a - No raise, b - raise, c - how much to save? ')

    annual_salary = float(input('How much do you make? '))
    if calc == 'a' or calc == 'b':
        portion_saved = float(input('Percentage of monthly salary saved (as a decimal)? '))
        total_cost = float(input('How much does the house cost? '))

        if calc == 'b':
            raise_rate = float(input('Semi-annual raise percent (as a decimal)? '))

            months_to_save = with_raise_calc(annual_salary, portion_saved, total_cost, raise_rate, r)

        else:
            months_to_save = no_raise_calc(annual_salary, portion_saved, total_cost, r)
        print('Months to save down payment:', months_to_save)

    else:
        ideal_savings, step_count = find_savings(annual_salary)
        print('Best savings rate: ', ideal_savings)
        print('Steps in bisection guess: ', step_count)

