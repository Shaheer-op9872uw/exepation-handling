try:
    num1 = int(input("enter number: "))
    num2 = int(input("enter num: "))
    result = num1/num2
    print("result is: ", result)
    print("result is: ", result1)

except ZeroDivisionError:
    print("divion by 0 isnt allowed")
except ValueError:
    print("enter a num value")
except NameError as ex:
    print("this exeption is ",ex)

except:
    print("some error is there ummmmm")
finally:
    print("i must do it no matter what ever will or is happening!!!!!")