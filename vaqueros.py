from receipt import Receipt
from ux.choice import Choice
from ux.ui import options


def main():
    print('Let\'s budget shit.')
    options()

    budgeting()


def budgeting():

    choice = input()
    choice = choice.upper()

    while choice != Choice.quit:
        if choice == Choice.view:
            view_budget()
        elif choice == Choice.add:
            receipt = add_cost()
            if item_confirmation(receipt):
                print('Congratulations, you have less money.')
            else:
                print('One more thing you don\'t have.')
        elif choice == Choice.summary:
            summary()

        options()
        choice = input()
        choice = choice.upper()


def view_budget():
    return

# Details about the cost are acquired, and a receipt for the new cost is
# created. The receipt contains all the information for the new burden on
# the budget. Way2go.


def add_cost():
    item = input('''
===>What item would you like to add?
    ''')
    cost = input('''
=======>How much you dropping?
        ''')
    freq = input('''
===========>How often are you dropping this?
            (daily, weekly, monthly, once)
            ''')
    r = Receipt()
    r.set_item(item)
    r.set_cost(cost)
    r.set_frequency(freq)
    return r

# Confirms with the user if this is something they really want to do. This
# step is important because, most of the time, whatever the user is trying
# to do is not necessary for human life. Water isn't necessary for human
# life.


def item_confirmation(receipt):
    save_item(receipt)
    return True


def save_item(receipt):
    return


def summary():
    print("Here is a summary of your accounts.")
    return


if __name__ == '__main__':
    main()
