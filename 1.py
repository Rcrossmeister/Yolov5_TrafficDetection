# import os
#
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
# import torch
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# img = 'https://ultralytics.com/images/zidane.jpg'
#
# results = model(img)
# results.print()

word1 = 'abcabc'
word2 = 'abdcaba'

merge = ''
if word1 or word2 != '':
    if word1 == '':
        print(word2)
    elif word2 == '':
        print(word1)
    else:
        while word1 != '' and word2 != '':
            if ord(word1[0]) >= ord(word2[0]):
                merge += word1[0]
                word1 = word1[1:]
                print(merge)
                print(1)
                print(str(word1)+'---'+str(word2))

            else:
                merge += word2[0]
                word2 = word2[1:]
                print(merge)
                print(2)
                print(str(word1) + '---' + str(word2))
        if word2 == '':
            merge = merge + word1
        else:
            merge = merge + word2

print(merge)

