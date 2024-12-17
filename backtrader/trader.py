import backtrader as bt
from strategy import TestStrategy
cerebro = bt.Cerebro()

cerebro.broker.set_cash(2000.0)

data = bt.feeds.YahooFinanceCSVData(dataname='final_tcs.csv')
cerebro.adddata(data)


cerebro.addstrategy(TestStrategy)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())