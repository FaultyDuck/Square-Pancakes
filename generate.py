fresh = []

def add_array(nu1, nu2, nu3,
              nu4, nu5, nu6,
              nu7, nu8, nu9):
    free = {
        '1': nu1,
        '2': nu2,
        '3': nu3,
        '4': nu4,
        '5': nu5,
        '6': nu6,
        '7': nu7,
        '8': nu8,
        '9': nu9
    }

    fresh.append(free)
    print('Array added:',free['1'],free['2'],free['3'],
          free['4'],free['5'],free['6'],
          free['7'],free['8'],free['9']
          )

x=0
while True:
    if x < 9:
        imo = input('Enter numbers: ')
        list=[]
        list.append(imo)
        fresh.append(list)
        x=x+1
    else:
        break

for i in fresh[:]:
    print(*i)