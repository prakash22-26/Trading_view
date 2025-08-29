# trading/ib.py
from ib_insync import IB, Stock, MarketOrder, util
import asyncio

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

def get_margin():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(ib.accountSummaryAsync())
    loop.close()
    
    margin_info = {}
    for row in result:
        if row.tag in ['TotalCashValue', 'NetLiquidation', 'AvailableFunds', 'ExcessLiquidity', 'BuyingPower', 'RegTMargin', 'Cushion']:
            margin_info[row.tag] = f"{row.value} {row.currency}"
    return margin_info


def get_positions():
    positions = ib.positions()
    return [
        {
            "symbol": p.contract.symbol,
            "exchange": p.contract.exchange,
            "position": p.position,
            "avgCost": p.avgCost
        }
        for p in positions
    ]
