#
str1="""Romans, which spared Ibiza from further destruction and allowed it to
continue its Carthaginian-Punic institutions well into the Empire days, when it became an official
Roman municipality. For this reason, Ibiza today contains
excellent examples of late Carthaginian-Punic civilization. During the Roman Empire,
the island became a quiet imperial outpost, removed from the important trading routes of the time"""
print str1.count("th"),"th"
print str1.count("a"),"a"
print str1.count("ex"),"ex"

str2=str1.replace("th","boom")
print str2
str3=str1.replace("a","ahaha")
print str3

yohhho=str1.split()
print len (yohhho)

text=str1.split(".")
print len (text)

def splitString (text,separator):
    words=text.split(separator)
    for word in words:
        print words


text="""Romans, which spared Ibiza from further destruction
and allowed it to
continue its Carthaginian-Punic institutions separator="""
splitString(text,"f")
