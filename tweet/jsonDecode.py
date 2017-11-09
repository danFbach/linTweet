import json
import operator
import matplotlib.pyplot as plt
import numpy as np
import time
import pathlib
from collections import OrderedDict
from pyasn1.compat.octets import null



class readjson():

    @staticmethod
    def decodej():
# var inits
        start_time = time.time()
        locationList = {}
        hashList = []
        hashtagPack = {}
        loc_names = []
        xhash = np.array([])
        yhash = np.array([])
        xloc = np.array([])
        yloc = np.array([])
        curHash = "#strangerthings"
# get data
        originalDataFilename = "strange1.json"
        fa = open(originalDataFilename)
        startFile = fa.readlines();
        startCount = len(startFile)
        quantity = input(' There are ' + str(startCount) +' tweets in \"' + originalDataFilename + '\".\n lease enter the number of tweets you would like to extract from this file. \n ===>')
        newFiletext = str(curHash).split('#')[1]
        fileToDecode = pathlib.Path(newFiletext + str(quantity) + '.json')
        if fileToDecode.is_file() is False:
            newDatapack = readjson.truncate(quantity, newFiletext, startFile)
# json thashtag tweet decoding
        for line in newDatapack:
            itemCount = 0
            thisTweetHash = []
            decodeLine = json.loads(line, object_pairs_hook=OrderedDict)
            if 'limit' not in decodeLine:
                location = decodeLine["user"]["location"]
                if location and not location.isspace():
                    location=str.lower(location)
                    if location in locationList:
                        locationList[location] += 1
                    else:
                        locationList.update({location: 1})
                    lineBreakup = line.split('\"')

                    for item in lineBreakup:
                        if item.__contains__(":"):
                            thisIs = None
                        if item.__contains__("{"):
                            thisIs = None
                        if item.__contains__(","):
                            thisIs = None
                        else:
                            if "entities" in item:
                                if "hashtag" in lineBreakup[itemCount + 2]:
                                    if"text" in lineBreakup[itemCount + 4]:
                                        tag = ""
                                        _tag = lineBreakup[itemCount + 6]
                                        curHash = str.lower(_tag)
                                        if curHash not in thisTweetHash:
                                            thisTweetHash.insert(0, curHash)
                                            if curHash in hashList:
                                                hashtagPack[curHash] += 1
                                            else:
                                                hashList.insert(0, curHash)
                                                hashtagPack.update({curHash: 1})
                        itemCount += 1
# build graph data
        counter1 = 0
        sorted_hashs = sorted(hashtagPack.items(), key=operator.itemgetter(1), reverse=True)
        hashLables = []
        for value in sorted_hashs:
            hashTitle = (value[0][:20] + '..') if len(value[0]) > 20 else value[0]
            if counter1 < 10:
                xhash = np.append(xhash, counter1, axis=None)
                yhash = np.append(yhash, value[1], axis=None)
                key_label = hashTitle + " - " + str(value[1])
                hashLables.append(key_label)
                counter1 += 1
        counter2 = 0
        sorted_locations = sorted(locationList.items(), key=operator.itemgetter(1), reverse=True)
        for value in sorted_locations:
            if counter2 < 10:
                if value[0] != "null":
                    xloc = np.append(xloc, counter2, axis=None)
                    yloc = np.append(yloc, value[1], axis=None)
                    key_label = value[0] + " - " + str(value[1])
                    loc_names.append(key_label)
                    counter2 += 1

        print(sorted_hashs[0:len(sorted_hashs)])
        print(sorted_locations[0:len(sorted_locations)])

        print("\n--- %s seconds ---" % (time.time() - start_time))
# build graphs
        plt.xticks(xloc, loc_names)
        plt.title("Common Locations")
        plt.stackplot(xloc, yloc, edgecolor='#4286f4', colors=('#FF4545', ), linewidth=4)
        plt.xlabel("xAxis")
        plt.show()

        plt.xticks(xhash, hashLables)
        plt.title("Common Hashtags")
        plt.stackplot(xhash, yhash, edgecolor='#FF4545', colors=('#4286f4', ), linewidth=2)
        plt.xlabel("xAxis")
        plt.show()

    @staticmethod
    def truncate(quantity, text, newData):
        datacount = 0
        resetCount = 0
        dataPack = []
        filename = text + str(quantity) + '.json'
        with open(filename, 'a') as fb:
            for line in newData:
                if resetCount is 1000:
                    fb.writelines(dataPack)
                    dataPack.clear()
                    resetCount = 0
                if datacount < int(quantity):
                        datacount += 1
                        resetCount += 1
                        dataPack.append(line)
                else:
                    fb.writelines(dataPack)
                    break
        thisFile = open(filename)
        return thisFile.readlines()

readjson.decodej()
