##SUVAT Calc V1.1.0.0 by Anush Patel ##
## Project Penrose ##
## If Anyone wants to use this don't steal it. ##
## COMMENTED OUT REGIONS WILL BE FIXED AND INTERGRATED IN LATER BUILDS ##
print('SUVAT Calculator - If have no data leave blank')
##S= int(input('Please enter the displacement:'))
##U= int(input('Please enter the Inital velocity:'))
##V= int(input('Please enter the Final Velocity:'))
##A= int(input('Please enter the acceleration:'))
##T= int(input('Please enter the time taken:'))
## BREAKPOINT ABOVE == GOOOD ##
import cmath

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
                time_with_UVA = (AskV-AskU)/AskA
                print(time_with_UVA)
        elif UWhat =='n':
            print('Okay')
            AWhat_u = input('Do you have A value')
            if AWhat_u== 'y':
                a= float(input('Please Input Acceleration Value multiplied by 1/2:'))
                b = float(input('Please input Final Velocity:'))
                c = float(input('Please input the Displacement Value'))
                # calculates the discriminant=
                d = (b**2) - (4*a*c)
                sol1 = (-b-cmath.sqrt(d))/(2*a)
                sol2 = (-b+cmath.sqrt(d))/(2*a)
                print('The Time taken is {0} and {1}'.format(sol1,sol2))
                time_with_VAS = ('Thanks for using SUVAT Calc') 
                print(time_with_VAS)
            if AWhat_u == 'n':
                print ('You have messed up. You need V and/or U')
    if VWhat == 'n':
        print('Im afraid you need a Final Velocity')

if CalcWhat == 's':
    VWhat= input('Do you have a U value?')
    if VWhat == 'y':
        UWhat = input('Do you have a A value')
        if UWhat =='y':
            AWhat = input('Do you have T value')
            if AWhat == 'y':
                AskA = float(input('Please Input Acceleration Value:'))
                AskU = float(input('Please input Inital Velocity:'))
                AskT = float(input('Please input the time taken:'))
                displacement_with_UTA = AskU*AskT + AskA*AskT**2/2
                print(displacement_with_UTA)
        elif UWhat =='n':
            print('Okay')
            AWhat_u = input('Do you have A value')
            if AWhat_u== 'y':
                AskA = float(input('Please Input Acceleration Value:'))
                AskV = float(input('Please input Final Velocity:'))
                time_with_VAS = ('Coming soon') 
                print(time_with_VAS)
    elif VWhat == 'n':
        UWhat = input('Do you have a V value')
        if UWhat =='y':
            AWhat = input('Do you have T value')
            if AWhat == 'y':
                AAWhat = input('Do You have a A Value')
                if AAWhat == 'y':
                    AskA = float(input('Please Input Acceleration Value:'))
                    AskU = float(input('Please input Final Velocity:'))
                    AskT = float(input('Please input the time taken:'))
                    displacement_with_VTA = AskU*AskT - AskA*AskT**2/2
                    print(displacement_with_VTA)
####       elif UWhat =='n':
##            print('Okay')
##            AWhat_u = input('Do you have A value')
##            if AWhat_u== 'y':
##                AskA = float(input('Please Input Acceleration Value:'))
##                AskV = float(input('Please input Final Velocity:'))
##                time_with_VAS = ('Coming soon') 
##                print(time_with_VAS)
        
##Calc = S*U*V*A*T
##print(Calc)
