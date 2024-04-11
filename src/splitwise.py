def split_booty(*args: list[dict:{str, int}]):
    count = 0
    for wal in args:
        wal = wal.copy()
        if 'gold_ingots' in wal:
            count += wal['gold_ingots']
    w_1: {str, int} = {"gold_ingots": count // 3}
    count_1 = count % 3
    w_2: {str, int} = {"gold_ingots": count // 3 + (count_1 == 2)}
    w_3: {str, int} = {"gold_ingots": count // 3 + (1 <= count_1 <= 2)}
    return w_1, w_2, w_3


if __name__ == "__main__":
    wallet_1: {str, int} = {'gold_ingots': 3}
    wallet_2: {str, int} = {'gold_ingots': 2}
    wallet_3: {str, int} = {'apples': 10}
    wallet_4: {str, int} = {'gold_ingots': 6}
    wallet_5: {str, int} = {'gold_ingots': 9}
    wallet_6: {str, int} = {'apples': 10}
    wallet_7: {str, int} = {'gold_ingots': 0}
    wallet_8: {str, int} = {'gold_ingots': 11}
    wallet_9: {str, int} = {'apples': 10}
    wallet_10: {str, int} = {'gold_ingots': 415}
    wallet_11: {str, int} = {'gold_ingots': 12}
    wallet_12: {str, int} = {'apples': 10}
    print(
        split_booty(wallet_1, wallet_2, wallet_3, wallet_4, wallet_5, wallet_6, wallet_7, wallet_8, wallet_9, wallet_10,
                    wallet_11, wallet_12))
