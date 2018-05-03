def nb_year(p0, percent, aug, p):
#     p0 = current population
#     percent = increase per year
#     aug = additional inhabitants coming or leaving each year
#     p = population we need to surpass
    years = 0
#    while our current population is less than p
#     loop through and add the % increase to the current pop
#     add the additl inhabitants to pop
#     add 1 to the year
    while p0 < p:
        fpercent = float(percent)/100
        p0 = p0 + int(p0 * fpercent) + aug
        years += 1
    return years