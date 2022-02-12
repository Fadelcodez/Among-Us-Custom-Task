import pickle

hacked = False
input_task = input('- ')
codes = ('1234', '4321', '1324', '1243', 'ABCD', 'DCBA', 'ACBD', 'ABDC')
codes_imposter = ('1111', '2222', '3333', '4444', 'AAAA', 'BBBB', 'CCCC', 'DDDD')

if input_task in codes:
    hacked = pickle.load(open('impasta.dat', 'rb'))
    if hacked == False:
        print('Welcome to the Server')
        print('[TASK COMPLETE]')
    else:
        print('[SERVER HACKED] The Server has been hacked, please use the detect-hacks command to fix it')
if input_task in codes_imposter:
    hacked = True
    pickle.dump(hacked,open('impasta.dat', 'wb'))
    print('[HACKED] The Server has been hacked')
if input_task == 'detect-hacks':
    hacked = pickle.load(open('impasta.dat', 'rb'))
    if hacked == True:
        print('[HACK DETECTED] Server has been sabotaged')
        input_hack = input('Please confirm you are the Crewmate by writing your code - ')
        if input_hack in codes:
            print('[HACK FIXED] The Server is back online')
            hacked = False
            pickle.dump(hacked, open('impasta.dat', 'wb'))
        else:
            print('[FIX FAILED] The Server is still sabotaged')
    else:
        print('[HACK NOT FOUND] Server has not been sabotaged')
