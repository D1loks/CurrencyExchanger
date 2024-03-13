from .get_value import get_value


def change_currency_place(
        com_input_currencies, com_output_currencies, text_input_currencies, text_output_currencies, currency_lab1,
        buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2, currency_lab3, buy_lab3, sell_lab3, currency_lab4,
        buy_lab4, sell_lab4
):
    inp = com_input_currencies.get()
    out = com_output_currencies.get()
    com_input_currencies.set(out)
    com_output_currencies.set(inp)
    get_value(
        com_input_currencies.get(), com_output_currencies.get(), text_input_currencies.get("0.0", "end"),
        text_output_currencies, currency_lab1, buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2, currency_lab3,
        buy_lab3, sell_lab3, currency_lab4, buy_lab4, sell_lab4
    )
