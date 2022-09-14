def cardSensor(nums):

    temp_str = ""
    i = 0
    while i <= len(nums)-4:
     if i % 5 != 0:
         temp_str += "#"
     else:
         temp_str += " "
     i += 1

    temp_str += nums[-4:]

    print(temp_str)

cardSensor("5124 4313 5456 7465")


    


    