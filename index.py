import tkinter as tk
from tkinter import ttk
import subprocess
import os
import json
import random
from tkinter import messagebox
from tkinter import PhotoImage


class Program():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.resizable(False, False)
        self.frm = tk.Frame(self.root)
        self.frm.grid(padx=10)
        self.user = tk.StringVar()
        self.put_password = tk.StringVar()
        self.password = tk.StringVar()
        self.logo()
        self.menu_login()

    #Cargando logo
    def logo(self):
        self.img = PhotoImage(file="./imagen/original_ccexpress.png")
        tk.Label(self.frm, image=self.img, width=300).grid(column=0, row=0, columnspan=4, sticky="we")

    #login
    def login(self):
        #comprobando si existe el archivo
        verificacion = os.path.exists("Base_datos_usuario.json")
        #obteniendo y luego leyendo los datos de login
        user = self.user.get()
        password = self.password.get()
        if verificacion:
            with open("Base_datos_usuario.json") as file:
                var1 = json.load(file)
                for key, value in var1.items():
                    if user == value["User_Id"] and password == value["Password"]:
                        self.root.destroy()
                        ventanados()
                    elif len(user) == 0:
                        messagebox.showerror(message="Ingresar user")
                    elif len(password) == 0:
                        messagebox.showerror(message="Ingresar password")
                    else:
                        messagebox.showerror(message="Password o user estan mal")
                        self.user.set("")
                        self.password.set("")
        else:
            messagebox.showinfo(message="No hay ninguna persona agregada aun")

    #Menu
    def menu_login(self):
        #User
        tk.Label(self.frm, text="User:", font=("Space mono", 15)).grid(column=0, row=1)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat",
                 textvariable=self.user).grid(column=1, row=1, sticky="we")

        #Password
        tk.Label(self.frm, text="Password:", font=("Space mono", 15)).grid(column=0, row=2, pady=6)
        tk.Entry(self.frm, font=("Space mono", 12),
                relief="flat", textvariable=self.password).grid(column=1, row=2,columnspan=1, sticky="we")


        #Button login
        tk.Button(self.frm, text="Log in",
                font=("Space mono", 12), cursor="hand2", command=self.login).grid(
                column=0, row=3, columnspan=4, sticky="we", pady=6)

        
        #Separador
        ttk.Separator(self.frm, orient="horizontal"
                      ).grid(column=0, row=4, columnspan=4, sticky="we", pady=6)

        #Button New user
        tk.Button(self.frm, text="Create new user",
                font=("Space mono", 12), command=New_user, cursor="hand2").grid(
                column=0, row=5, columnspan=4, sticky="we", pady=6)

        self.root.mainloop()


