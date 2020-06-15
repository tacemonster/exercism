def recite(start_verse, end_verse):
    gifts = ["a Partridge in a Pear Tree", 
            "two Turtle Doves", 
            "three French Hens", 
            "four Calling Birds", 
            "five Gold Rings", 
            "six Geese-a-Laying", 
            "seven Swans-a-Swimming", 
            "eight Maids-a-Milking", 
            "nine Ladies Dancing", 
            "ten Lords-a-Leaping", 
            "eleven Pipers Piping", 
           "twelve Drummers Drumming"]
    days = {1:"first", 
            2:"second", 
            3:"third", 
            4:"fourth", 
            5:"fifth", 
            6:"sixth", 
            7:"seventh", 
            8:"eighth", 
            9:"ninth", 
            10:"tenth", 
            11:"eleventh", 
            12:"twelfth"}
    giftstring = gifts[0]
    for i in range(1,start_verse):
        if i == 1:
            giftstring = "{0}, and {1}".format(gifts[i], giftstring)
        else:
            giftstring = "{0}, {1}".format(gifts[i], giftstring)
    song = ["On the {0} day of Christmas my true love gave to me: {1}.".format(days[start_verse], giftstring)]
    for j in range(start_verse + 1,end_verse + 1):
        if j == 2:
            giftstring = "{0}, and {1}".format(gifts[j-1], giftstring)
        else:
            giftstring = "{0}, {1}".format(gifts[j-1], giftstring)
        song.append("On the {0} day of Christmas my true love gave to me: {1}.".format(days[j], giftstring))
    return song
        
        
