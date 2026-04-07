from metrics import calculate_all, get_stock_data

def run():
    df, ticker = get_stock_data()
    df, beta, rsi_val, price, yearly_high, yearly_low, distance_from_high, fund_df, pe_ratio, marketCap= calculate_all(df, ticker)
    return df, ticker, beta, rsi_val, price, yearly_high, yearly_low, distance_from_high, fund_df, pe_ratio, marketCap
