import backtrader as bt

class PrintClose(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        print('Close, %.2f' % self.dataclose[0])