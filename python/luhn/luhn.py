class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        char_count = len(self.card_num)
        if char_count < 2 or not self.card_num.isnumeric():
            return False
        i = char_count - 2
        test_string = self.card_num
        while i >= 0:
            value = int(self.card_num[i])
            value *= 2
            if value > 9:
                value -= 9
            test_string = test_string[:i] + str(value) + test_string[i+1:]
            i -= 2
        sum = 0
        for j in range(char_count):
            sum += int(test_string[j])
        if sum % 10:
            return False
        return True
