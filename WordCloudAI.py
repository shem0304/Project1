from collections import Counter
from konlpy.tag import Twitter, Okt
import pytagcloud
import matplotlib.image as img
import matplotlib.pyplot as pp
from matplotlib import font_manager, rc
import matplotlib
import webbrowser

#출처 : https://ericnjennifer.github.io/python_visualization/2018/01/21/PythonVisualization_Chapt3.html
def showGraph(wordInfo):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    pp.title('울산 인공지능 뉴스 검색 결과')
    pp.xlabel('주요 단어')
    pp.ylabel('빈도수')
    pp.grid(True)

    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    pp.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    pp.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    pp.show()

# 출처 : https://thinkwarelab.wordpress.com/2016/08/30/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EC%9C%BC%EB%A1%9C-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B7%B8%EB%A6%AC%EA%B8%B0/

def saveWordCloud(wordInfo, filename):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=150)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='korean', rectangular=False)
    webbrowser.open(filename)

def main():
    f = open('d:\\aihhi.txt', 'r', encoding="utf-8")

    data = f.read()

    print(data)

    nlp = Okt()
    nouns = nlp.nouns(data)
    print(nouns)
    count = Counter(nouns)

    #그래프
    wordInfo = dict()
    for tags, counts in count.most_common(30):
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
            print("%s : %d" % (tags, counts))

    showGraph(wordInfo)
    saveWordCloud(wordInfo, 'd:\\aiwordcloud.jpg')

    #print(count)
    #tag2 = count.most_common(50)
    #taglist = pytagcloud.make_tags(tag2, maxsize=150)
    #print(taglist)
    #pytagcloud.create_tag_image(taglist, 'd:\\aiwordcloud.jpg', size=(900, 600), fontname='korean', rectangular=False)
    #fileName = 'd:\\aiwordcloud.jpg'
    #ndarray = img.imread(fileName)
    #pp.imshow(ndarray)
    #pp.show()

if __name__ == "__main__":
    main()