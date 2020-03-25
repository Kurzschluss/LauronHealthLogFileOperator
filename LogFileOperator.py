 
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class LogFileOperator(object):
    def __init__(self):
        self.fileList = []
        self.classDataList = []
        self.timeInterval = 100     # ms
        self.savePlots = True
        self.showPlots = True

    def getFileList(self):
        for file in os.listdir():
            if file.endswith(".csv"):
                self.fileList.append(os.path.join("", file))

    def calculate(self):
        pass

    def operate(self):
        for file in self.fileList:
            dataList = []
            timeList = []
            with open(file, 'r+', newline='') as file_object:
                fileReader = csv.reader(file_object, delimiter='\t', quotechar='|')
                i = 0
                for row in fileReader:
                    #for element in row: #?????
                    dataList.append(float(row[0]))
                    timeList.append(i*self.timeInterval)
                    i = i+1

            self.plotter(file, dataList, timeList)

    def plotter(self, title, timeList, dataList):
        fig, ax = plt.subplots(1, 1, constrained_layout=True)

        ax.plot(dataList, timeList)
        ax.set_xlabel("time [ms]")
        ax.set_ylabel("health")
        ax.grid(True)
        ax.set_ylim([-0.1, 1.1])

        fig.suptitle(title, fontsize=16)
        if self.savePlots:
            #fig.savefig(self.directory + title + ".png")
            fig.savefig(title + ".png")
        if self.showPlots:
            plt.show(block=True)
        else:
            plt.show(block=False)


def main():
    op = LogFileOperator()
    op.getFileList()
    op.operate()


if __name__ == '__main__':
    main()