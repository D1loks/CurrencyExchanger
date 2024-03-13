from forex_python.converter import CurrencyRates


def get_value(
        com_input_currencies, com_output_currencies, text_input_currencies, text_output_currencies, currency_lab1,
        buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2, currency_lab3, buy_lab3, sell_lab3, currency_lab4,
        buy_lab4, sell_lab4
):
    try:
        text_value = float(text_input_currencies)
        currency_rates = CurrencyRates()
        result = currency_rates.convert(com_input_currencies, com_output_currencies, text_value)
        text_output_currencies.delete("1.0", "end-1c")
        text_output_currencies.insert("end-1c", str(round(result, 2)))
        if com_input_currencies == "USD":
            currency_lab1.configure(text="EUR", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('USD', 'EUR')
            eur_to_usd_sell = currency_rates.get_rate('EUR', 'USD')
            buy_lab1.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab1.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab2.configure(text="GBP", text_color="yellow")
            usd_to_gbp_buy = currency_rates.get_rate('USD', 'GBP')
            gbp_to_usd_sell = currency_rates.get_rate('GBP', 'USD')
            buy_lab2.configure(text=f"{round(usd_to_gbp_buy, 2)}🔺", text_color="green")
            sell_lab2.configure(text=f"{round(gbp_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab3.configure(text="CHF", text_color="yellow")
            usd_to_chf_buy = currency_rates.get_rate('USD', 'CHF')
            chf_to_usd_sell = currency_rates.get_rate('CHF', 'USD')
            buy_lab3.configure(text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green")
            sell_lab3.configure(text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab4.configure(text="PLN", text_color="yellow")
            usd_to_pln_buy = currency_rates.get_rate('USD', 'PLN')
            pln_to_usd_sell = currency_rates.get_rate('PLN', 'USD')
            buy_lab4.configure(text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green")
            sell_lab4.configure(text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green")
        elif com_input_currencies == "EUR":
            currency_lab1.configure(text="USD", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('EUR', 'USD')
            eur_to_usd_sell = currency_rates.get_rate('USD', 'EUR')
            buy_lab1.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab1.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab2.configure(text="GBP", text_color="yellow")
            usd_to_gbp_buy = currency_rates.get_rate('EUR', 'GBP')
            gbp_to_usd_sell = currency_rates.get_rate('GBP', 'EUR')
            buy_lab2.configure(text=f"{round(usd_to_gbp_buy, 2)}🔺", text_color="green")
            sell_lab2.configure(text=f"{round(gbp_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab3.configure(text="CHF", text_color="yellow")
            usd_to_chf_buy = currency_rates.get_rate('EUR', 'CHF')
            chf_to_usd_sell = currency_rates.get_rate('CHF', 'EUR')
            buy_lab3.configure(text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green")
            sell_lab3.configure(text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab4.configure(text="PLN", text_color="yellow")
            usd_to_pln_buy = currency_rates.get_rate('EUR', 'PLN')
            pln_to_usd_sell = currency_rates.get_rate('PLN', 'EUR')
            buy_lab4.configure(text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green")
            sell_lab4.configure(text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green")
        elif com_input_currencies == "GBP":
            currency_lab1.configure(text="USD", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('GBP', 'USD')
            eur_to_usd_sell = currency_rates.get_rate('USD', 'GBP')
            buy_lab1.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab1.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab2.configure(text="EUR", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('GBP', 'EUR')
            eur_to_usd_sell = currency_rates.get_rate('EUR', 'GBP')
            buy_lab2.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab2.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab3.configure(text="CHF", text_color="yellow")
            usd_to_chf_buy = currency_rates.get_rate('GBP', 'CHF')
            chf_to_usd_sell = currency_rates.get_rate('CHF', 'GBP')
            buy_lab3.configure(text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green")
            sell_lab3.configure(text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab4.configure(text="PLN", text_color="yellow")
            usd_to_pln_buy = currency_rates.get_rate('GBP', 'PLN')
            pln_to_usd_sell = currency_rates.get_rate('PLN', 'GBP')
            buy_lab4.configure(text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green")
            sell_lab4.configure(text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green")
        elif com_input_currencies == "CHF":
            currency_lab1.configure(text="USD", text_color="yellow")
            usd_to_chf_buy = currency_rates.get_rate('CHF', 'USD')
            chf_to_usd_sell = currency_rates.get_rate('USD', 'CHF')
            buy_lab1.configure(text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green")
            sell_lab1.configure(text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab2.configure(text="EUR", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('CHF', 'EUR')
            eur_to_usd_sell = currency_rates.get_rate('EUR', 'CHF')
            buy_lab2.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab2.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab3.configure(text="GBP", text_color="yellow")
            usd_to_gbp_buy = currency_rates.get_rate('CHF', 'GBP')
            gbp_to_usd_sell = currency_rates.get_rate('GBP', 'CHF')
            buy_lab3.configure(text=f"{round(usd_to_gbp_buy, 2)}🔺", text_color="green")
            sell_lab3.configure(text=f"{round(gbp_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab4.configure(text="PLN", text_color="yellow")
            usd_to_pln_buy = currency_rates.get_rate('CHF', 'PLN')
            pln_to_usd_sell = currency_rates.get_rate('PLN', 'CHF')
            buy_lab4.configure(text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green")
            sell_lab4.configure(text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green")

        elif com_input_currencies == "PLN":
            currency_lab1.configure(text="USD", text_color="yellow")
            usd_to_pln_buy = currency_rates.get_rate('PLN', 'USD')
            pln_to_usd_sell = currency_rates.get_rate('USD', 'PLN')
            buy_lab1.configure(text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green")
            sell_lab1.configure(text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab2.configure(text="EUR", text_color="yellow")
            usd_to_eur_buy = currency_rates.get_rate('PLN', 'EUR')
            eur_to_usd_sell = currency_rates.get_rate('EUR', 'PLN')
            buy_lab2.configure(text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green")
            sell_lab2.configure(text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab3.configure(text="GBP", text_color="yellow")
            usd_to_gbp_buy = currency_rates.get_rate('PLN', 'GBP')
            gbp_to_usd_sell = currency_rates.get_rate('GBP', 'PLN')
            buy_lab3.configure(text=f"{round(usd_to_gbp_buy, 2)}🔺", text_color="green")
            sell_lab3.configure(text=f"{round(gbp_to_usd_sell, 2)}🔺", text_color="green")

            currency_lab4.configure(text="CHF", text_color="yellow")
            usd_to_chf_buy = currency_rates.get_rate('PLN', 'CHF')
            chf_to_usd_sell = currency_rates.get_rate('CHF', 'PLN')
            buy_lab4.configure(text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green")
            sell_lab4.configure(text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green")

    except ValueError:
        if len(text_input_currencies) < 1:
            print("Введіть число")
        else:
            print("Введіть числа, а не букви!")
