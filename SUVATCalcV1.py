##SUVAT Calc V1.0.0.1 by Anush Patel ##

print('SUVAT Calculator - If have no data leave blank')
##S= int(input('Please enter the displacement:'))
##U= int(input('Please enter the Inital velocity:'))
##V= int(input('Please enter the Final Velocity:'))
##A= int(input('Please enter the acceleration:'))
##T= int(input('Please enter the time taken:'))
CalcWhat = input('What would you like to calc?')
if CalcWhat == 't':
    VWhat= input('Do you have a V value?')
    if VWhat == 'y':
        UWhat = input('Do you have a U value')
        if UWhat =='y':
            AWhat = input('Do you have A value')
            if AWhat == 'y':
                AskA = float(input('Please Input Acceleration Value:'))
                AskV = float(input('Please input Final Velocity:'))
                AskU = float(input('Please input Inital Velocity:'))
                Test = (AskV-AskU)/AskA
                print(Test)
        elif UWhat =='n':
            print('Okay')
            AWhat_u = input('Do you have A value')
            if AWhat_u== 'y':
                AskA = float(input('Please Input Acceleration Value:'))
                AskV = float(input('Please input Final Velocity:'))
                AskU = float(input('Please input Inital Velocity:'))
                Test = (AskV-AskU)/AskA
                print(Test)
    if VWhat == 'n':
        print('Im afraid you need a Final Velocity')
##Calc = S*U*V*A*T
##print(Calc)
