
import spjutkastare
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create a label and entry
        Label(self,
              text="Fil med spjutkastare:"
              ).grid(row=0, column=0, sticky=W)
        self.file_name_ent = Entry(self)
        self.file_name_ent.grid(row=0, column=1, sticky=W)

        # create a label and entry
        Label(self,
              text="Antal tävlingar:"
              ).grid(row=1, column=0, sticky=W)
        self.num_comp_ent = Entry(self)
        self.num_comp_ent.grid(row=1, column=1, sticky=W)

        # create buttons for running simulator

        self.bttn_sim = Button(self,
                               text="Kör tävlingarna",
                               command=self.bttn_sim_command)
        self.bttn_sim.grid(row=2, column=1, sticky=W)

        # create text field
        self.output_txt = Text(self, width=75, height=20, wrap=WORD)
        self.output_txt.grid(row=3, column=0, columnspan=2)

    def bttn_sim_command(self):
        try:
            fobj = open(self.file_name_ent.get())
            num_comp = int(self.num_comp_ent.get())
        except ValueError:
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, "Antal tävlingar skall vara ett heltal!")
        except IOError:
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, "Filen existerar inte!")
        else:
            output_text = "Filinläsningen misslyckades, formatet skall vara:\n Oliver Ojämn ; 19 ; 2.0"
            try:
                spjutkastarlista = spjutkastare.läs_in_från_sekvens(fobj)
            except (ValueError, IndexError):
                self.output_txt.delete(0.0, END)
                self.output_txt.insert(0.0, output_text)
            else:
                (resultatsträng_för_tävlingar, statistik) = \
                    spjutkastare.kör_flera_tävlingar(num_comp, spjutkastarlista)
                statistik_sträng = spjutkastare.skriv_ut_statistik(statistik)
                # display the output
                self.output_txt.delete(0.0, END)
                self.output_txt.insert(0.0, "Dags för tävlingarna!!\n" + resultatsträng_för_tävlingar)
                self.output_txt.insert(END, "Resultat\n" + statistik_sträng)


root = Tk()
root.title("Spjutkastartävling")
root.geometry("500x300")
my_app = Application(root)
root.mainloop()
