real = input()
out = input()

silly = []
quiet = "-"
quiet_count = 0
for i in range(0, len(real)):
    if i - quiet_count < len(out):
        if real[i] != out[i - quiet_count]:
            if real[i] == quiet:
                quiet_count += 1
            else:
                if not silly:
                    silly = [real[i], out[i - quiet_count]]
                    if len(real) == len(out):
                        break
                    if quiet == "-":
                        j = i + 1
                        while j < len(real):
                            if real[j] != real[i]:
                                if real[i:j+1] != out[i:j+1].replace(silly[1], silly[0]):
                                    quiet = real[i]
                                    quiet_count = 1
                                    silly = []
                                j = len(real)  #to exit while loop
                            j += 1
                else:
                    if real[i] != silly[0]:
                        quiet = real[i]
                        break
    else:
        quiet = real[i]
        break
print(silly[0], silly[1])
print(quiet)




        

