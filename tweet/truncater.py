import time

class theTruncur():

    @staticmethod
    def trunc():
        startTime = time.time()
        fa = open("strange1.json")
        newData = fa.readlines();
        datacount = 0

        for line in newData:
            if datacount < 60000:
                with open('strange' + str(60000) + '.json', 'a') as f:
                    f.write(line)
                    datacount += 1
            else:
                break
        endTime = time.time() - startTime
        print(str(endTime) + " seconds")
theTruncur.trunc()