class New_user:
    def __init__(self):
        self.datos = {}
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.dui = tk.StringVar()
        self.password = tk.StringVar()
        self.admin_password = tk.StringVar()
        self.window_admin_password()
    
    #Mostrando la ventana de ingreso de contra admin
    def window_admin_password(self):
    
        self.admin = tk.Toplevel(padx=10, pady=10)
        self.admin.resizable(False, False)
        self.admin.focus_set()
        tk.Label(self.admin, text="Put password", font=("Space mono", 15)).grid(column=0, row=0)
        tk.Entry(self.admin, font=("Space mono", 12), show="*", 
                textvariable=self.admin_password, relief="flat").grid(column=1, row=0)
        tk.Button(self.admin, text="Confirm",
                font=("Space mono", 12), cursor="hand2", command=self.Check_password).grid(
                column=0, row=1, columnspan=2, sticky="we", pady=10)
        self.admin.grab_set()

    #Comprobando contra de admin
    def Check_password(self):
        pass_admin = self.admin_password.get()
        if pass_admin == "qq":
            self.admin.destroy()

            #Corriendo la nueva ventana
            self.Menu_ingreso_user()
        else:
            self.admin_password.set("")
            messagebox.showerror(message="Contrasena incorrecta")

    #Ventana de ingreso de usuario
    def Menu_ingreso_user(self):
        self.menu_user =  tk.Toplevel(padx=10, pady=10)
        self.menu_user.resizable(False, False)
        self.menu_user.focus_set()

        #Nombres
        tk.Label(self.menu_user, text="Name:", font=("Space mono", 15)).grid(column=0, row=0, pady=5)
        tk.Entry(self.menu_user, font=("Space mono", 12), relief="flat",
                textvariable=self.name).grid(column=1, row=0, pady=5)

        #Apellidos
        tk.Label(self.menu_user, text="Last name:", font=("Space mono", 15)).grid(column=0, row=1, pady=5)
        tk.Entry(self.menu_user, font=("Space mono", 12), relief="flat",
                textvariable=self.last_name).grid(column=1, row=1, pady=5)

        #Dui
        tk.Label(self.menu_user, text="Dui:", font=("Space mono", 15)).grid(column=0, row=2, pady=5)
        tk.Entry(self.menu_user, font=("Space mono", 12), relief="flat",
                textvariable=self.dui).grid(column=1, row=2, pady=5)

        #Password
        tk.Label(self.menu_user, text="Password:", font=("Space mono", 15)).grid(column=0, row=3, pady=5)
        tk.Entry(self.menu_user, font=("Space mono", 12), relief="flat",
                textvariable=self.password).grid(column=1, row=3, pady=5)

        #Boton de confirmacion y guardado
        tk.Button(self.menu_user, text="Save", font=("Space mono", 12),
                cursor="hand2",command=self.guardado).grid(column=0, row=4, columnspan=2, sticky="we", pady=5)
        self.menu_user.grab_set()

    def Key_id(self):
        all = "1234567890poiuytrewqasdfghjklmnbvcxz"
        new_id = "".join(random.sample(all, 9))
        return new_id


    #Guardado de datos
    def guardado(self):
        name = self.name.get()
        last_name = self.last_name.get()
        dui = self.dui.get()
        password = self.password.get()
        comprobacion = os.path.exists("Base_datos_usuario.json")
        if len(name) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de names")
        elif len(last_name) ==0:
            messagebox.showinfo(message="Falta rellenar el campo de last name")
        elif len(dui) ==0:
            messagebox.showinfo(message="Falta rellenar el campo de dui")
        elif len(password) ==0:
            messagebox.showinfo(message="Falta rellenar el campo de password")

        #Comprobando si la base de datos de usuarios existe, si no existe la creara
        if comprobacion == False:
            #Modificando dui
            dui = [f for f in dui]
            dui.insert(8, "-")
            dui = "".join(dui)
            #Creando el User_id con el nombre y apellido
            all = F"{name} {last_name}"
            all = all.replace(" ", "")
            User_id = "".join(random.sample(all, 8))
            self.datos.setdefault(self.Key_id(),{
                "Name":name.title(),
                "Last_name": last_name.title(),
                "Dui":dui,
                "User_Id":User_id,
                "Password":password})
            #Creando base de datos y insertandole el nuevo usuario 
            with open("Base_datos_usuario.json", "w") as file:
                json.dump(self.datos, file, indent=4)
                messagebox.showinfo(message=f"""
Usuario creado

User: {User_id}
password: {password}
""")        
                self.menu_user.destroy()
        else:
            #Creando el User_id con el nombre y apellido
            all = F"{name} {last_name}"
            all = all.replace(" ", "")
            User_id = "".join(random.sample(all, 8))
            #Cargando la base de datos ya existente para luego agregarle el nuevo usuario
            with open("Base_datos_usuario.json") as file:
                    var1 = json.load(file)
                    var1[self.Key_id()] = {"Name":name.title(),
                                        "Last_name": last_name.title(),
                                        "Dui":dui,
                                        "User_Id":User_id,
                                        "Password":password}
                    with open("Base_datos_usuario.json", "w") as f:
                        json.dump(var1, f, indent=4)
                        messagebox.showinfo(message=f"""
Usuario agregado

User: {User_id}
Password: {password}
""")
                        self.menu_user.destroy()        
                
            


        
