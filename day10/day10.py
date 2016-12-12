#!/usr/bin/env python3

"""Day 10: Balance Bots."""

INPUT_FILE = "day10_input.txt"
FIND_CHIPS = (61, 17)
# INPUT_FILE = "day10x_input.txt"
# FIND_CHIPS = (5, 2)

class BotNotReady(Exception):
    pass

class Bot:
    def __init__(self, bot_no, low_destination=None, high_destination=None):
        self.bot_no = bot_no
        self.low_dest = low_destination
        self.high_dest = high_destination
        self.chips = []

    def __str__(self):
        msg = "Bot {}, low {!r}, high {!r}. Chips: {!r}"
        return msg.format(self.bot_no, self.low_dest, self.high_dest, self.chips)

    def __len__(self):
        return len(self.chips)

    def __bool__(self):
        return len(self) == 2

    def give_chip(self, chip_value):
        self.chips.append(chip_value)

    def proceed(self, bots, outputs):
        if not self:
            raise BotNotReady
        if self.low_dest[0] == "bot":
            bots[self.low_dest[1]].give_chip(min(self.chips))
        else:
            outputs[self.low_dest[1]] = min(self.chips)
        if self.high_dest[0] == "bot":
            bots[self.high_dest[1]].give_chip(max(self.chips))
        else:
            outputs[self.high_dest[1]] = max(self.chips)
        self.chips = []
        return bots, outputs

def main():
    with open(INPUT_FILE, 'r') as input_file:
        descriptions = [line.strip() for line in input_file]
    bot_descriptions = []
    value_inputs = []
    for line in descriptions:
        parts = line.split()
        if parts[0] == "bot":
            bot_descriptions.append((int(parts[1]),
                                     (parts[5], int(parts[6])),
                                     (parts[10], int(parts[11]))))
        elif parts[0] == "value":
            parts = line.split()
            value_inputs.append((int(parts[1]), int(parts[5])))
        else:
            print("Unknown instruction:", line)

    bots = {}
    for bot_desc in bot_descriptions:
        bots[bot_desc[0]] = Bot(*bot_desc)

    for value in value_inputs:
        bots[value[1]].give_chip(value[0])

    outputs = {}
    while any([bot for bot in bots.values()]):
        for bot in bots.values():
            if FIND_CHIPS[0] in bot.chips and FIND_CHIPS[1] in bot.chips:
                msg = "Found chips {} and {} in bot {}!"
                print(msg.format(*FIND_CHIPS, bot.bot_no))
            if bot:
                bots, outputs = bot.proceed(bots, outputs)

    print(outputs[0]*outputs[1]*outputs[2])

if __name__ == "__main__":
    main()
