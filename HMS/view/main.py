from functools import partial
import customtkinter as tk
from HMS.view.component.msg_handler import MessageBox
from HMS.view.management_panel.doctor import doctor_info
from HMS.view.management_panel.patient import patient_info
from HMS.view.management_panel.department import department_info
from HMS.model.entity.doctor import Doctor
from HMS.model.entity.patient import Patient
from HMS.controller.controller import Controller
from HMS.view.component.label_text import TextWithLabel
import HMS.view.management_panel.department.register as department_registration
import HMS.view.management_panel.department.department_table as department_list
import HMS.view.management_panel.department.search as department_search
import HMS.view.management_panel.appointment.register as appointment_registration
import HMS.view.management_panel.patient.register as patient_registration
import HMS.view.management_panel.doctor.register as doctor_registration
import HMS.view.management_panel.shifts.register as shift_registration
import HMS.view.management_panel.patient.info_table as patients_list
import HMS.view.management_panel.doctor.info_table as doctors_list
import HMS.view.management_panel.patient.search as patient_search
import HMS.view.management_panel.doctor.search as doctor_search
import HMS.view.management_panel.med_serv.register as med_serv_registration
import HMS.view.management_panel.med_serv.info_table as services_list
import HMS.view.management_panel.shifts.info_table as shifts_list