class ventanados():
    def __init__(self):
        #root
        self.root = tk.Tk()
        self.root.title("ventana dos")
        self.root.resizable(False, False)
        #Frame
        self.frm = tk.Frame(self.root, )
        self.frm.grid(padx=10, pady=10)
        #Variables
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.dui = tk.StringVar()
        self.number_phone = tk.StringVar()
        self.email = tk.StringVar()
        #Table
        self.tabla_datos()
        #Menubar
        self.Bar_menu()
        #Principal
        self.Pantalla_principal()

        
    #Funcion para abrir la terminal
    def terminal(self):
        return subprocess.call("xfce4-terminal")

    #ID
    def __id(self):
        numbers = "1234567890"
        letter = "poiuytrewqasdfghjklmnbvcxz"
        letter_up = letter.upper()
        all = numbers+letter+letter_up
        new_id = "".join(random.sample(all, 8))
        return new_id


    #Barra de menu con multiples opciones
    def Bar_menu(self):
        menubar = tk.Menu(self.root)

        #Opcion
        option = tk.Menu(menubar, tearoff=False)
        option.add_command(label="Option", font=("Space mono", 11))
        option.add_command(label="Editar", font=("Space mono", 11))
        option.add_command(label="Exit", font=("Space mono", 11), command=self.root.destroy)

        #Terminal
        terminal = tk.Menu(menubar, tearoff=False)
        terminal.add_command(label="Nueva terminal", font=("Space mono", 11),
                            command=self.terminal)
        
        #Agregando terminal en barra
        menubar.add_cascade(label="File", menu=option, font=("Space mono", 13))

        #Agregando opcion en la barra
        menubar.add_cascade(label="Terminal", menu=terminal, font=("Space mono", 13))
        self.root.config(menu=menubar)

    
    #Pantalla principal
    def Pantalla_principal(self):
        #Name
        tk.Label(self.frm, text="Name:", font=("Space mono", 15)).grid(column=0, row=0, pady=5)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat", width=60, textvariable=self.name).grid(
            column=1, columnspan=2, row=0, sticky="we", pady=5)

        #Last name
        tk.Label(self.frm, text="Last name:", font=("Space mono", 15)).grid(column=0, row=1, pady=5)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat", textvariable=self.last_name).grid(
            column=1, columnspan=2, sticky="we", row=1, pady=5)

        #Dui
        tk.Label(self.frm, text="Dui:", font=("Space mono", 15)).grid(column=0, row=2, pady=5)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat", textvariable=self.dui).grid(
            column=1, row=2, columnspan=2, sticky="we", pady=5)

        #Number phone
        tk.Label(self.frm, text="Number phone:", font=("Space mono", 15)).grid(column=0, row=3, pady=5)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat", textvariable=self.number_phone).grid(
            column=1, row=3, columnspan=2, sticky="we", pady=5)

        #Correo
        tk.Label(self.frm, text="Email:", font=("Space mono", 15)).grid(column=0, row=4, pady=5)
        tk.Entry(self.frm, font=("Space mono", 12), relief="flat", textvariable=self.email).grid(
            column=1, row=4, columnspan=2, sticky="we", pady=5)

        #Botones

        #Button cancel
        tk.Button(self.frm, text="Cancel", font=("Space mono", 12), cursor="hand2",
                width=11).grid(column=0, row=5, columnspan=1, sticky="we")

        #Button edit
        tk.Button(self.frm, text="Edit", font=("Space mono", 12), cursor="hand2",
                width=12).grid(column=1, row=5, columnspan=1, sticky="we", padx=15, pady=40)

        #Button save
        tk.Button(self.frm, text="Save", font=("Space mono", 12), cursor="hand2",
                width=10, relief="flat", bg="#008FE4",fg="white", command=self.Save_Registro
                ).grid(column=2, row=5, columnspan=1, sticky="we")

        self.root.mainloop()
        
    #Guardando todo el registro del formulario
    def Save_Registro(self):

        datos = {}
        verificacion = os.path.exists("Base_User.json")
        name = self.name.get()
        last_name = self.last_name.get()
        dui = self.dui.get()
        number_phone = self.number_phone.get()
        email = self.email.get()

        if len(name) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de nombre")
        elif len(last_name) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de apellido")
        elif len(dui) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de dui")
        elif len(number_phone) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de telefono")
        elif len(email) == 0:
            messagebox.showinfo(message="Falta rellenar el campo de email")
        else:
            dui = [f for f in dui]
            dui.insert(8, "-")
            dui = "".join(dui)

            #Creacion de base de datos si ya existe al menos uno
            if verificacion:
                with open("Base_User.json") as file:
                    var1 = json.load(file)
                    var1[self.__id()] = {
                        "Name":name.title(),
                        "Last_name":last_name.title(),
                        "Dui":dui,
                        "Number_phone":number_phone,
                        "Email":email}
                    with open("Base_User.json", "w") as write:
                        json.dump(var1, write, indent=4)
                    self.name.set("")
                    self.last_name.set("")
                    self.dui.set("")
                    self.number_phone.set("")
                    self.email.set("")
                    self.option = True

                        
            #Creando base de datos si el archivo no existe
            else:
                datos.setdefault(self.__id(), {
                    "Name":name.title(),
                    "Last_name": last_name.title(),
                    "Dui":dui,
                    "Number_phone":number_phone,
                    "Email":email})
                with open("Base_User.json", "w") as file:
                    json.dump(datos, file, indent=4)
                self.name.set("")
                self.last_name.set("")
                self.dui.set("")
                self.number_phone.set("")
                self.email.set("")
                self.option = True
        

    #Tabla de datos
    def tabla_datos(self):
            
        #Agregando campos a mostrar
        self.table = ttk.Treeview(self.frm,
        column=("Name", "Last_name", "Dui", "Number_phone","Email"))
        self.table.grid(column=0, row=6, columnspan=3, sticky="we")
        self.table.heading("#0", text="ID")
        self.table.heading("#1", text="Name")
        self.table.heading("#2", text="Last_name")
        self.table.heading("#3", text="Dui")
        self.table.heading("#4", text="Number_phone")
        self.table.heading("#5", text="Email")

        #Leyendo base de datos
        verificacion = os.path.exists("Base_User.json")
        if verificacion:
            with open("Base_User.json") as file:
                var1 = json.load(file)
                i = 0
                for key, value in var1.items():
                    for i in str(len(var1)):
                        i = i
                        self.table.insert("", i, text=f"{key}", values=(value["Name"], value["Last_name"],
                                                                        value["Dui"], value["Number_phone"],
                                                                        value["Email"]))
        else:
             self.table.insert("", 0, text="No hay nada")   

        #Agregando boton de eliminar
        tk.Button(self.frm, text="Eliminar", font=("Space mono", 12), cursor="hand2",
                  width=10, relief="flat", bg="#FF0E0E", fg="white"
                ).grid(column=0,row=7, columnspan=1, sticky="we")
            



if __name__ == '__main__':
    # application = Program()
    app = ventanados()