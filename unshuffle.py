cards = {
    'AC': '52',
    'AD': '51',
    'AH': '50',
    'AS': '49',
    'KC': '48',
    'KD': '47',
    'KH': '46',
    'KS': '45',
    'QC': '44',
    'QD': '43',
    'QH': '42',
    'QS': '41',
    'JC': '40',
    'JD': '39',
    'JH': '38',
    'JS': '37',
    '10C': '36',
    '10D': '35',
    '10H': '34',
    '10S': '33',
    '9C': '32',
    '9D': '31',
    '9H': '30',
    '9S': '29',
    '8C': '28',
    '8D': '27',
    '8H': '26',
    '8S': '25',
    '7C': '24',
    '7D': '23',
    '7H': '22',
    '7S': '21',
    '6C': '20',
    '6D': '19',
    '6H': '18',
    '6S': '17',
    '5C': '16',
    '5D': '15',
    '5H': '14',
    '5S': '13',
    '4C': '12',
    '4D': '11',
    '4H': '10',
    '4S': '9',
    '3C': '8',
    '3D': '7',
    '3A': '6',
    '3S': '5',
    '2C': '4',
    '2D': '3',
    '2H': '2',
    '2S': '1',                    
}

while True:
    n = int(input())
    if 1 < n <= 52:
        arr = input()
        orr = arr.split()
        p = len(orr)
        jk = 0
        for pp in range(0,p):
            pp = orr
            for i in range(0,n):
                print(cards.get(orr[0]))
    else:
        break