class Main:
    def __init__(self):
        self.logged_in_family = None
        self.logged_in_name = None
        self.win = tk.CTk()
        self.switch_var = tk.StringVar(value="on")
        self.right_buttons_list = []
        self.role = None
        self.logged_in = None
        self.win.title("HMS")
        self.win.geometry("600x400")
        tk.set_appearance_mode("dark")
        font_tuple = ("Vazir", 30,)
        tk.CTkLabel(self.win, text="ورود کاربر", font=font_tuple, fg_color="transparent").place(x=250, y=30)
        font_tuple = ("Vazir", 15,)
        self.login_user = TextWithLabel(self.win, text=": نام کاربری 👤", font_conf=font_tuple, x=320, y=90,
                                        distance=140, label_width=100, entry_width=130)
        self.login_pass = TextWithLabel(self.win, text=": کلمه عبور 🔐", x=320, y=125, font_conf=font_tuple,
                                        distance=140, label_width=100, entry_width=130, show='*')
        font_tuple = ("Vazir", 12,)
        tk.CTkButton(self.win, text="ورود", width=235, font=font_tuple, command=self.login).place(x=180, y=165)
        tk.CTkButton(self.win, text="فراموشی رمز عبور", font=font_tuple, width=235, command=self.login).place(x=180,
                                                                                                              y=195)
        tk.CTkButton(self.win, text="ثبت نام", width=235, font=font_tuple, command=self.login).place(x=180, y=225)

        self.win.mainloop()

    def login(self):
        username = self.login_user.text
        password = self.login_pass.text
        status, self.logged_in = Controller.login_check(username, password)
        self.logged_in_name = self.logged_in.name
        self.logged_in_family = self.logged_in.family
        if status:
            self.win.destroy()
            self.win = tk.CTk()
            self.win.title("HMS")
            w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
            self.win.geometry("%dx%d+0+0" % (w, h))
            self.raw()

            if self.logged_in.role == "Admin":
                self.admin_view()
            elif self.logged_in == "Doctor":
                pass
            elif self.logged_in == "Patient":
                pass
            self.win.mainloop()
        else:
            MessageBox.show_error(self.logged_in)

    def switch_event(self):
        if self.switch_var.get() == "off":
            tk.set_appearance_mode("light")
        else:
            tk.set_appearance_mode("dark")

    def logout(self):
        MessageBox.exit_question(master=self, message="آیا مطمئن هستید که میخواهید خارج شوید؟", option1="لغو",
                                 option2="خیر", option3="بله")

    def raw(self):
        to_per = {"Admin": "مدیریت"}
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        font_tuple = ("B Titr", 20,)

        tk.CTkLabel(self.win, text=f"سیستم مدیریت بیمارستان\n پنل {to_per[self.logged_in.role]}", bg_color="#374A69",
                    text_color="#E1F9FF", font=font_tuple, width=w, height=75).place(x=0, y=0)


        tk.CTkLabel(self.win, text=f"کاربر: {self.logged_in_name} {self.logged_in_family}👤", bg_color="#374A69",
                    text_color="#E1F9FF", font= ("Sahel", 13,), width=150,anchor="e", height=5).place(x=w-160, y=10)


        tk.CTkButton(self.win, text="خروج", font=font_tuple, bg_color="#374A69", command=self.logout).place(x=20,
                                                                                                            y=8)
        font_tuple = ("Sahel", 12,)
        switch = tk.CTkSwitch(self.win, text="حالت تیره🌓", command=self.switch_event, bg_color="#374A69",
                              font=font_tuple, variable=self.switch_var, onvalue="on", offvalue="off")
        switch.place(x=35, y=51)
        tk.CTkLabel(self.win, text="", bg_color="#C6CDDF", font=font_tuple, width=250, height=h).place(x=w - 250, y=75)
        self.right_panel()

    def on_button_click(self, button):
        list_ = ["پنل اصلی💢", "بیماران🦽", "پزشکان🩺", "شیفت ها⏳",
                 "نوبت دهی 📆", "خدمات🧾", "دپارتمان ها🏢", "پرداخت ها💲"]
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        for but in self.right_buttons_list:
            but.destroy()
            self.right_buttons_list = []

        match button:
            case "پنل اصلی💢":
                new_ = []
                self.clear_sc()
                self.admin_view()
            case "نوبت دهی 📆":
                new_ = ["ثبت نوبت جدید➕", "لیست بیماران🗂", "ویرایش بیمار✏️", "جزئیات بیمار🔍"]
            case "بیماران🦽":
                new_ = ["اضافه کردن بیمار➕", "لیست بیماران🗂", "ویرایش بیمار✏️", "جزئیات بیمار🔍"]
            case "پزشکان🩺":
                new_ = ["اضافه کردن پزشک➕", "لیست پزشکان🗂", "ویرایش پزشک✏️", "جزئیات پزشک🔍"]
            case "دپارتمان ها🏢":
                new_ = ["اضافه کردن دپارتمان➕", "لیست دپارتمان ها🗂", "ویرایش دپارتمان✏️", "جزئیات دپارتمان🔍"]
            case "خدمات🧾":
                new_ = ["اضافه کردن سرویس➕", "لیست سرویس ها🗂", "ویرایش سرویس✏️"]
            case "شیفت ها⏳":
                new_ = ["اضافه کردن شیفت➕", "لیست شیفت ها🗂", "ویرایش شیفت✏️"]
            case _:
                new_ = []

        font_tuple = ("Sahel", 15,)
        y = 85
        for i in list_:
            rm1 = tk.CTkButton(self.win, text=i, width=220, font=font_tuple, fg_color="#248DB6",
                               hover_color="#0F6BAE", bg_color="#C6CDDF", hover=True,
                               command=partial(self.on_button_click, i))
            rm1.place(x=w - 236, y=y)
            self.right_buttons_list.append(rm1)
            if i == button:
                for new in new_:
                    y += 40
                    rm1 = tk.CTkButton(self.win, text=new, width=200, font=font_tuple, fg_color="#248BD6",
                                       hover_color="#83B8FF", bg_color="#C6CDDF", hover=True,
                                       command=partial(self.on_button_click2, new))
                    rm1.place(x=w - 218, y=y)
                    self.right_buttons_list.append(rm1)
            y += 40

    def on_button_click2(self, button):
        font_tuple = ("Sahel", 15,)
        self.clear_sc()
        match button:
            case "ثبت نوبت جدید➕":
                appointment_registration.registration(self)
            case "اضافه کردن شیفت➕":
                shift_registration.registration(self)
            case "لیست شیفت ها🗂":
                shifts_list.view(self)
            case "اضافه کردن بیمار➕":
                patient_registration.registration(self)
            case "ویرایش بیمار✏️":
                user_id = TextWithLabel(self.win, ": کدملی", 1200, 210, entry_width=150, distance=160,
                                        font_conf=font_tuple)
                button = tk.CTkButton(self.win, text="✅", width=10, font=font_tuple, fg_color="#248DB6",
                                      hover_color="#0F6BAE", hover=True,
                                      command=partial(patient_registration.edit, self, user_id))
                button.place(x=990, y=212)
            case "جزئیات بیمار🔍":
                patient_search.search_patient(self)
            case "لیست بیماران🗂":
                patients_list.view(self)

            case "اضافه کردن پزشک➕":
                doctor_registration.registration(self)
            case "ویرایش پزشک✏️":

                user_id = TextWithLabel(self.win, ":کدملی", 1200, 210, entry_width=150, distance=160,
                                        font_conf=font_tuple)
                button = tk.CTkButton(self.win, text="✅", width=10, font=font_tuple, fg_color="#248DB6",
                                      hover_color="#0F6BAE", hover=True,
                                      command=partial(doctor_registration.edit, self, user_id))
                button.place(x=990, y=212)
            case "جزئیات پزشک🔍":
                doctor_search.search_doctor(self)
            case "لیست پزشکان🗂":
                doctors_list.view(self)

            case "اضافه کردن دپارتمان➕":
                department_registration.registration(self)
            case "لیست دپارتمان ها🗂":
                department_list.view(self)
            case "ویرایش دپارتمان✏️":
                user_id = TextWithLabel(self.win, ":ایدی دپارتمان", 1170, 210, entry_width=150, distance=160,
                                        font_conf=font_tuple)
                button = tk.CTkButton(self.win, text="✅", width=10, font=font_tuple, fg_color="#248DB6",
                                      hover_color="#0F6BAE", hover=True,
                                      command=partial(department_registration.edit, self, user_id))
                button.place(x=968, y=212)
            case "جزئیات دپارتمان🔍":
                department_search.search_department(self)

            case "اضافه کردن سرویس➕":
                med_serv_registration.registration(self)
            case "لیست سرویس ها🗂":
                services_list.view(self)
            case "ویرایش سرویس✏️":
                user_id = TextWithLabel(self.win, ":ایدی سرویس", 1170, 210, entry_width=150, distance=160,
                                        font_conf=font_tuple)
                button = tk.CTkButton(self.win, text="✅", width=10, font=font_tuple, fg_color="#248DB6",
                                      hover_color="#0F6BAE", hover=True,
                                      command=partial(med_serv_registration.edit, self, user_id))
                button.place(x=968, y=212)

            case _:
                new_ = []

    def search_department(self):
        status, p_list = Controller.search_by_department(self.name.text, self.department.text)
        if len(p_list) == 1:
            department_info.DepartmentInfo.show_menu(self, p_list)
        else:
            MessageBox.show_warning("دپارتمانی با این مشخصات یافت نشد")

    def search_patient(self):
        status, p_list = Controller.search_by_patient(self.name.text, self.family.text, self.user.text, self.phone.text,
                                                      self.gender.text, self.blood_type.text, self.birthday.text)

        if len(p_list) == 1:
            patient_info.PatientInfo.show(self, p_list[0])
        elif len(p_list) > 1:
            patient_info.PatientInfo.show_menu(self, p_list)
        else:
            MessageBox.show_warning("بیماری با این مشخصات یافت نشد")

    def search_doctor(self):
        status, d_list = Controller.search_by_doctor(self.name.text, self.family.text, self.user.text, self.phone.text,
                                                     self.specialty.text, self.sub_specialty.text, self.department.text,
                                                     self.birthday.text)

        if len(d_list) == 1:
            doctor_info.DoctorInfo.show(self, d_list[0])
        elif len(d_list) > 1:
            doctor_info.DoctorInfo.show_menu(self, d_list)
        else:
            MessageBox.show_warning("پزشکی با این مشخصات یافت نشد")

    def right_panel(self):
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        font_tuple = ("Sahel", 15,)
        list_ = ["پنل اصلی💢", "بیماران🦽", "پزشکان🩺", "شیفت ها⏳", "نوبت دهی 📆", "خدمات🧾", "دپارتمان ها🏢",
                 "پرداخت ها💲"]

        y = 85
        for it in list_:
            rm1 = tk.CTkButton(self.win, text=it, width=220, font=font_tuple, fg_color="#248DB6",
                               hover_color="#0F6BAE", bg_color="#C6CDDF", hover=True,
                               command=partial(self.on_button_click, it))
            rm1.place(x=w - 236, y=y)
            self.right_buttons_list.append(rm1)
            self.right_buttons_list.append(rm1)
            y += 40

    def admin_view(self):
        status, doctors = Controller.find_all(Doctor)
        if status:
            doctors = len(doctors)
            doctors = f"پزشکان⚕️\n{doctors}"
        status, patients = Controller.find_all(Patient)
        if status:
            patients = len(patients)
            patients = f"بیماران🦽\n{patients}"
        if status:
            shifts = 10
            shifts = f"شیفت های امروز⏳\n{shifts}"
        if status:
            appointment = 20
            appointment = f"نوبت های امروز📆\n{appointment}"
        _list = [appointment, shifts, doctors, patients,]

        font_tuple = ("B Titr", 20,)
        x = 20
        for i in _list:
            label = tk.CTkLabel(self.win, text=i, width=300, height=100, font=font_tuple, fg_color="#0F6BAE",
                                text_color="#D9E9FF", corner_radius=10)
            label.place(x=x, y=90)
            x += 315

    def add_admin(self):
        status, admin = Controller.add_person(self.name.text, self.family.text, self.user.text, self.password.text,
                                              self.passwrod2.text, self.birthday.text, "Admin", self.phone.text,
                                              self.email.text, self.address.text)

        if status:
            MessageBox.show_checkmark(master=self, message="ادمین با موفقیت ثبت شد!")
        else:
            MessageBox.show_error(f"Admin Registered failed because of {admin} error")

        self.clear_sc()

    def add_patient(self):
        status, patient = Controller.add_patient(self.name.text, self.family.text, self.user.text, self.password.text,
                                                 self.password2.text, self.birthday.text, "Patient", self.phone.text,
                                                 self.email.text, self.address.text, self.gender.text,
                                                 self.blood_type.text)

        if status:
            MessageBox.show_checkmark(master=self, message="بیمار با موفقیت ثبت شد")
        else:
            MessageBox.show_error(f"Patient Registered failed because of {patient} error")

        self.clear_sc()

    def add_doctor(self):
        status, doctor = Controller.add_doctor(self.name.text, self.family.text, self.user.text, self.password.text,
                                               self.password2.text, self.birthday.text, "Doctor", self.phone.text,
                                               self.email.text, self.address.text, self.specialty.text,
                                               self.department.text, self.sub_specialty.text, self.experience.text)

        if status:
            MessageBox.show_checkmark(master=self, message="پزشک با موفقیت به ثبت رسید!")
        else:
            MessageBox.show_error(f"Doctor Registered failed because of {doctor} error")
        self.clear_sc()

    def add_department(self):
        status, department = Controller.add_department(self.name.text, self.head_id.text)
        if status:
            MessageBox.show_checkmark(master=self, message="دپارتمان با موفقیت ثبت شد!")
        else:
            MessageBox.show_error(f"Department Registered failed because of {department} error")

    def add_med_serv(self):
        status, service = Controller.add_service(self.name.text, self.note.text)
        if status:
            MessageBox.show_checkmark(master=self, message="سرویس جدید با موفقیت ثبت شد!")
        else:
            MessageBox.show_error(f"Medical Service Registered failed because of {service} error")

    def clear_sc(self):
        for child in self.win.winfo_children():
            child.destroy()
        self.raw()

        if self.logged_in.role == "Admin":
            self.admin_view()
        elif self.logged_in == "Doctor":
            pass
        elif self.logged_in == "Patient":
            pass
