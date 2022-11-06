MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input('Enter the amout to deposit : $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Enter Valid Amount')
    print(f"You have deposited ${amount}")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}) : ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'Enter lines between 1-{MAX_LINES}')
        else:
            print('Enter valid number')
    print(f'You have bet on {lines} lines.')
    return lines

def get_bet_amount():
    while True:
        amount = input('What would you like to bet on each line : $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount to bet must be between ({MIN_BET}-{MAX_BET}).')
        else:
            print('Enter Valid Amount')
    print(f"You have bet on ${amount}")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}')
            reply = input('If you want to deposit more ? Y/N :')
            reply = reply.lower()
            if reply == 'y':
                balance = deposit()
            else:
                break
        else:
            break
    print(f'You are betting ${bet} on {lines} lines , your total bet is ${total_bet}.')
    print(balance, lines)

main()