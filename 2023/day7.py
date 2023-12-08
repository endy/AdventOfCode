
day = 7

problem_2=False
face_card_ranks = {'T': 0xA, 'J': 0xB, 'Q': 0xC, 'K': 0xD, 'A': 0xE }


def get_value(c):
    
    if c.isdigit():
        return int(c)
    else:
        return face_card_ranks[c]


def get_counts(hand):
    counts = {}
    for c in hand:
        counts[c] = counts.get(c, 0) + 1
    return counts

from enum import Enum

class HandValues(Enum):
    FiveKind = 7
    FourKind = 6
    FullHouse = 5
    ThreeKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


def get_hand_value(hand):

    hand_value = HandValues.HighCard

    card_counts = get_counts(hand[0])

    if problem_2  is True:
        keys = card_counts.keys()
        if 'J' in keys:
            max = 0
            max_key = 'J'
            for k, count in card_counts.items():
                if k == 'J':
                    continue
                if count > max:
                    max = count
                    max_key = k
            if max_key != 'J':
                card_counts[max_key] += card_counts['J']
                card_counts['J'] = 0


    for c, c_count in card_counts.items():
        if c_count == 5:
            hand_value = HandValues.FiveKind
            break
        if c_count == 4:
            hand_value = HandValues.FourKind
            break
        if c_count == 3:
            if hand_value == HandValues.OnePair:
                hand_value = HandValues.FullHouse
                break
            else:
                hand_value = HandValues.ThreeKind
        if c_count == 2:
            if hand_value == HandValues.ThreeKind:
                hand_value = HandValues.FullHouse
                break
            elif hand_value == HandValues.OnePair:
                hand_value = HandValues.TwoPair
                break
            else:
                hand_value = HandValues.OnePair

    fractional = ""
    for i, c in enumerate(hand[0]):
        fractional += hex(get_value(c))[2:]

    fractional = float(f"0.{int(fractional, base=16):07d}")  # pad string with 0s to max FFFFF

    return hand_value.value + fractional

hands = []

with open(f"day{day}_problem_input.txt", "r") as input_file:
    for l in input_file.readlines():
        hands.append(l.strip().split(' '))

def exec_problem():
    ranked_hands = sorted(hands, key=get_hand_value)

    total = 0
    for i, rh in enumerate(ranked_hands):
        total += int(rh[1]) * (i+1)

    return total

problem1 = exec_problem()

problem_2 = True
face_card_ranks['J'] = 1

problem2 =  exec_problem()


print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")
