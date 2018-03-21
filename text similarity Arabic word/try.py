# -*- coding: utf-8 -*-
import codecs
import glob
class Word :
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2
        #self.m = m


    def open_file (self):

        read_file_1 = codecs.open(self.file1,"r","utf-8")
        read_file_2 = codecs.open(self.file2,"r","utf-8")

        text = read_file_1.read()
        text2 = read_file_2.read()

        return text , text2
    def split_word (self):
        text, text2 = self.open_file()
        f1words = text.split()
        f2words = text2.split()


        return f1words , f2words


    def counter (self):
        #if (self.m==1):

            #fwords= self.split_word()
        #else:
        fwords, swords = self.split_word()

        k = {}
        match = 0
        for w in fwords:
            if w in swords :
                match +=1
            k[w] = match
        return k

    def display_word (self):
        Dic = self.counter()
        for key,value in Dic.items():
            print key.encode('utf-8'), str(value).encode('utf-8')

#def directory_list():
 #   return  glob.glob("*.txt")



x = Word("file1.txt","file2.txt")
x.display_word()

