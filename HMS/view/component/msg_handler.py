from CTkMessagebox import CTkMessagebox
import customtkinter


class MessageBox:
    @staticmethod
    def show_info(title, message):
        CTkMessagebox(title=title, message=message, font=("Sahel", 12,),justify="center")

    @staticmethod
    def show_checkmark(master, message, option1="باشه"):
        msg = CTkMessagebox(message=message, icon="check", option_1=option1, font=("Sahel", 12,),justify="center")
        if msg.get() == option1:
            master.clear_sc()

    @staticmethod
    def show_error(message, error_title="Error"):
        msg = CTkMessagebox(title="Error", message=f"{message}!!!", icon="cancel", font=("Sahel", 12,),
                            justify="center")
        print(msg.get())

    @classmethod
    def show_warning(cls, message, option1="لغو", option2="تلاش مجدد", title="هشدار!"):
        msg = CTkMessagebox(title=title, message=message, icon="warning", option_1=option1, option_2=option2,
                            font=("Sahel", 12,), justify="center")

        if msg.get() == option2:
            cls.show_warning(message, option1="لغو", option2="تلاش مجدد", title="هشدار!")

    @classmethod
    def exit_question(cls, master, message, option1, option2, option3, title="خروج؟"):
        msg = CTkMessagebox(title=title, message=message, icon="question", option_1=option1, option_2=option2,
                            option_3=option3, font=("Sahel", 12,), justify="center")
        response = msg.get()

        if response == option3:
            master.win.destroy()
