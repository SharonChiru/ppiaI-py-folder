def calculate_net_worth():
    # Sample input values
    user_name = "Sharon Chiru"
    checking_account_balance = 5000.00
    savings_account_balance = 10000.00
    investment_account_value = 15000.00
    total_utility_bills = 500.00
    total_credit_card_debt = 8000.00
    credit_card_balance_due = 6000.00
    credit_card_min_payment_due = 200.00
    annual_credit_card_interest_rate = 0.18  # 18%
    loan_debt = 12000.00
    loan_payment_due = 1000.00
    annual_loan_interest_rate = 0.10  # 10%
    other_asset_value = 20000.00

    # Calculations
    total_assets = checking_account_balance + savings_account_balance + investment_account_value + other_asset_value
    total_debt = total_utility_bills + total_credit_card_debt + loan_debt
    total_net_worth = total_assets - total_debt

    total_bills_due = total_utility_bills + credit_card_balance_due + loan_payment_due
    remaining_in_checking = checking_account_balance - total_bills_due
    total_remaining_money_in_bank = remaining_in_checking + savings_account_balance

    credit_card_debt_after_payment = total_credit_card_debt - credit_card_balance_due
    loan_debt_after_payment = loan_debt - loan_payment_due + ((loan_debt - loan_payment_due) * annual_loan_interest_rate / 12)

    total_debt_after_payment = loan_debt_after_payment + credit_card_debt_after_payment
    net_worth_after_payment = total_assets - total_utility_bills - loan_payment_due - credit_card_min_payment_due - \
                              loan_debt_after_payment - credit_card_debt_after_payment

    # Output report
    print("\nHello {},".format(user_name))
    print("\nThe total dollar value of assets you own is ${:.2f} and the total dollar value of your debt is currently ${:.2f}; therefore, your current net worth is: ${:.2f}".format(total_assets, total_debt, total_net_worth))
    print("\nYour total bills due are ${:.2f}. Once you make these payments, you will have ${:.2f} left in your checking account, and ${:.2f} in your bank overall.".format(total_bills_due, remaining_in_checking, total_remaining_money_in_bank))
    print("Additionally, your total credit card debt will be down to ${:.2f} and your loan debt will be ${:.2f}, including interest applied on the remaining balance after your payment.".format(credit_card_debt_after_payment, loan_debt_after_payment))

    # Extra Credit
    minimum_bills_due = total_utility_bills + credit_card_min_payment_due + loan_payment_due
    remaining_in_checking_min_payment = checking_account_balance - minimum_bills_due
    total_remaining_money_in_bank_min_payment = remaining_in_checking_min_payment + savings_account_balance
    interest_accrued_on_credit_card = (credit_card_balance_due - credit_card_min_payment_due) * (annual_credit_card_interest_rate / 12)
    credit_card_debt_after_min_payment = total_credit_card_debt - credit_card_min_payment_due + interest_accrued_on_credit_card
    total_debt_after_min_payment = loan_debt_after_payment + credit_card_debt_after_min_payment
    net_worth_after_min_payment = total_assets - total_utility_bills - loan_payment_due - credit_card_min_payment_due - \
                                  loan_debt_after_payment - credit_card_debt_after_min_payment

    print("\nEXTRA CREDIT:")
    print("If you choose not to pay off your full credit card balance due, ${:.2f}, and only pay the minimum payment due, ${:.2f}, you will have ${:.2f} left in your checking account, and ${:.2f} in your bank overall.".format(credit_card_balance_due, credit_card_min_payment_due, remaining_in_checking_min_payment, total_remaining_money_in_bank_min_payment))
    print("However, you will accrue ${:.2f} in interest on your credit card balance for the month.".format(interest_accrued_on_credit_card))
    print("Your total credit card debt will then be ${:.2f}.".format(credit_card_debt_after_min_payment))
    print("In this case, your total debt would instead be ${:.2f} and your net worth will be ${:.2f}.".format(total_debt_after_min_payment, net_worth_after_min_payment))


# Run the financial state calculator with sample values
calculate_net_worth()

