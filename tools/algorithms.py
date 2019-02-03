class algorithms():
    def luhn(self):
        print("\033[93mWARNING:\033[0m This uses the Luhn algorithm to check, so there is no guarantee that this is 100% accurate.")
        print("")
        purported = raw_input("Enter the credit card number: ")
        while purported.lower() != "exit":


            LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)  # sum_of_digits (index * 2)
            if not isinstance(purported, str):
                purported = str(purported)
            try:
                evens = sum(int(p) for p in purported[-1::-2])
                odds = sum(LUHN_ODD_LOOKUP[int(p)] for p in purported[-2::-2])
                if (((evens + odds) % 10 == 0)):
                    print("\033[92mCard number is valid\033[0m")

                    number = purported
                    first_two = number[0:2]
                    first_four = number[0:4]

                    vendor = None
                    if number[0] == 4:
                        vendor = 'Visa'
                    elif number[0] == '5' and '0' < number[1] < '6':
                        vendor = 'Mastercard'
                    elif number[0] == '6' or first_four == '6011':
                        vendor = 'Discover'
                    elif first_two in ('36', '38'):
                        vendor = "Diners Club"
                    elif first_two in ('34', '37'):
                        vendor = 'American Express'

                    if vendor is not None:
                        print('This seems like a \033[92m'+vendor+'\033[0m credit card!')
                    else:
                        print("\033[91mERROR:\033[0m Couldn't find the vendor of this card.")

                else:
                    print("\033[91mCard number is invalid\033[0m")

                print("")
            except ValueError:  # Raised if an int conversion fails
                print("\033[91mCard number is invalid\033[0m")
                print("")

            purported = raw_input("Enter the credit card number: ")
