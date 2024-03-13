from customtkinter import CTk, set_default_color_theme, set_appearance_mode, CTkFrame, CTkLabel, CTkComboBox, \
    CTkTextbox, CTkButton
from forex_python.converter import CurrencyRates

from Functions import get_value, change_currency_place


def main():
    root_tk = CTk()
    currency_rates = CurrencyRates()
    root_tk.title("Currency Exchanger")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    w = root_tk.winfo_screenwidth() // 2 - 150
    h = root_tk.winfo_screenheight() // 2 - 200
    root_tk.geometry(f'700x275+{w}+{h}')

    currency = ["USD", "EUR", "GBP", "CHF", "PLN"]

    buy_sell_currency_frame = CTkFrame(root_tk, border_width=2, border_color="yellow")
    buy_sell_currency_frame.pack(side='left', padx=(30, 0), ipady=50, ipadx=30)
    change_currency_frame = CTkFrame(root_tk, border_width=2, border_color="yellow")
    change_currency_frame.pack(side='right', padx=30, ipady=50, ipadx=50)

    lab_you_give = CTkLabel(change_currency_frame, text="You give", text_color="white", font=("helvetica", 16))
    lab_you_give.pack(anchor="nw", padx=30, pady=(30, 0))

    input_frame = CTkFrame(change_currency_frame, border_width=0, fg_color="transparent")
    input_frame.pack(anchor="nw", padx=30, pady=(0, 0))

    com_input_currencies = CTkComboBox(
        input_frame, values=currency, text_color="yellow", border_color="yellow",
        dropdown_text_color="yellow", state="readonly", width=100, height=30,
        command=lambda event: get_value(com_input_currencies.get(), com_output_currencies.get(),
                                        text_input_currencies.get("0.0", "end"), text_output_currencies,
                                        currency_lab1, buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2,
                                        currency_lab3, buy_lab3, sell_lab3, currency_lab4, buy_lab4, sell_lab4)
    )
    com_input_currencies.set(currency[1])
    com_input_currencies.pack(side="left", padx=(0, 5), pady=(0, 20))

    text_input_currencies = CTkTextbox(input_frame, width=150, height=35)
    text_input_currencies.pack(side="right", padx=(0, 30), pady=(0, 20))
    text_input_currencies.bind("<Return>",
                               lambda event: get_value(
                                   com_input_currencies.get(),
                                   com_output_currencies.get(),
                                   text_input_currencies.get("0.0", "end"),
                                   text_output_currencies, currency_lab1,
                                   buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2, currency_lab3, buy_lab3,
                                   sell_lab3, currency_lab4,
                                   buy_lab4, sell_lab4)
                               )

    change_place_btn = CTkButton(change_currency_frame, text="↕️", anchor="center", width=35, font=("helvetica", 16),
                                 text_color="yellow", fg_color="#333333", hover_color="#545454",
                                 command=lambda: change_currency_place(
                                     com_input_currencies, com_output_currencies,
                                     text_input_currencies, text_output_currencies,
                                     currency_lab1,
                                     buy_lab1, sell_lab1, currency_lab2, buy_lab2,
                                     sell_lab2, currency_lab3, buy_lab3, sell_lab3,
                                     currency_lab4,
                                     buy_lab4, sell_lab4
                                 )
                                 )
    change_place_btn.pack(anchor="ne", padx=(0, 10), pady=(0, 0))

    lab_you_get = CTkLabel(change_currency_frame, text="You get", text_color="white", font=("helvetica", 16))
    lab_you_get.pack(anchor="nw", padx=30, pady=(0, 0))
    output_frame = CTkFrame(change_currency_frame, border_width=0, fg_color="transparent")
    output_frame.pack(anchor="nw", padx=30, pady=(0, 0))
    com_output_currencies = CTkComboBox(
        output_frame, values=currency, text_color="yellow", border_color="yellow",
        dropdown_text_color="yellow", state="readonly", width=100, height=30,
        command=lambda event: get_value(com_input_currencies.get(), com_output_currencies.get(),
                                        text_input_currencies.get("0.0", "end"), text_output_currencies,
                                        currency_lab1, buy_lab1, sell_lab1, currency_lab2, buy_lab2, sell_lab2,
                                        currency_lab3, buy_lab3, sell_lab3, currency_lab4, buy_lab4, sell_lab4)
    )
    com_output_currencies.set(currency[0])
    com_output_currencies.pack(side="left", padx=(0, 5), pady=(0, 5))

    text_output_currencies = CTkTextbox(output_frame, width=150, height=35)
    text_output_currencies.pack(side="right", padx=(0, 20), pady=(0, 5))

    second_buy_sell_frame = CTkFrame(buy_sell_currency_frame, fg_color="transparent")
    second_buy_sell_frame.pack(padx=(0, 0), pady=(30, 0))
    currency_lab = CTkLabel(second_buy_sell_frame, text="Currency", text_color="White", font=("helvetica", 16))
    currency_lab.pack(side="left", padx=(0, 50), pady=(0, 0))
    buy_lab = CTkLabel(second_buy_sell_frame, text="Buy", text_color="White", font=("helvetica", 16))
    buy_lab.pack(side="left", padx=(0, 30), pady=(0, 0))
    sell_lab = CTkLabel(second_buy_sell_frame, text="Sell", text_color="White", font=("helvetica", 16))
    sell_lab.pack(side="left", padx=15, pady=(0, 0))
    second_buy_sell_frame1 = CTkFrame(buy_sell_currency_frame, fg_color="transparent")
    second_buy_sell_frame1.pack(padx=(10, 0), pady=(15, 0))
    currency_lab1 = CTkLabel(second_buy_sell_frame1, text="USD", text_color="yellow", font=("helvetica", 16))
    currency_lab1.pack(side="left", padx=(10, 50), pady=(0, 0))
    usd_to_eur_buy = currency_rates.get_rate('EUR', 'USD')
    eur_to_usd_sell = currency_rates.get_rate('USD', 'EUR')
    buy_lab1 = CTkLabel(second_buy_sell_frame1, text=f"{round(eur_to_usd_sell, 2)}🔺", text_color="green",
                        font=("helvetica", 16))
    buy_lab1.pack(side="left", padx=(0, 30), pady=(0, 0))
    sell_lab1 = CTkLabel(second_buy_sell_frame1, text=f"{round(usd_to_eur_buy, 2)}🔺", text_color="green",
                         font=("helvetica", 16))
    sell_lab1.pack(side="left", padx=15, pady=(0, 0))
    second_buy_sell_frame2 = CTkFrame(buy_sell_currency_frame, fg_color="transparent")
    second_buy_sell_frame2.pack(padx=(10, 0), pady=(8, 0))
    currency_lab2 = CTkLabel(second_buy_sell_frame2, text="GBP", text_color="yellow", font=("helvetica", 16))
    usd_to_gbp_buy = currency_rates.get_rate('EUR', 'GBP')
    gbp_to_usd_sell = currency_rates.get_rate('GBP', 'EUR')
    currency_lab2.pack(side="left", padx=(10, 50), pady=(0, 0))
    buy_lab2 = CTkLabel(second_buy_sell_frame2, text=f"{round(usd_to_gbp_buy, 2)}🔺", text_color="green",
                        font=("helvetica", 16))
    buy_lab2.pack(side="left", padx=(0, 30), pady=(0, 0))
    sell_lab2 = CTkLabel(second_buy_sell_frame2, text=f"{round(gbp_to_usd_sell, 2)}🔺", text_color="green",
                         font=("helvetica", 16))
    sell_lab2.pack(side="left", padx=15, pady=(0, 0))
    second_buy_sell_frame3 = CTkFrame(buy_sell_currency_frame, fg_color="transparent")
    second_buy_sell_frame3.pack(padx=(10, 0), pady=(8, 0))
    currency_lab3 = CTkLabel(second_buy_sell_frame3, text="CHF", text_color="yellow", font=("helvetica", 16))
    currency_lab3.pack(side="left", padx=(10, 50), pady=(0, 0))
    usd_to_chf_buy = currency_rates.get_rate('EUR', 'CHF')
    chf_to_usd_sell = currency_rates.get_rate('CHF', 'EUR')
    buy_lab3 = CTkLabel(second_buy_sell_frame3, text=f"{round(usd_to_chf_buy, 2)}🔺", text_color="green",
                        font=("helvetica", 16))
    buy_lab3.pack(side="left", padx=(0, 30), pady=(0, 0))
    sell_lab3 = CTkLabel(second_buy_sell_frame3, text=f"{round(chf_to_usd_sell, 2)}🔺", text_color="green",
                         font=("helvetica", 16))
    sell_lab3.pack(side="left", padx=15, pady=(0, 0))
    second_buy_sell_frame4 = CTkFrame(buy_sell_currency_frame, fg_color="transparent")
    second_buy_sell_frame4.pack(padx=(10, 0), pady=(8, 0))
    currency_lab4 = CTkLabel(second_buy_sell_frame4, text="PLN", text_color="yellow", font=("helvetica", 16))
    currency_lab4.pack(side="left", padx=(10, 50), pady=(0, 0))
    usd_to_pln_buy = currency_rates.get_rate('EUR', 'PLN')
    pln_to_usd_sell = currency_rates.get_rate('PLN', 'EUR')
    buy_lab4 = CTkLabel(second_buy_sell_frame4, text=f"{round(usd_to_pln_buy, 2)}🔺", text_color="green",
                        font=("helvetica", 16))
    buy_lab4.pack(side="left", padx=(0, 30), pady=(0, 0))
    sell_lab4 = CTkLabel(second_buy_sell_frame4, text=f"{round(pln_to_usd_sell, 2)}🔺", text_color="green",
                         font=("helvetica", 16))
    sell_lab4.pack(side="left", padx=15, pady=(0, 0))

    root_tk.mainloop()


if __name__ == "__main__":
    main()
